# Use an official Python runtime as a parent image
FROM python:3.7-slim

COPY ./requirements.txt /app/requirements.txt

# Set the working directory to /app
WORKDIR /app

# # copy the requirements file into the image

COPY ./requirements.txt ./app

# # install the dependencies and packages in the requirements file
# RUN pip install --no-cache-dir -r requirements.txt


RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python
# RUN pip install flask
# RUN python -m pip install scikit-image
# RUN apt-get update && apt-get install -y python3-opencv

# Copy the current directory contents into the container at /app
COPY . /app

# # Make port 5005 available to the world outside this container
# EXPOSE 5000

# Define environment variable
ENV NAME MNIST-FLASK

# ENTRYPOINT [ "python" ]

# # Run app.py when the container launches
# CMD flask run --host 172.17.0.2