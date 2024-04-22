# Imports
import matplotlib.pyplot as plt
import tensorflow as tf
import pandas as pd
import numpy as np
import random
import os
import matplotlib.image as mpimg

import warnings
warnings.filterwarnings('ignore')

from tensorflow import keras
from keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dropout, Flatten, Dense
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img
from tensorflow.keras.preprocessing import image_dataset_from_directory

path = '/Users/ayesha/Documents/chest_xray/train'
test_path = '/Users/ayesha/Documents/chest_xray/test'  
classes = os.listdir(path)

def TrainModel():
    
# Prepare data for training
    Train = keras.utils.image_dataset_from_directory(
        directory='/Users/ayesha/Documents/chest_xray/train',
        labels="inferred",
        label_mode="categorical",
        batch_size=32,
        image_size=(256, 256))

    Test = keras.utils.image_dataset_from_directory(
        directory='/Users/ayesha/Documents/chest_xray/test',
        labels="inferred",
        label_mode="categorical",
        batch_size=32,
        image_size=(256, 256))

    Validation = keras.utils.image_dataset_from_directory(
        directory='/Users/ayesha/Documents/chest_xray/val',
        labels="inferred",
        label_mode="categorical",
        batch_size=32,
        image_size=(256, 256))

    # Convolution Neural Network model
    model = tf.keras.models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(256, 256, 3)),
        layers.MaxPooling2D(2, 2),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D(2, 2),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D(2, 2),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D(2, 2),
        layers.Flatten(),
        layers.Dense(512, activation='relu'),
        layers.BatchNormalization(),
        layers.Dense(512, activation='relu'),
        layers.Dropout(0.1),
        layers.BatchNormalization(),
        layers.Dense(512, activation='relu'),
        layers.Dropout(0.2),
        layers.BatchNormalization(),
        layers.Dense(512, activation='relu'),
        layers.Dropout(0.2),
        layers.BatchNormalization(),
        layers.Dense(2, activation='sigmoid')
    ])

    model.compile(
        # specify the loss function to use during training
        loss='binary_crossentropy',
        # specify the optimizer algorithm to use during training
        optimizer='adam',
        # specify the evaluation metrics to use during training
        metrics=['accuracy']
    )

    # Train the model
    history = model.fit(Train, epochs=10, validation_data=Validation)

    # Evaluate the model
    history_df = pd.DataFrame(history.history)
    history_df.loc[:, ['loss', 'val_loss']].plot()
    history_df.loc[:, ['accuracy', 'val_accuracy']].plot()
    plt.show()

    # Save the Trained Model
    model.save('Pneumonia_AI_Trained_Model.h5')

# Test the model

def TestModel(test_path):
    # Load the trained model
    model = tf.keras.models.load_model('Pneumonia_AI_Trained_Model.h5')

    # Enter the path of the image you want to test
    test_image = tf.keras.utils.load_img(

        "/Users/ayesha/Desktop/chest_xray/test/NORMAL/IM-0016-0001.jpeg",

        target_size=(256, 256))

    # Display the image
    plt.imshow(test_image)

    # Convert the loaded image into a NumPy array
    test_image = tf.keras.utils.img_to_array(test_image)
    # Expand its dimensions to match the expected input shape of the model
    test_image = np.expand_dims(test_image, axis=0)

    # Use the trained model to make a prediction on the input image
    result = model.predict(test_image)

    # Check AI prediction
    class_probabilities = result[0]

    # Determine the class with the highest probability and print its label
    if class_probabilities[0] > class_probabilities[1]:
        print("Normal")
    else:
        print("Pneumonia")

    plt.show()


# Ask the user whether to train the model or test it
UserInput = input("Do you want to train the model or test it?: ")
if UserInput.lower().strip() == "train":
    TrainModel()
elif UserInput.lower().strip() == "test":
    TestModel(test_path)
else:
    print("Invalid input")