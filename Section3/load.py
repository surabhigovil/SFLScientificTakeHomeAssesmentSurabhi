#load the trained model's structure and weights from json and h5 file
import numpy as np
# import keras.models
import torch
# from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from train import Net

def init():
	
    # json_file = open('modelStructure.json','r')
    # loaded_model_json = json_file.read()
    # json_file.close()
    # model = model_from_json(loaded_model_json)
    # model = torch.load_state_dict(torch.load('model_weights.pth'))
    # #compile and evaluate loaded model
    # model.eval()
    # return model

    model = Net()
    checkpoint = torch.load('modelWeights.pth')
    try:
        checkpoint.eval()
    except AttributeError as error:
        print (error)
    ### 'dict' object has no attribute 'eval'

    model.load_state_dict(checkpoint['state_dict'])
    ### now you can evaluate it
    model.eval()
    #loss,accuracy = model.evaluate(X_test,y_test)
    #print('loss:', loss)
    #print('accuracy:', accuracy)
    # graph = tf.compat.v1.get_default_graph()
    
    return model