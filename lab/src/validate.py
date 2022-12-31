
from tensorflow import keras
from pathlib import Path
import cv2
import numpy as np

DOGS = 0
CATS = 1

# Load the model
model = keras.models.load_model('classifier.h5')

# Make predictions on a batch of data
validate_dogs_path = Path('../processed/dogs/training')
batch_data = [] # Batch of images (or other data)
for i in range(1, 2):
    image_path = "cat.jpg" #str(validate_dogs_path / f'dog.{i}.jpg')
    image = cv2.imread(image_path)
    image = cv2.normalize(image, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    image = cv2.resize(image, (256, 256))
    # Crop image
    image = image[16:240, 16:240] # crop into shape of 224x224
    image = cv2.cvtColor(np.float32(image), cv2.COLOR_BGR2GRAY)
    image = np.reshape(image, (1,224, 224,1))
    batch_data.append(image)

total = len(batch_data)
correct = 0
for i in batch_data:
    p = model.predict(i) # A list of labels, one for each item in the batch
    # Get the label for each item in the batch
    if p >= 0.5:
        print(p)
        correct += 1
    print(p)
print(f'{correct} out of {total}')