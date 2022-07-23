# SFLScientificTakeHomeAssesmentSurabhi

Section1 uploaded as a PDF.

Section2:

ETL Pipeline created using Docker compose and Python. Docker compose creates a mysql database image and web app image. The db.py file creates a SqlAlchemy engine to connect to mysql database and create user db and user_info tables. The data is sanitize like removing spaces and speacial characters before being loaded in the db. etl.py perfroms the sanitizing operations on fields from the csv file.

Issues not able to resolve: 

on running docker-compose up getting errored out because docker not able to connect to localhost for mysql server. Tried chanig mysql conf local to allow biniding of address from outside localhost. Created user for mysql in the docker container with all privileges as root user. 

Section3:

MNIST PyTorch model deployed as a Flask app using docker.
Issues not able to resolve: 

ImportError: cannot import name 'QuantStub' from 'torch.ao.quantization' is constricting me from creating a docker container to deploy the falsk app.
