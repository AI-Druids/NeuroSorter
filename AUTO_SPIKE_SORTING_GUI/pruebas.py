#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 17:56:59 2021

@author: mikel
"""

import numpy as np
from SORTER.sorter_umap import sorter_umap as sorter
import matplotlib.pyplot as plt
import similaritymeasures as sm
from scipy.stats import zscore

def __python_dict(file):
    spike_dict = {'ExperimentID':[],'ChannelID':[],'UnitID':[],'OldID':[],'TimeStamps':[],'Waveforms':[]}
    append_channelID = spike_dict['ChannelID'].append
    append_TimeStamps = spike_dict['TimeStamps'].append
    append_Waveforms = spike_dict['Waveforms'].append
    append_UnitID = spike_dict['UnitID'].append
    append_OldID= spike_dict['OldID'].append
    append_ExperimentID = spike_dict['ExperimentID'].append
    
    aux = np.load(file, allow_pickle=True)
    dictionary = aux.item()
    
    [append_channelID(ChannelID) for ChannelID in dictionary['ChannelID']]
    [append_TimeStamps(TimeStamp) for TimeStamp in dictionary['TimeStamps']]
    [append_Waveforms(Waveform) for Waveform in dictionary['Waveforms']]
    [append_UnitID(UnitID) for UnitID in dictionary['UnitID']]
    [append_OldID(OldID) for OldID in dictionary['OldID']]
    [append_ExperimentID(ExperimentID) for ExperimentID in dictionary['ExperimentID']]
    
    return spike_dict


def _detect_similarUnits(units, spikes):
    means = []
    for label in np.unique(units):
        positions = [idx for idx,unit in enumerate(units) if unit == label]
        means.append( spikes[positions].mean(axis=0) )

    if len(means) > 1:
        mylist = []
        my_index = list(range(len(means)))
        
        aux_means = means[1:]
        aux_myindex = my_index[1:]
        
        index = 0
        for _ in range(len(means)):
            main_mean = means[index]
            
            equal, distinct = [],[]
            for aux, idx in zip(aux_means,aux_myindex):
                print( 'distances ', sm.frechet_dist(main_mean, aux) )
                
                if sm.frechet_dist(main_mean, aux) < 10:
                    equal.append(idx)
                else:
                    distinct.append(idx)

            
            if equal:
                equal.append(index)
                mylist.append(equal)
            elif not equal and len(distinct) >= 1:
                mylist.append([my_index[index]])
            
            if not distinct:
                break
            elif len(distinct) == 1:
                mylist.append(distinct)
                break
            else:
                aux_means = [means[val] for val in distinct[1:]]
                aux_myindex = [my_index[val] for val in distinct[1:]]
                index = distinct[0]
                
        return mylist
    else:
        return []

def _merge_similarClusters(mylist, units, spikes):
    labels = np.unique(units)
    
    for idx, sublist in enumerate(mylist):
        for position in sublist:
            index = np.array([pos for pos,unit in enumerate(units) if unit == labels[position]])
            units[index] = (idx+1)*-1
    
    return abs(units)

#%%
plt.close('all')
ae = sorter()       
spike_dict = __python_dict('./prueba.npy')
spikes = np.array([spike for index, spike in enumerate(spike_dict['Waveforms']) if spike_dict['ChannelID'][index] == 24])


plt.figure()
for wave in spikes:
    plt.plot(wave, 'b')

units = ae.sort_spikes(spikes)
print(np.unique(units))

colors = ['r','m','c','b','y','g']
plt.figure()
for color, unit in zip(colors, np.unique(units)):
    index = np.array([idx for idx,_ in enumerate(spikes) if units[idx] == unit])
    mean = spikes[index].mean(axis=0)
    plt.plot(mean, color)


mylist = _detect_similarUnits(units, spikes)
if mylist:
    final_units = _merge_similarClusters(mylist, units, spikes)

    print(np.unique(final_units))
    
    plt.figure()
    for color, unit in zip(colors, np.unique(final_units)):
        index = np.array([idx for idx,wave in enumerate(spikes) if final_units[idx] == unit])
        mean = spikes[index].mean(axis=0)
        plt.plot(mean, color)
    
    
    



