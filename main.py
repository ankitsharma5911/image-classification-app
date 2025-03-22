from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.filechooser import FileChooserListView
import numpy as np
import tensorflow as tf
import cv2

class ImageClassifier(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.model = tf.lite.Interpreter(model_path="model.tflite")
        self.model.allocate_tensors()
        self.input_index = self.model.get_input_details()[0]['index']
        self.output_index = self.model.get_output_details()[0]['index']

        # UI Elements
        self.image = Image(size_hint=(1, 0.8))
        self.add_widget(self.image)
        
        self.label = Label(text="Upload an Image", font_size=24)
        self.add_widget(self.label)
        
        self.button = Button(text="Select Image", size_hint=(1, 0.1))
        self.button.bind(on_press=self.load_image)
        self.add_widget(self.button)

    def load_image(self, instance):
        # Simple FileChooser to pick image
        filechooser = FileChooserListView(on_selection=self.process_image)
        self.add_widget(filechooser)

    def process_image(self, filechooser, selection):
        if selection:
            img_path = selection[0]
            self.image.source = img_path
            self.predict(img_path)
            self.remove_widget(filechooser)

    def predict(self, img_path):
        # Read and preprocess the image
        img = cv2.imread(img_path)
        img = cv2.resize(img, (224, 224))  # Resize to match model input
        img = np.expand_dims(img, axis=0).astype(np.float32) / 255.0

        # Make prediction
        self.model.set_tensor(self.input_index, img)
        self.model.invoke()
        pred = self.model.get_tensor(self.output_index)
        class_label = np.argmax(pred)

        # Update UI
        self.label.text = f"Prediction: Class {class_label}"

class MainApp(App):
    def build(self):
        Window.size = (360, 640)
        return ImageClassifier()

if __name__ == '__main__':
    MainApp().run()
