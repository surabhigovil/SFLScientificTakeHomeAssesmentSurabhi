# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Set the working directory to /app
WORKDIR /app

# # copy the requirements file into the image

# COPY ./requirements.txt ./app

# # install the dependencies and packages in the requirements file
# RUN pip install --no-cache-dir -r requirements.txt

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install flask
# RUN python -m pip install scikit-image
# RUN apt-get update && apt-get install -y python3-opencv

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 5005 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME MNIST-FLASK

# Run app.py when the container launches
CMD ["python", "app.py"]