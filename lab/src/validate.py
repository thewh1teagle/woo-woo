
from tensorflow import keras
import cv2
import numpy as np
import settings

# Load the model
model = keras.models.load_model(settings.CLASSIFIER_PATH)

def validate(animal):
    animal_name = 'cat' if settings.CAT == animal else 'dog'
    data = []
    images_path = settings.PROCESSING_PATH
    images_path /= animal_name
    images_path /= 'validate'
    for i in range(settings.VALIDATING_START_IDX, 5110):
        
        image_path = images_path / f'{animal_name}.{i}.jpg'
        image_path = str(image_path)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        image = cv2.normalize(image, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
        image = np.reshape(image, (1, 224, 224,1)) # 224x224x1 (Grayscaled)
        data.append(image)
    total = len(data)
    correct = 0
    for i in data:
        p = model.predict(i)
        p = np.round(p)
        p = 1 if p >= 1 else 0
        if animal == p:
            correct += 1
        # else:
        #     cv2.imshow('', i[0])
        #     while cv2.waitKey(1) & 0xFF != ord('q'): pass
    return correct, total
    

if __name__ == '__main__':
    dogs_correct, dogs_total = validate(settings.DOG)
    cats_correct, cats_total = validate(settings.CAT)
    print(f'DOGS: {dogs_correct} out of {dogs_total} - {dogs_correct/100*dogs_total}')
    print(f'CATS: {cats_correct} out of {cats_total} - {cats_correct/100*cats_total}')