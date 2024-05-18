from tensorflow import keras
import numpy as np

class Model():
    def __init__(self, current_directory) :
        self.model = keras.models.load_model(current_directory + "/model.h5")
    def predict(self, smart_infor: dict): 
        num_feature = len(smart_infor)
        input_predict = np.zeros((1, num_feature))
        for i, (key, value) in enumerate(smart_infor.items()):
            input_predict[0, i] = value
        predictions = self.model.predict(input_predict)
        predicted_classes = predictions.argmax(axis=1)
        return predicted_classes
    def test_predict(self, input_predict):
        predictions = self.model.predict(input_predict)
        predicted_classes = predictions.argmax(axis=1)
        print("test predict: ", predicted_classes)
        return predicted_classes