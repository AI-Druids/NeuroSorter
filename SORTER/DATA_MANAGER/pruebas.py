#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: %(Mikel Val Calvo)s
@email: %(mikel1982mail@gmail.com)
@institution: %(Dpto. de Inteligencia Artificial, Universidad Nacional de Educación a Distancia (UNED))
"""
#%%
from IO.brpylib import NevFile
import numpy as np

class nev_manager:   
     
    def load_nev(self, fileNames):
        print(fileNames)
        ExperimentID = 0
        for file in fileNames:
            nev_file = NevFile(file)
            experimentData = nev_file.getdata()
            self.__data2dict(experimentData,ExperimentID)
            ExperimentID += 1
    
    def save(self, path):
        np.save(path,self.spike_dict)
        
    def __data2dict(self, experimentData,ExperimentID):
        for channel in range(len(experimentData['spike_events']['ChannelID'])):
            for event in range(len(experimentData['spike_events']['TimeStamps'][channel])):
                self.spike_dict['ExperimentID'].append( ExperimentID )
                self.spike_dict['ChannelID'].append( experimentData['spike_events']['ChannelID'][channel] )
                self.spike_dict['UnitID'].append( 0 )
                self.spike_dict['OldID'].append( 0 )           
                self.spike_dict['TimeStamps'].append( experimentData['spike_events']['TimeStamps'][channel][event] )
                self.spike_dict['Waveforms'].append( experimentData['spike_events']['Waveforms'][channel][event] )           
                self.spike_dict['curves'].append( None )      
    
class data_manager(nev_manager):
    
    def __init__(self):
        nev_manager.__init__(self)
        self.current ={'channelID':None,'unitID':None,'plotted':[]}
        self.spike_dict = {'ExperimentID':[],'ChannelID':[],'UnitID':[],'OldID':[],'TimeStamps':[],'Waveforms':[],'curves':[]}
        


dmg = data_manager()
dmg.load_nev(['./data/barra_v_thresholding_30012.nev','./data/barra_v_thresholding_30012.nev'])    

len(dmg.spike_dict['Waveforms'])














