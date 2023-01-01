import pathlib
import cv2
import settings

def pre_process(image):
    # Resize image
    image = cv2.resize(image, (256, 256))
    
    # Crop image
    image = image[16:240, 16:240] # crop into shape of 224x224

    # Gray scale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image


def create_dataset(animal, validating = False):
    # For dogs training
    animal_name = 'dog' if animal == settings.DOG else 'cat'
    start_idx = settings.VALIDATING_START_IDX if validating else settings.TRAINING_START_IDX
    end_idx = settings.VALIDATING_END_IDX if validating else settings.TRAINING_END_IDX
    for i in range(start_idx, end_idx):
        image_path = settings.DOGS_PATH if animal == settings.DOG else settings.CATS_PATH
        image_path /= f'{animal_name}.{i}.jpg'
        image = cv2.imread(str(image_path))
        image = pre_process(image)
        outpath = settings.PROCESSING_PATH / f'{animal_name}'
        outpath /= 'validate' if validating else 'train'
        outpath /= f'{animal_name}.{i}.jpg'
        cv2.imwrite(str(outpath), image)

if __name__ == '__main__':
    # we have total of 12,500 images for each folder, dogs and cats.
    for animal in ['cat', 'dog']:
        training_path = settings.PROCESSING_PATH / animal / 'training'
        training_path.mkdir(parents=True, exist_ok=True)
        validating_path = settings.PROCESSING_PATH / animal / 'validating'
        validating_path.mkdir(parents=True, exist_ok=True)
    create_dataset(settings.DOG, validating=False)
    create_dataset(settings.DOG, validating=True)
    create_dataset(settings.CAT, validating=False)
    create_dataset(settings.CAT, validating=True)
