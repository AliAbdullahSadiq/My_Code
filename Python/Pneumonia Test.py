import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import os
import random
import pandas as pd
from sklearn.utils.class_weight import compute_class_weight

from tensorflow import keras
from keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dropout, Flatten, Dense
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img
from tensorflow.keras.preprocessing import image_dataset_from_directory

import warnings
warnings.filterwarnings('ignore')

# Path to your dataset
train_path = '/Users/ayesha/Documents/chest_xray/train'
test_path = '/Users/ayesha/Documents/chest_xray/test'

# List of class names
class_names = os.listdir(train_path)

def TrainModel():
    # Define and compile the model
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(256, 256, 3)),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dropout(0.1),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dropout(0.4),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dense(len(class_names), activation='softmax')
    ])

    history = model.compile(
        loss='categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy']
    )

    # Load the data for training and validation
    Train = tf.keras.utils.image_dataset_from_directory(
        directory=train_path,
        labels="inferred",
        label_mode="categorical",
        batch_size=32,
        image_size=(256, 256))

    Validation = tf.keras.utils.image_dataset_from_directory(
        directory='/Users/ayesha/Documents/chest_xray/val',
        labels="inferred",
        label_mode="categorical",
        batch_size=32,
        image_size=(256, 256))
    
    # Calculate class weights based on the training dataset
    train_labels = np.concatenate([y for x, y in Train], axis=0)
    class_labels = np.argmax(train_labels, axis=1)  # Convert one-hot encoded labels to class labels
    class_weights = compute_class_weight('balanced', classes=np.unique(class_labels), y=class_labels)
    class_weight_dict = {i: weight for i, weight in enumerate(class_weights)}

    # Train the model with class weights
    history = model.fit(Train, epochs=10, validation_data=Validation, class_weight=class_weight_dict)

    # Save the trained model
    model.save('Pneumonia_AI_Trained_Model_Test.h5')

    # Graph the loss and accuracy of the model
    history_df = pd.DataFrame(history.history)
    history_df.loc[:, ['loss', 'val_loss']].plot()
    history_df.loc[:, ['accuracy', 'val_accuracy']].plot()
    plt.show()

def TestModel():
    # Load the trained model
    model = tf.keras.models.load_model('Pneumonia_AI_Trained_Model_Test.h5')

    # Enter the path of the image you want to test
    test_image = tf.keras.utils.load_img(

        #"/Users/ayesha/Desktop/chest_xray/test/NORMAL/IM-0016-0001.jpeg",
        "/Users/ayesha/Desktop/chest_xray/train/NORMAL/IM-0135-0001.jpeg",

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
    TestModel()
else:
    print("Invalid input")