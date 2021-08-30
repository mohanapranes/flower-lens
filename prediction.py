from keras.models import model_from_json
import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import os

json_file = open('model/model_final.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model/model_final.h5")
 

image = '/home/siva/mpw/projects/flower/oxford102/train/anthurium/train_21.jpg'
xt = np.array(Image.open(image).resize((128,128)))
xt = np.expand_dims(xt, axis=0)

preds = loaded_model.predict(xt)
predicted_batch = tf.squeeze(preds).numpy()
predicted_ids = np.argmax(predicted_batch, axis=-1)

val = str(predicted_ids)
myfile = open("lables.txt", 'r')
data_dict = {}
for line in myfile:
    key,name = line.strip().split(':')
    data_dict[key.strip()] = name.strip()
 
myfile.close()

if(val in data_dict):
	print(data_dict[val])
