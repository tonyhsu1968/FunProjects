import tensorflow as tf
import numpy as np
import json
import requests

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array

SIZE=128
MODEL_URI='http://localhost:8501/v1/models/my_model:predict'
CLASSES = ['Cat', 'Dog']

def get_prediction(image_path):
    #image = tf.keras.preprocessing.image.load_img(image_path, target_size=(SIZE, SIZE))
    #image = tf.keras.preprocessing.image.img_to_array(image)
    #image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
    #image = np.expand_dims(image, axis=0)
    
    image = load_img(image_path, target_size=(224, 224))
	# convert to array
    image = img_to_array(image)
	# reshape into a single sample with 3 channels
    image = image.reshape(1, 224, 224, 3)
	# center pixel data
    image = image.astype('float32')
    image = image - [123.68, 116.779, 103.939]
    #image = np.expand_dims(image, axis=0)

    data = json.dumps({
        'instances': image.tolist()
    })
    response = requests.post(MODEL_URI, data=data.encode('utf-8'))
    #print(response)
    result = json.loads(response.text)
    print(result)
    prediction = np.squeeze(result['predictions'][0])
    class_name = CLASSES[int(prediction > 0.5)]
    return class_name
