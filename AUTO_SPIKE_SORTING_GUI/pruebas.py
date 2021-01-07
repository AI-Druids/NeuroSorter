# -*- coding: utf-8 -*-
"""
@author: %(Mikel Val Calvo)s
@email: %(mikel1982mail@gmail.com)
@institution: %(Dpto. de Inteligencia Artificial, Universidad Nacional de Educación a Distancia (UNED))
@DOI: 
"""
import numpy as np

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


from CLEANER.cleaner import spike_denoiser

spk = spike_denoiser()
#%%

file = './prueba.npy'
spike_dict = __python_dict(file)

print(np.unique(spike_dict['ChannelID']))
#%%
plt.close('all')
for channel in np.unique(spike_dict['ChannelID']):
    data = np.array([wave for idx, wave in enumerate(spike_dict['Waveforms']) if spike_dict['ChannelID'][idx] == 8])
    print(data.shape)
    
    scores = spk.run(data)
    
    import matplotlib.pyplot as plt
    
    plt.figure()
    for it, score in enumerate(scores):
        if score == 0:
            plt.plot(data[it], 'm')
        else:
            plt.plot(data[it], 'c')
