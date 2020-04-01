# -*- coding: utf-8 -*-
"""
@author: %(Mikel Val Calvo)s
@email: %(mikel1982mail@gmail.com)
@institution: %(Dpto. de Inteligencia Artificial, Universidad Nacional de Educación a Distancia (UNED))
"""
import numpy as np 
import matplotlib.pyplot as plt


def run(spike_dict, current):
    max_ISIvalue=200
    ISI_bins = 30    
    #%%%%%%
    index = current['plotted']
    print(np.shape(index))
    time_stamps = np.empty((1,len(index)))
    for j in range(0,len(index)):
        time_stamps[0,j] = (spike_dict["TimeStamps"][index[j]])/20 #TimeStamp of each spike is obtained 
    time_stamps = time_stamps[0]    
    ISI = []
    for k in range(0,len(time_stamps)-1): #Goes through all spikes
        ISI.append(time_stamps[k+1]-time_stamps[k]) #Computed delay between two spikes
    ISI = np.array(ISI)
    print(np.shape(ISI)) 
    plt.figure() 
    print('ok')       
    plt.hist(ISI[ISI<max_ISIvalue], bins = ISI_bins)
    plt.xlabel('Time (ms)')
    plt.ylabel('Spike count ' + str(len(np.squeeze(time_stamps))))
        

        
    

        
        



