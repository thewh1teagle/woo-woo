
from keras.models import load_model
import cv2
import numpy as np

CAT = 0
DOG = 1

IMAGE_WIDTH=128
IMAGE_HEIGHT=128
IMAGE_SIZE=(IMAGE_WIDTH, IMAGE_HEIGHT)
IMAGE_CHANNELS=3
model = load_model('model.h5')

def predict(bytes_image):
    buf = np.frombuffer(bytes_image, dtype=np.uint8)
    img = cv2.imdecode(buf, flags=cv2.IMREAD_COLOR)
    img = cv2.resize(img, (128, 128))
    img = img[:128, :128]
    img = img / 255
    img = np.expand_dims(img, axis=0)
    p = model.predict(img)
    p = p.argmax(axis=1)
    return p