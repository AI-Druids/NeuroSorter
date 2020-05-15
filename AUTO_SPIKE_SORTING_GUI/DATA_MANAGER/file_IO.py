# -*- coding: utf-8 -*-
"""
@authors: %(Val-Calvo, Mikel and Alegre-Cortés, Javier)
@emails: %(mikel1982mail@gmail.com, jalegre@umh.es)
@institutions: %(Dpto. de Inteligencia Artificial, Universidad Nacional de Educación a Distancia (UNED), Postdoctoral Researcher Instituto de Neurociencias UMH-CSIC)
"""
#%%
from GLOBAL_CONSTANTS import SPIKES_EXPAND
from DATA_MANAGER.brpylib import NevFile
import numpy as np

class nev_manager:   
     
    def load(self, fileNames):
        self.initialize_spike_containers()
        
        ExperimentID = 0
        for file in fileNames:
            if file[-4:] == '.npy':
                self.__python_dict(file)
            ExperimentID += 1
        
    
    def save(self, path):
        np.save(path,self.spike_dict)
        
    def __python_dict(self, file):
        aux = np.load(file, allow_pickle=True)
        self.spike_dict = aux.item()
                
    def __expand(self,waveform):
        ini = np.zeros((SPIKES_EXPAND,))
        end = np.zeros((SPIKES_EXPAND,))
        return np.hstack((ini,waveform,end))

        

    
