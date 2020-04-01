#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: %(Mikel Val Calvo)s
@email: %(mikel1982mail@gmail.com)
@institution: %(Dpto. de Inteligencia Artificial, Universidad Nacional de Educación a Distancia (UNED))
"""

from tensorflow.keras.models import model_from_json

class spike_denoiser:
    
    def __init__(self):
        print('cleaner')
        self.model = self.__load_model()
        
    def __load_model(self):
        json_file = open('./CLEANER/model_2.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        model = model_from_json(loaded_model_json)
        # load weights into new model
        model.load_weights("./CLEANER/model_weights_2.h5")
        print("Loaded model from disk")
        model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        print('model compiled')
        return model
        
    def run(self, waveforms):
        # evaluar el model
        scores = self.model.predict_proba(waveforms, batch_size=16)
        
        return scores 