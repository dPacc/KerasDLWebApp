# Backend for out Cat-Dog prediction Web-App

import base64
import numpy as np
import io
from PIL import Image
import keras
import tensorflow as tf
from keras import backend as K
from keras.models import Sequential
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from flask import request
from flask import jsonify
from flask import Flask

app = Flask(__name__)

def get_model():
    global model
    model = load_model('VGG16_cats_and_dogs.h5')
    print("* Model Loaded!")


def preprocess_image(image, target_size):
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    return image


print("* Loading Keras Model.....")
get_model()
graph  = tf.get_default_graph()

@app.route("/predict", methods=["POST"])
def predict():
    message = request.get_json(force=True)
    encoded = message["image"]
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    processed_image = preprocess_image(image, target_size=(224, 224))
    global graph
    with graph.as_default():
        prediction = model.predict(processed_image).tolist()

    response = {
        'prediction' : {
            'dog': prediction[0][0],
            'cat': prediction[0][1]
        }
    }

    return jsonify(response)
