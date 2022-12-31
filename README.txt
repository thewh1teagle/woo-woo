Python program to classify between dogs and cats
It uses cnn network, the layers are
- input layer (explicity passed into second layer in the code)
- convolutional layer
- max pooling layer
- dropout layer
- flatten layer
- dense layer
- second dropout layer 
- output dense layer

Lab folder contains the code for preparing the dataset, 
and creating / validating the model

App folder contains a simple Flask web app to demonstrate the model, 
it allows the user to upload image of cat or dog, identifing using 
the classifier.h5 model we created, and then it shows the result in the app

Instructions:
get 12,500 cats and dogs images from https://www.kaggle.com/competitions/dogs-vs-cats/code
In lab folder, create these folders
/lab/images/{cats,dogs}/
/lab/processed/{cats,dogs}/{training,validating}
extract the zip file you just downloaded from kaggle 
and put the dogs and cats in the right folders under /lab/images/

Run pre_process.py
Run train.py
Run validate.py
validate that the model works. 
Not you can use classifier.h5 generated from training. check out app folder!


Mailstones:

1. Pre-process the images - make sure that they are all the same size, convert them to greyscale, and normalize the pixel values.

2. Split the data into training and testing sets - create separate datasets for training the model, and for validating it.

3. Build the model - Use a convolutional neural network (CNN) to classify the images.

4. Train the model - Input the training data and train the model using the selected optimizer.

5. Test the model - feed the testing set into the model and evaluate the results. 

6. Optimize the model - Tune the hyperparameters and perform validation until the model achieves the desired