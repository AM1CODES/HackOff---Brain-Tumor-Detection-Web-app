import streamlit as st #importing streamlit and tensorflow
import tensorflow as tf
import cv2
import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, BatchNormalization, Flatten
import numpy as np
from PIL import Image ,ImageOps


st.set_option('deprecation.showfileUploaderEncoding',False) #on loading a streamlit app we get a warning, this line prevents us from getting that warning

@st.cache(allow_output_mutation=True) #this line prevent us from loading the model again and again and will help in storing the model in cache once it has been loaded

def load_model(): #loading our model
  model = tf.keras.models.load_model('/content/BrainTumorModel .h5')
  return model

model = load_model()
#defining the header or title of the page that the user will be seeing

st.markdown("<h1 style='text-align: center; color: Black;'>Brain Tumor Classifier</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: Black;'>All you have to do is Upload the MRI scan and the model will do the rest!</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: Black;'>Submission for HackOff V3.0</h4>", unsafe_allow_html=True)
st.sidebar.header("What is this Project about?")
st.sidebar.text("It is a Deep learning solution to detection of Brain Tumor using MRI Scans.")
st.sidebar.header("What does it do?")
st.sidebar.text("The user can upload their MRI scan and the model will try to predict whether or not the user has Brain Tumor or not.")
st.sidebar.header("What tools where used to make this?")
st.sidebar.text("The Model was made using a dataset from Kaggle along with using Kaggle notebooks to train the model. We made use of Tensorflow, Keras as well as some other Python Libraries to make this complete project. To deply it on web, we used ngrok and Streamlit!")



file=st.file_uploader("Please upload your MRI Scan",type = ["jpg","png"]) #accepting the image input from the user

def import_and_predict(image_data,model): #our prediction method that will accept the data and the model and would give us a prediction
  size = (150,150)
  image1 = ImageOps.fit(image_data,size,Image.ANTIALIAS)
  image = ImageOps.grayscale(image1)
  img = np.asarray(image)
  img_reshape = img[np.newaxis,...]
  #img_reshape = img_reshape/255.0
  img_reshape = img.reshape(1,150,150,1)
  prediction = model.predict(img_reshape)
  return prediction

if file is None:
  st.markdown("<h5 style='text-align: center; color: Black;'>Please Upload a File</h5>", unsafe_allow_html=True)
else:
  image = Image.open(file)
  st.image(image,use_column_width = True)
  predictions = import_and_predict(image,model)
  class_names = ['glioma_tumor','meningioma_tumor','no_tumor','pituitary_tumor']
  string = "The patient most likely has:"+ class_names[np.argmax(predictions)]
  st.success(string)
  #st.success(predictions)