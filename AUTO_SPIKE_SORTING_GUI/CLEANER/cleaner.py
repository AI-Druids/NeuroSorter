# -*- coding: utf-8 -*-
"""
@authors: %(Val-Calvo, Mikel and Alegre-Cortés, Javier)
@emails: %(mikel1982mail@gmail.com, jalegre@umh.es)
@institutions: %(Dpto. de Inteligencia Artificial, Universidad Nacional de Educación a Distancia (UNED), Postdoctoral Researcher Instituto de Neurociencias UMH-CSIC)
"""
#%%
from GLOBAL_CONSTANTS import CLEANER_MODEL_LOAD_METHOD, CLEANER_DEEPL_H5_MODEL, CLEANER_DEEPL_JSON, CLEANER_DEEPL_WEIGHTS, LOSS, OPTIMIZER, BATCH_SIZE
from tensorflow.keras.models import model_from_json
from keras.models import load_model
import numpy as np

class spike_denoiser:
    
    def __init__(self):
        self.model = self.__load_model()
    
    def __load_model(self):
        if CLEANER_MODEL_LOAD_METHOD == 'json_weights':
            json_file = open(CLEANER_DEEPL_JSON, 'r')
            loaded_model_json = json_file.read()
            json_file.close()
            model = model_from_json(loaded_model_json)
            # load weights into new model
            model.load_weights(CLEANER_DEEPL_WEIGHTS)
        elif CLEANER_MODEL_LOAD_METHOD == 'h5':
            model = load_model(CLEANER_DEEPL_H5_MODEL)
        model.compile(loss=LOSS, optimizer=OPTIMIZER, metrics=['accuracy'])
        return model
        
    def run(self, waveforms):
        # minmax scaling in the range (0,1)
        for i in range(0,waveforms.shape[0]):
            waveforms[i,:] = (waveforms[i,:] - np.min(waveforms[i,:])) / (np.max(waveforms[i,:]) - np.min(waveforms[i,:])).astype(float)
        # inference on waveforms using the loaded model
        scores = self.model.predict_classes(waveforms, batch_size=BATCH_SIZE)
        print(scores)
        return scores 