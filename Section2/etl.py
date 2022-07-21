import re
import pandas as pd 
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, sessionmaker


class LoadCsv():
    def __init__(self):
        self.data = None
        self.path = None
        self.engine = None
        self.conn = None
        self.session = None
        self.user_table = None

    def create_conn(self):
        """ Create engine """
        url = 'mysql+pymysql://root:password@database:3306/testdb'
        try:
            self.engine = create_engine(url)
            self.conn = self.engine.connect()
           
            session_factory = sessionmaker(bind=self.engine)
            self.session = session_factory()

            print("Connection Created")

            if not self.load_db_tables():
                print("Failed to load tables")
                return False
            return True
        except Exception as e:
            print("Error connecting mysql: %s" % e)
            return False
    
    def load_db_tables(self):
        try:
            Base = automap_base()
            Base.prepare(self.engine, reflect=True)
            self.user_table = Base.classes.users
            return True
        except Exception as e:
            print("Failed to initalize tables: %s" % e)
            return False

    def load_csv(self):
        try:
            self.data = pd.read_csv(
                            self.path,
                            sep=",",
                            dtype=object)
            return True
        except Exception as e:
            print("Exception %s" % e)
            return False

    def mandatory_sanitization(self, val):
        """ mandatory sanitzation for all columns data """
        # strip whitespace and remove delimiter
        return val.str.strip().str.replace(";", "")
        return val

    def sanitize_business_name(self, val):
        p1, p2 = str(val).split(" ", 1)
        regex = re.compile(r"^([a-zA-Z0-9]\.)")
        if re.match(regex, p1):
            return "%s %s" % (p1.upper(), p2)
        else:
            return val

    def sanitize_date(self,val):
        from dateutil.parser import parse
        try:
            new_date = parse(val)
            return str(new_date)
        except Exception as e:
            print("Error Sanitizing date: %s" % e)
            return val
            

    def sanitize_mobile_numbers(self, val):
        """ Add "64" prefix to front of mobile number """
        if str(val).startswith("64"):
            return val
        else:
            return "64%s" % val
    
    def sanitize_landline_numbers(self, val):
        """ Add "09" prefix to front of landline number """
        if str(val).startswith("(09)") or str(val).startswith("09"):
            return val
        elif str(val).startswith("64"):
            return val
        else:
            return "09-%s" % val
    
    def sanitize_notes(self, val):
        """ Sanitize notes column """
        # sanitize emoji
        val = val.encode('ascii', 'ignore').decode('ascii')

        return val
    
    def main_sanitize_data(self):
        """ Main Sanitize function to sanitize data """
        # Sanitize column names
        self.data.columns = self.data.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

        # Mandatory Sanitization
        self.data = self.data.apply(self.mandatory_sanitization)

        # Specific Column Sanitization
        # self.data['id'] = self.data['id'].loc[self.data['business'].notnull()].apply(self.sanitize_business_name)
        # self.data['first_name'] = self.data['first_name'].str.capitalize()
        # self.data['last_name'] = self.data['last_name'].str.capitalize()
        # self.data['email'] = self.data['email'].loc[self.data['date_of_birth'].notnull()].apply(self.sanitize_date)
        # self.data['gender'] = self.data['gender'].loc[self.data['home_number'].notnull()].apply(self.sanitize_landline_numbers)
        # self.data['ip_address'] = self.data['ip_address'].loc[self.data['fax_number'].notnull()].apply(self.sanitize_landline_numbers)

        # Convert nan to None
        self.data = self.data.where(pd.notnull(self.data), None)
        
        print("Data Sanitization Successful")
        return True
    
    def import_to_db(self):
    
        for row in self.data.itertuples():
            if row.first_name is not None:
                if row.last_name is not None:
                    name = "%s %s" % (row.first_name,row.last_name)
                else:
                    name = "%s" % row.first_name
            elif row.last_name is not None:
                name = "%s" % row.last_name 
            else:
                name = None

            user_info = {
                        "first_name": row.first_name,
                        "last_name": row.last_name,
                        "email": row.email,
                        "gender": row.gender,
                        "ip_address":row.ip_address
                    }
            
            user = self.user_table(**user_info)
            self.session.add(user)
            self.session.commit()
            self.session.flush()
            self.session.refresh(user)
            id = user.id

        return True

    def run(self, path):
        self.path = path
        if not self.create_conn():
            return False

        if not self.load_csv():
            return False
        
        if not self.main_sanitize_data():
            return False
        
        if not self.import_to_db():
            return False
        
        return True

if __name__ == "__main__":
    print("Init loading csv")
    processor = LoadCsv()
    if processor.run("/app/data/DATA.csv"):
        print("Data ETL Successful")
    else:
        print("Data ETL Failed")