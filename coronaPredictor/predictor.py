from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.vgg19 import preprocess_input
from tensorflow.keras.models import load_model, model_from_json
from django.conf import settings
import numpy as np


def load_neural_network(modelPath):
    json_file = open('/home/rodrigo/Área de Trabalho/corona-master/coronaPredictor/model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights(modelPath)
    loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    return loaded_model


def predict_covid(imagePath):
    img = load_img(settings.MEDIA_ROOT.replace("/media","") + imagePath, grayscale=False, target_size=(299, 299))
    img = img_to_array(img)
    img = preprocess_input(img)
    img = np.expand_dims(img, axis=0)
    base_model = load_neural_network("/home/rodrigo/Área de Trabalho/corona-master/coronaPredictor/model_weights.h5")
    pred = base_model.predict(img)

    return pred[0, 0] * 100