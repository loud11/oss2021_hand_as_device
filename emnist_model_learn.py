import tensorflow as tf
from emnist import extract_training_samples, extract_test_samples
from keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Reshape, Flatten

ascii_Big_start = 65
ascii_Small_start = 97

emnist_enum_by_class = [i for i in range(10)]
emnist_enum_by_class += [chr(i) for i in range(ascii_Big_start, ascii_Big_start + 26)]
emnist_enum_by_class += [chr(i) for i in range(ascii_Small_start, ascii_Small_start + 26)]

emnist_target_param = "bymerge"# 'balanced', 'byclass', 'bymerge', 'digits', 'letters', 'mnist'

INPUT_SHAPE = (28, 28, 1)
num_classes = 47

model = tf.keras.models.Sequential([
    Reshape((28, 28, 1), input_shape=(784,)),
    Conv2D(32, (3, 3), padding='SAME', activation='relu'),
    Conv2D(32, (3, 3), padding='SAME', activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Dropout(0.5),
    Conv2D(64, (3, 3), padding='SAME', activation='relu'),
    Conv2D(64, (3, 3), padding='SAME', activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Dropout(0.5),
    Flatten(),
    Dense(512, activation='relu'),
    Dropout(0.5),
    Dense(num_classes, activation='softmax')
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

train_x, train_y = extract_training_samples(emnist_target_param)
sample_shape = train_x[0].shape
test_x, test_y = extract_test_samples(emnist_target_param)
train_x = train_x.reshape(train_x.shape[0], 784, 1)
test_x = test_x.reshape(test_x.shape[0], 784, 1)
train_x = train_x / 255.
test_x = test_x / 255.

batch_size_param = 64
print("hello ~")

hist = model.fit(
    train_x,
    train_y,
    batch_size=batch_size_param,
    validation_data=(test_x, test_y),
)

print(hist.history)
scores = model.evaluate(test_x, test_y, verbose=0)
print("Accuracy: %.2f%%" % (scores[1] * 100))

filename = 'finalized_emnist_model_merged'
model.save(filename)
