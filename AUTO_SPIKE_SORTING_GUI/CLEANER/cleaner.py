# -*- coding: utf-8 -*-
"""
@authors: %(Val-Calvo, Mikel and Alegre-Cortés, Javier)
@emails: %(mikel1982mail@gmail.com, jalegre@umh.es)
@institutions: %(Dpto. de Inteligencia Artificial, Universidad Nacional de Educación a Distancia (UNED), Postdoctoral Researcher Instituto de Neurociencias UMH-CSIC)
"""
#%%
from GLOBAL_CONSTANTS import CLEANER_DEEPL_H5_MODEL, LOSS, OPTIMIZER, BATCH_SIZE
from keras.models import load_model
import numpy as np

class spike_denoiser:
    
    def __init__(self):
        self.model = self.__load_model()
    
    def __load_model(self):
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