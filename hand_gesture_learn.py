import csv
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
import seaborn as sns
from tensorflow.keras.models import load_model
from sklearn.metrics import confusion_matrix


dataset = 'learning_data.csv'
NUM_CLASSES = 7
X_dataset = np.loadtxt(dataset, delimiter=',', dtype='float32', usecols=list(range(1, (21 * 2) + 1)))
y_dataset = np.loadtxt(dataset, delimiter=',', dtype='int32', usecols=(0))

X_train, X_test, y_train, y_test = train_test_split(X_dataset, y_dataset, train_size=0.75)

"""
model = load_model("hand_made_hand_guesture_model")
predicted_y = model.predict(X_test)
decoded_p_y = np.argmax(predicted_y, 1)

classification_matrix = confusion_matrix(y_test, decoded_p_y)
sns.heatmap(classification_matrix.T, square=True, annot=True, cbar=False, cmap=plt.cm.Blues)
plt.xlabel('predicted Values')
plt.ylabel('answer Values')
plt.show()
"""

model = tf.keras.models.Sequential([
    tf.keras.layers.Input((21 * 2, )),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(20, activation='relu'),
    tf.keras.layers.Dropout(0.4),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(NUM_CLASSES, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

hist = model.fit(
    X_train,
    y_train,
    epochs=1000,
    batch_size=128,
    validation_data=(X_test, y_test),
)

plt.figure()
plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.title('Accuracy')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

plt.figure()
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('LOSS')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

val_loss, val_acc = model.evaluate(X_test, y_test, batch_size=128)

print(val_loss, val_acc)
model_save_path = "hand_made_hand_guesture_model"
model.save(model_save_path, include_optimizer=False)