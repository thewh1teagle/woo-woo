import numpy
from pathlib import Path
import cv2
from tensorflow import keras
from keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D
from keras.models import Sequential
import settings


def get_model(input_shape):
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss=keras.losses.binary_crossentropy, optimizer=keras.optimizers.Adam(), metrics=['accuracy'])
    return model

def load_dataset(animal_type):
    animal_name = 'dog' if animal_type == settings.DOG else 'cat'
    training_path = settings.PROCESSING_PATH / f'{animal_name}/train'
    images = []
    for i in range(settings.TRAINING_START_IDX, settings.TRAINING_END_IDX):
        image = cv2.imread(str(training_path / f'{animal_name}.{i}.jpg'), cv2.IMREAD_GRAYSCALE)
        # normalize
        image = cv2.normalize(image, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
        images.append(image)
    # for i in images:
    #     cv2.imshow('', i)
    #     while cv2.waitKey(1) & 0xFF != ord('q'): pass
    return images

def train(dataset):
    input_shape = (224, 224, 1)
    model = get_model(input_shape)
    X = numpy.array([i for i in dataset])
    y = numpy.array([0 for _ in range(int(len(X)/2))]+[1 for _ in range(int(len(X)/2))])
    model.fit(X, y, epochs=10)
    return model

if __name__ == "__main__":
    print('Loading data...')
    dogs_dataset = load_dataset(settings.DOG)
    cats_dataset = load_dataset(settings.CAT)

    print('Training model...')
    model = train(dogs_dataset + cats_dataset)

    print('Saving model...')
    model.save(settings.CLASSIFIER_PATH)
    print('Done!')