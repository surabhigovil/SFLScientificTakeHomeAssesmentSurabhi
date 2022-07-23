from sqlalchemy import create_engine

def create_conn():
    """ Create engine """
    url = 'mysql+pymysql://test:secret@localhost:3306/userdb'
    engine = create_engine(url, pool_pre_ping=True)
    conn = engine.connect()
    print("tiger")
    print("Connection Created")
    return conn

def create_table(connection):
    result= []
    """ Create Table on Init """

    queries = [
        ("user","""
            CREATE TABLE user_info (
                id INT NOT NULL AUTO_INCREMENT,, 
                first_name VARCHAR(64),
                last_name VARCHAR(64),
                email VARCHAR(64), 
                gender VARCHAR(64),
                ip_address VARCHAR(255),
                PRIMARY KEY(id)
            );
        """)]
    
    for q in queries:
        table = q[0]
        query = q[1]

        try:
            connection.execute(query)
        except Exception as e:
            if "already exist" in str(e):
                print("Table %s already created" % table)
                result.append(True)
            else:
                print("Exception: %s" % e)
                result.append(False)
        else:
            print("Table %s created" % table)
            result.append(True)
    
    if all(result):
        return True
    else:
        return False

if __name__ == "__main__":
    conn = create_conn()
    create_table(conn)