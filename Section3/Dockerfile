# Use an official Python runtime as a parent image
FROM python:3.6-slim

# # copy the requirements file into the image
# COPY ./requirements.txt /app/requirements.txt

# Set the working directory to /app
WORKDIR /app

# install the dependencies and packages in the requirements file
# RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 5005 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME MNIST-FLASK

# Run app.py when the container launches
CMD ["python", "app.py"]