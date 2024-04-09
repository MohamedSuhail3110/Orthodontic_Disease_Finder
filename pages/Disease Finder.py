import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import  load_model
import streamlit as st
import numpy as np 

st.header('Orthodontic Disease Finder')
model = load_model('C:/Users/LOKI/Desktop/Orthodontic/Image_classify.keras')
data_cat = ['Teeth - Crooked Teeth', 'Teeth - Crossbite', 'Teeth - Excessive Overjet', 'Teeth - Overbite', 'Teeth - Space Between Teeth', 'Teeth - Underbite']
img_height = 180
img_width = 180
image =st.file_uploader(label='Upload your dataset')

image_load = tf.keras.utils.load_img((image), target_size=(img_height,img_width))
img_arr = tf.keras.utils.array_to_img(image_load)
img_bat=tf.expand_dims(img_arr,0)

predict = model.predict(img_bat)

score = tf.nn.softmax(predict)
st.image(image, width=200)
st.write('The disease name is: ' + data_cat[np.argmax(score)])
