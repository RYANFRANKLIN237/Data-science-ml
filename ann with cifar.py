import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
import numpy as np

# Load CIFAR-10 dataset
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Normalize pixel values (scale from 0-255 to 0-1)
x_train, x_test = x_train / 255.0, x_test / 255.0

# Convert labels to categorical format (One-hot encoding)
y_train_cat = to_categorical(y_train, 10)
y_test_cat = to_categorical(y_test, 10)

### PART A: BUILDING A PERCEPTRON ###

# Define a simple perceptron model
perceptron = Sequential([
    Flatten(input_shape=(32, 32, 3)),  # Flatten the input image
    Dense(10, activation='softmax')  # Single-layer perceptron with 10 output classes
])

# Compile the model
perceptron.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the perceptron model
perceptron.fit(x_train, y_train_cat, epochs=10, batch_size=64, validation_data=(x_test, y_test_cat))

# Evaluate on test set
perceptron_score = perceptron.evaluate(x_test, y_test_cat, verbose=0)
print(f'Perceptron Test Accuracy: {perceptron_score[1]:.4f}')

### PART B: BUILDING AN ARTIFICIAL NEURAL NETWORK (ANN) ###

# Define an ANN with one hidden layer of 150 neurons
ann = Sequential([
    Flatten(input_shape=(32, 32, 3)),  # Flatten the input image
    Dense(150, activation='relu'),  # Hidden layer with 150 neurons
    Dense(10, activation='softmax')  # Output layer with 10 classes
])

# Compile the ANN model
ann.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the ANN model
ann.fit(x_train, y_train_cat, epochs=10, batch_size=64, validation_data=(x_test, y_test_cat))

# Evaluate on test set
ann_score = ann.evaluate(x_test, y_test_cat, verbose=0)
print(f'ANN Test Accuracy: {ann_score[1]:.4f}')

### CONFUSION MATRIX FOR BEST MODEL ###
# Select the best model based on accuracy
best_model = perceptron if perceptron_score[1] > ann_score[1] else ann

# Predict labels using the best model
y_pred = np.argmax(best_model.predict(x_test), axis=1)
y_true = y_test.flatten()  # Convert y_test to 1D for confusion matrix

# Compute confusion matrix
cm = confusion_matrix(y_true, y_pred)

# Plot confusion matrix
plt.figure(figsize=(10, 7))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=range(10), yticklabels=range(10))
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix of Best Model')
plt.show()
