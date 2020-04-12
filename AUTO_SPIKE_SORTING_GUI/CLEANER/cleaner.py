# -*- coding: utf-8 -*-
"""
@authors: %(Val-Calvo, Mikel and Alegre-Cortés, Javier)
@emails: %(mikel1982mail@gmail.com, jalegre@umh.es)
@institutions: %(Dpto. de Inteligencia Artificial, Universidad Nacional de Educación a Distancia (UNED), Postdoctoral Researcher Instituto de Neurociencias UMH-CSIC)
"""
#%%

from tensorflow.keras.models import model_from_json
import numpy as np

class spike_denoiser:
    
    def __init__(self):
        self.model = self.__load_model()
        
    def __load_model(self):
        json_file = open('./CLEANER/model_2.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        model = model_from_json(loaded_model_json)
        # load weights into new model
        model.load_weights("./CLEANER/model_weights_2.h5")
        model.compile(loss='categorical_crossentropy', optimizer='Nadam', metrics=['accuracy'])
        return model
        
    def run(self, waveforms):
        data = waveforms.copy()

        for i in range(0,data.shape[0]):
            data[i,:] = (data[i,:] - np.min(data[i,:])) / (np.max(data[i,:]) - np.min(data[i,:])).astype(float)

        scores = self.model.predict_proba(waveforms, batch_size=16)
        
        return scores 