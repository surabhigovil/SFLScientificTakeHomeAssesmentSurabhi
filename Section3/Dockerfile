# # Use an official Python runtime as a parent image
FROM python:3

# COPY './requirements.txt' .

# # Set the working directory to /app
# WORKDIR /app

# # # copy the requirements file into the image

# # COPY ./requirements.txt ./app

# # # install the dependencies and packages in the requirements file
# # RUN pip install --no-cache-dir -r requirements.txt


# RUN pip install --upgrade pip

# RUN pip install -r requirements.txt

# RUN apt-get update && apt-get install -y python3-opencv
# RUN pip install opencv-python

# # RUN python -m pip install scikit-image
# # RUN apt-get update && apt-get install -y python3-opencv

# # Copy the current directory contents into the container at /app
# COPY . .

# # # Make port 5005 available to the world outside this container
# # EXPOSE 5000

# # Define environment variable
# ENV NAME MNIST-FLASK

# # ENTRYPOINT [ "python" ]

# # # Run app.py when the container launches
# CMD ["python","app.py"]

WORKDIR /app

COPY './requirements.txt' .

# RUN apt-get install libgtk2.0-dev pkg-config -yqq 

RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y python3-opencv

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]