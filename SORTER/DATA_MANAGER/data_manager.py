# -*- coding: utf-8 -*-
"""
@authors: %(Val-Calvo, Mikel and Alegre-Cortés, Javier)
@emails: %(mikel1982mail@gmail.com, jalegre@umh.es)
@institutions: %(Dpto. de Inteligencia Artificial, Universidad Nacional de Educación a Distancia (UNED), Postdoctoral Researcher Instituto de Neurociencias UMH-CSIC)
"""
#%%
from DATA_MANAGER.file_IO import nev_manager 
import numpy as np

class data_manager(nev_manager):
    
    def __init__(self, spk, ae):
        nev_manager.__init__(self)
        
        self.spk = spk
        self.ae = ae
        
        self.current ={'channelID':None,'unitID':None,'plotted':[],'selected':[]}
        self.spike_dict = {'ExperimentID':[],'ChannelID':[],'UnitID':[],'OldID':[],'TimeStamps':[],'Waveforms':[]}
        
    def show_channelID(self, channelID):
        num = len(self.spike_dict['ChannelID'])
        self.current['channelID'] = int(channelID)
        self.current['plotted'] = [i for i in range(num)  if (self.spike_dict['ChannelID'][i] == int(channelID) and self.spike_dict['UnitID'][i] != -1)]
        return self.current['plotted']
        
        
    def show_unitID(self, unitID):
        num = len(self.spike_dict['ChannelID'])
        
        self.current['unitID'] = unitID
        if unitID == 'Noise':
            self.current['plotted'] = [i for i in range(num)  if (self.spike_dict['ChannelID'][i] == self.current['channelID'] and self.spike_dict['UnitID'][i] == -1)]

        elif unitID == 'All':
            self.current['plotted'] = [i for i in range(num)  if (self.spike_dict['ChannelID'][i] == self.current['channelID'] and self.spike_dict['UnitID'][i] != -1)]
        else:
            self.current['plotted'] = [i for i in range(num)  if (self.spike_dict['ChannelID'][i] == self.current['channelID'] and self.spike_dict['UnitID'][i] == int(self.current['unitID']))]
        
        
        return self.current['plotted']
        
    def delete(self):
        self.spike_dict['OldID'] = [None for _ in self.spike_dict['OldID']]
        
        for sel in self.current['selected']:
            self.spike_dict['OldID'][sel] = self.spike_dict['UnitID'][sel]
            self.spike_dict['UnitID'][sel] = -1
            self.current['plotted'].remove(sel)
            
        self.current['selected'] = []
        return self.current['plotted']
        
    def selected_unit2ID(self, unit2ID):   
        if unit2ID != 'All':
            if unit2ID == 'Noise':
                unit2ID = -1
            else:
                unit2ID = int(unit2ID)
                
            self.spike_dict['OldID'] = [None for _ in self.spike_dict['OldID']]
            
            for sel in self.current['selected']:
                if self.spike_dict['UnitID'][sel] != unit2ID:
                    self.spike_dict['OldID'][sel] = self.spike_dict['UnitID'][sel]
                    self.spike_dict['UnitID'][sel] = unit2ID
                    self.current['plotted'].remove(sel)
                    
            self.current['selected'] = []
            
            return self.current['plotted']
        else:
            return []
        
    def undo(self):
        num = len(self.spike_dict['ChannelID'])
        
        index = [i for i in range(num) if (self.spike_dict['OldID'][i] != None)]
        for sel in index:
            self.spike_dict['UnitID'][sel] = self.spike_dict['OldID'][sel]
            self.current['plotted'].append(sel)
            
        self.spike_dict['OldID'] = [None for _ in self.spike_dict['OldID']]
        
        return self.current['plotted']
    
    def clean(self):
        num = len(self.spike_dict['ChannelID'])
        index = np.asarray( [i for i in range(num) if (self.spike_dict['ChannelID'][i] > 0)] )
        
        waveforms = np.asarray(self.spike_dict['Waveforms'])[index]
        waveforms = np.expand_dims(waveforms,axis=-1)
        
        scores = self.spk.run(waveforms)
        
        spike_index = index[scores[:,0]==1]
        noise_index = index[scores[:,0]!=1]
        
        for i in range(len(spike_index)):
            self.spike_dict['UnitID'][spike_index[i]] = 1
            
        for i in range(len(noise_index)):
            self.spike_dict['UnitID'][noise_index[i]] = -1   
            
        return self.current['plotted']

    
    def sort(self):
        print('self.current unitID ', self.current['unitID'])
        if self.current['unitID'] != 'Noise' and self.current['unitID'] != 'All':     
            num = len(self.spike_dict['ChannelID'])
            channelID = self.current['channelID']
            unitID = self.current['unitID']
            index_channel = np.asarray( [i for i in range(num) if (self.spike_dict['ChannelID'][i] == int(channelID) and self.spike_dict['UnitID'][i] != -1)] )

            # reset old unit for undo action
            self.spike_dict['OldID'] = [None for _ in self.spike_dict['OldID']]
            for index in index_channel:
                self.spike_dict['OldID'][index] = self.spike_dict['UnitID'][index]
                
            # select the maximun unitID value for the current plotted channel
            index_ch = np.asarray( [i for i in range(num) if (self.spike_dict['ChannelID'][i] == int(channelID))] )
            max_unitID = np.asarray(self.spike_dict['UnitID'])[index_ch].max()+1
            
            # select the current plotted(channel, unit) waveforms index
            index_chunit = np.asarray( [i for i in range(num) if (self.spike_dict['ChannelID'][i] == int(channelID) and self.spike_dict['UnitID'][i] == int(unitID))] )
            # get the corresponding waveforms
            waveforms = np.asarray(self.spike_dict['Waveforms'])[index_chunit]
            waveforms = np.expand_dims(waveforms,axis=-1)
            # compute clustering
            UnitIDs = self.ae.sort_spikes(waveforms)
            print('units before: ', np.asarray(self.spike_dict['UnitID'])[index_ch])
            print('max_unitID ', max_unitID)
            print('UnitIDs ', np.unique(UnitIDs))
            
            # set new unitIDs for the selected units in the selected channel
            for index,global_index in enumerate(index_chunit):
                # first old ID is stored
                self.spike_dict['OldID'][global_index] = self.spike_dict['UnitID'][global_index]
                # second, the new ID is set
                self.spike_dict['UnitID'][global_index] = int(UnitIDs[index]) + max_unitID
                
            # now correct the unitIDs of all units in the channel, except Noise
            unitIDs_2correct = np.unique( np.asarray(self.spike_dict['UnitID'])[index_channel] )
            print('unitIDs_2correct ', unitIDs_2correct)
            final_unitIDs = np.arange(1,len(unitIDs_2correct)+1)
            print('final_unitIDs ', final_unitIDs)
            
            for index in index_channel:
                self.spike_dict['UnitID'][index] = list(unitIDs_2correct).index(self.spike_dict['UnitID'][index])+1
                
            # current unit set to all, current channel is mantained
            self.current['unitID'] = 'All'
            # plotted index is set to current channel
            self.current['plotted'] = list(index_channel)
            
            return self.current['plotted']
        else:
            return []
    
    
    
    
        