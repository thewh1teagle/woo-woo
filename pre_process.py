import pathlib
import cv2
from PIL import Image
import numpy as np


TRAINING_START_IDX = 1
TRAINING_STOP_IDX = 5001

VALIDATING_START_IDX = 5001
VALIDATING_STOP_IDX = 6001

def pre_process(image):
    # Resize image
    image = cv2.resize(image, (256, 256))
    
    # Crop image
    image = image[16:240, 16:240] # crop into shape of 224x224

    # Gray scale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image

if __name__ == '__main__':
    # we have total of 12,500 images for each folder, dogs and cats.
    for i in ['cats', 'dogs']:
        pathlib.Path(f'./processed/{i}/training').mkdir(parents=True, exist_ok=True)
        pathlib.Path(f'./processed/{i}/validating').mkdir(parents=True, exist_ok=True)
    dogs_path = pathlib.Path('./images/dogs')
    cats_path = pathlib.Path('./images/cats')
    

    # For dogs training
    j = 0
    for i in range(TRAINING_START_IDX, TRAINING_STOP_IDX):
        j += 1
        image_path = dogs_path / f'dog.{i}.jpg'
        image = cv2.imread(str(image_path))
        image = pre_process(image)
        output = pathlib.Path(f'./processed/dogs/training/dog.{j}.jpg') # it's not really jpg
        cv2.imwrite(str(output), image) # https://stackoverflow.com/questions/54165365/opencv2-imwrite-is-writing-a-black-image
        # cv2.imshow('', image)
        # while True:
        #     if cv2.waitKey(0) & 0xFF == ord('q'):
        #         break

    # for dogs validating
    j = 0
    for i in range(VALIDATING_START_IDX, VALIDATING_STOP_IDX):
        j += 1
        image_path = dogs_path / f'dog.{i}.jpg'
        image = cv2.imread(str(image_path))
        image = pre_process(image)
        output = pathlib.Path(f'./processed/dogs/validating/dog.{j}.jpg') # it's not really jpg
        cv2.imwrite(str(output), image)
        # cv2.imshow('', image)
        # while True:
        #     if cv2.waitKey(0) & 0xFF == ord('q'):
        #         break


    # for cats training
    j = 0
    for i in range(TRAINING_START_IDX, TRAINING_STOP_IDX):
        j += 1
        image_path = cats_path / f'cat.{i}.jpg'
        image = cv2.imread(str(image_path))
        image = pre_process(image)
        output = pathlib.Path(f'./processed/cats/training/cat.{j}.jpg') # it's not really jpg
        cv2.imwrite(str(output), image)


    # for cats validating
    j = 0
    for i in range(VALIDATING_START_IDX, VALIDATING_STOP_IDX):
        j += 1
        image_path = cats_path / f'cat.{i}.jpg'
        image = cv2.imread(str(image_path))
        image = pre_process(image)
        output = pathlib.Path(f'./processed/cats/validating/cat.{j}.jpg') # it's not really jpg
        cv2.imwrite(str(output), image)
