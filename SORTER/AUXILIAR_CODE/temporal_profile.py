# -*- coding: utf-8 -*-
"""
@author: %(Mikel Val Calvo)s
@email: %(mikel1982mail@gmail.com)
@institution: %(Dpto. de Inteligencia Artificial, Universidad Nacional de Educación a Distancia (UNED))
"""
#%%
import numpy as np 
import matplotlib.pyplot as plt
import numpy as np
def run(spike_dict, current):

    print('ya esta listo')
    print('vamooos')
    index = current['plotted']
    time_stamps = np.empty((1,len(index)))
    wave_forms = np.empty((60,len(index)))
    units = np.empty((1,len(index)))
    for j in range(0,len(index)):
        time_stamps[0,j] = (spike_dict["TimeStamps"][index[j]])/20 #TimeStamp of each spike is obtained 
        wave_forms[:,j] = (spike_dict["Waveforms"][index[j]]) #Waveform of each spike is obtained
        units[0,j] = spike_dict["UnitID"][index[j]]
    #%% Plotting

    colours = plt.get_cmap('Set1')    
    #Create a variable with the colours of interest
    plt.figure() #Create a figure
    plt.xlabel('Time (ms)')
    plt.ylabel('uV')
    for j in np.unique(units):
        trans = np.where(units==j) 
#Select the spikes in each unit
        trans = trans[1]
        print(colours(j))
        print(j)
        color = colours(int(j))
        for i in trans:
            k = np.round(time_stamps[0,i]) #Round the time stamps
            k = int(k)
            time_position = np.arange(k, k+60) #Give space to the spike
            
            plt.plot(time_position, wave_forms[:,i], color=color) 
                
