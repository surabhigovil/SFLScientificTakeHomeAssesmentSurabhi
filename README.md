# SFLScientificTakeHomeAssesmentSurabhi

System Used: MacOS

Section1 uploaded as a PDF.

Section2:

ETL Pipeline created using Docker compose and Python. Docker compose creates a mysql database image and web app image. The db.py file creates a SqlAlchemy engine to connect to mysql database and create user db and user_info tables. The data is sanitized with techniques like removing spaces and speacial characters before being loaded in the db. etl.py perfroms the sanitizing operations on fields from the csv file.

The Transform is as follows in the etl.py: 
1. Using netaddr python dependency to mask ip address
2. Using regex pattern matching to validate email address before storing in database.

Issues not able to resolve: 

on running docker-compose up getting errored out because docker not able to connect to localhost for mysql server. Tried changing mysql conf local to allow biniding of address from outside localhost. Created user for mysql in the docker container with all privileges as root user. Also aading localhost connection on SOCKS proxies in system preferences of mac. The app builds fine but localhost cannot be resolved.

Run and usage: 
docker-compose up: spins up a mysql server instance and web app instance

Section3:

MNIST PyTorch model deployed as a Flask app using docker. train.py trains the PyTorch model and app.py has predict API to generate response.

Issues not able to resolve: 
Running docker container on localhost on mac. The docker container builds and runs successfully but I am having some problems accesing localhost on a Mac OS after running the container. I tried few port forwarding techniques and adding extra host in docker but the issue did not resolve.

Run and usage: 
1. docker build -t flask-ml-model-deploy:latest .
2. docker run -d -p 5000:5000 flask-ml-model-deploy
