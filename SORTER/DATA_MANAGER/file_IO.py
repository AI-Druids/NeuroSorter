#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: %(Mikel Val Calvo)s
@email: %(mikel1982mail@gmail.com)
@institution: %(Dpto. de Inteligencia Artificial, Universidad Nacional de Educación a Distancia (UNED))
"""
from DATA_MANAGER.brpylib import NevFile
import numpy as np

class nev_manager:   
     
    def load_nev(self, fileNames):
        ExperimentID = 0
        for file in fileNames:
            if file[-4:] == '.nev':
                nev_file = NevFile(file)
                ExperimentData = nev_file.getdata()
                self.__nevdata2dict(ExperimentData,ExperimentID)
                ExperimentID += 1
            elif file[-4:] == '.npy':
                self.__python_dict(file)
    
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
        ini = np.zeros((6,))
        end = np.zeros((6,))
        return np.hstack((ini,waveform,end))

        

    
