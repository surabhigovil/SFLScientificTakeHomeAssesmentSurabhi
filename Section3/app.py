#import flask class
#render the html template to display the web
#request class to handle post/get methods
from flask import Flask, render_template, request
import imageio 
from imageio import imsave
from skimage.transform import resize
import cv2 as cv
import numpy as np
import keras.models
import re
import base64

import sys 
import os
#sys.path.append(os.path.abspath("."))
from load import *

#import cansandra packages to store the input and output data
import logging
import time
import socket


log = logging.getLogger()
log.setLevel('INFO')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)

#############

#init flask app
app = Flask(__name__)
global model, graph
model = init()
    
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict/', methods=['GET','POST'])
def predict():
    #get the time
    uploadtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    
    #whenever the predict method is called, we're going
    #to input the user drawn character as an image into the model
    #perform inference, and return the classification
    #get the raw data format of the image
    #read the image into memory
    formatImage(request.get_data())
    x =  cv.imread('output.png')
    x = x[:,:,0]
    #compute a bit-wise inversion so black becomes white and vice versa
    x = np.invert(x)
    #resize the image
    x = resize(x,(28,28))
    #convert to a 4D tensor to feed into our model
    x = x.reshape(1,28,28,1)
    # with graph.as_default():
    out = model.predict(x)
    
    print(out)
    print(np.argmax(out, axis=1))
    print(uploadtime)
    response = np.array_str(np.argmax(out, axis=1))
    print(str(response))
    return response

def formatImage(imgData):
    """Decode the input image to raw binary data and feed it into the graph"""
    imgstr = re.search(b'base64,(.*)', imgData).group(1)
    with open('output.png','wb') as output:
        output.write(base64.decodebytes(imgstr))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)