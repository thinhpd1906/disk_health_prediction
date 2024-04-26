from tensorflow import keras
import numpy as np

class Model():
    def __init__(self) :
        self.model = keras.models.load_model("C:/Users/phant/Downloads/my_model2.keras")
    def predict(self, smart_infor: dict): 
        num_feature = len(smart_infor)
        input_predict = np.zeros((1, num_feature))
        for i, (key, value) in enumerate(smart_infor.items()):
            input_predict[0, i] = value
        # print(input_predict)
        predictions = self.model.predict(input_predict)
        predicted_classes = predictions.argmax(axis=1)
        print("Predicted classes:", predicted_classes)
        return predicted_classes