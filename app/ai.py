
import tensorflow
from tensorflow import keras
from pathlib import Path
import cv2
import numpy as np

DOG = 0
CAT = 1

# Load the model
model = keras.models.load_model('classifier.h5')


def predict(bytes_image):
    np_image = np.frombuffer(bytes_image, dtype=np.uint8)
    image = cv2.imdecode(np_image, flags=1)
    image = cv2.normalize(image, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    image = cv2.resize(image, (256, 256))
    # Crop image
    image = image[16:240, 16:240] # crop into shape of 224x224
    image = cv2.cvtColor(np.float32(image), cv2.COLOR_BGR2GRAY)
    image = np.reshape(image, (1,224, 224,1))
    p = model.predict(image) # A list of labels, one for each item in the batch
    # Get the label for each item in the batch
    p = p[0]
    result = np.round(p)
    result = DOG if result <= 0.5 else CAT
    return result