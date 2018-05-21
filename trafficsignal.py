# -*- coding: utf-8 -*-
"""
Created on Sat May 19 11:47:54 2018

@author: sainath.kommineni
"""

# Convolutional Neural Network

# Installing Theano
# pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# Installing Tensorflow
# Install Tensorflow from the website: https://www.tensorflow.org/versions/r0.12/get_started/os_setup.html

# Installing Keras
# pip install --upgrade keras

# Part 1 - Building the CNN

# Importing the Keras libraries and packages


from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

# Initialising the CNN
classifier = Sequential()

# Step 1 - Convolution
classifier.add(Conv2D(32,( 3, 3), input_shape = (480, 640, 3), activation = 'relu'))

# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Adding a second convolutional layer
classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full connection
#classifier.add(Dense( activation = 'relu',units= 128))
#classifier.add(Dense( activation = 'softmax',units = 3))
classifier.add(Dense( output_dim = 128, activation = 'relu'))
classifier.add(Dense( output_dim = 3, activation = 'softmax'))

# Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Part 2 - Fitting the CNN to the images

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('data/train',
                                                 target_size = (480, 640),
                                                 batch_size = 16,
                                                 class_mode = 'categorical')

test_set = test_datagen.flow_from_directory('data/test',
                                            target_size = (480,640),
                                            batch_size = 8,
                                            class_mode = 'categorical')

classifier.fit_generator(training_set,
                         steps_per_epoch = 488,
                         nb_epoch = 1,
                         validation_data = test_set,
                         validation_steps = 32)

classifier.save('trafficsignalmodel.h10')

#Test for a single Image - CNN
import os
import numpy as np
import cv2
cwd = os.getcwd()
from keras.preprocessing import image
test_image = cv2.imread(cwd+'\\ButterflyVALV (2).Png',0) # 0 - Greyscale , 1 -Color 
img = np.reshape(test_image,[600,800,1])
test_image = np.expand_dims(img, axis = 0)
result = classifier.predict(test_image)
training_set.class_indices
