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
        ExperimentID = 0
        for file in fileNames:
            if file[-4:] == '.nev':
                nev_file = NevFile(file)
                ExperimentData = nev_file.getdata()
                self.__nevdata2dict(ExperimentData,ExperimentID)
                ExperimentID += 1
            elif file[-4:] == '.npy':
                self.__python_dict(file)
                ExperimentID += 1
        
    
    def save(self, path):
        np.save(path,self.spike_dict)
        
    def __python_dict(self, file):
        aux = np.load(file, allow_pickle=True)
        self.spike_dict = aux.item()
        
    def __nevdata2dict(self, ExperimentData, ExperimentID):
        for channel in range(len(ExperimentData['spike_events']['ChannelID'])):
            for event in range(len(ExperimentData['spike_events']['TimeStamps'][channel])):
                self.spike_dict['ExperimentID'].append( ExperimentID )
                self.spike_dict['ChannelID'].append( ExperimentData['spike_events']['ChannelID'][channel] )
                self.spike_dict['UnitID'].append( 1 )
                self.spike_dict['OldID'].append( None )           
                self.spike_dict['TimeStamps'].append( ExperimentData['spike_events']['TimeStamps'][channel][event] )
                waveform = self.__expand( ExperimentData['spike_events']['Waveforms'][channel][event]  )
                self.spike_dict['Waveforms'].append( waveform )           
    
    def __expand(self,waveform):
        ini = np.zeros((SPIKES_EXPAND,))
        end = np.zeros((SPIKES_EXPAND,))
        return np.hstack((ini,waveform,end))

        

    
