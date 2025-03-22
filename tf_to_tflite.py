import tensorflow as tf

# Load your Keras model
model = tf.keras.models.load_model('MobileNetV2-100-(224,224)-90.2.h5')

# Convert to TFLite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the model
with open('model.tflite', 'wb') as f:
    f.write(tflite_model)
