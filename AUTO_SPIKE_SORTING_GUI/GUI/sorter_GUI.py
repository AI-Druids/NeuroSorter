# -*- coding: utf-8 -*-
"""
@authors: %(Val-Calvo, Mikel and Alegre-Cortés, Javier)
@emails: %(mikel1982mail@gmail.com, jalegre@umh.es)
@institutions: %(Dpto. de Inteligencia Artificial, Universidad Nacional de Educación a Distancia (UNED), Postdoctoral Researcher Instituto de Neurociencias UMH-CSIC)
"""
#%%
from DYNAMIC.dynamic import dynamic 
from QTDesigner.sorter_mpl import  Ui_MainWindows as ui
from LOG.log import log
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QShortcut
from PyQt5.QtGui import QKeySequence
import numpy as np


class GUI(QMainWindow, ui):
    def __init__(self, dmg, parent=None):
        QMainWindow.__init__(self, parent=parent) 
        self.dmg = dmg
        ### BIOSIGNALS gui design ##############################
        self.setupUi(self)
        self.MplWidget.emitter.connect(self.manage_selection)
        self.show()
        ###### dynamic auxiliar scripts ########################
        self.dyn = dynamic(self.dmg, self.listWidget_3, self.RawCode)
        self.dyn.load_auxiliar_code()
        ######### init logger ####################
        self.log = log(self.logger) 
        ######### callbacks ####################
        self.channel_comboBox.activated.connect(lambda:  self.toChannelID(self.channel_comboBox.currentText()))
        self.unit_comboBox.activated.connect(lambda:  self.toUnitID(self.unit_comboBox.currentText()))
        self.U2ID_comboBox.activated.connect(lambda:  self.selected_unit2ID(self.U2ID_comboBox.currentText()))
        self.delete_btn.clicked.connect(lambda:  self.delete())
        self.undo_btn.clicked.connect(lambda:  self.undo())
        self.clean_btn.clicked.connect(lambda:  self.spikes_clean())
        self.sorting_btn.clicked.connect(lambda:  self.sorting())
        
        self.btn_load.clicked.connect(self.openFileNameDialog)
        self.btn_save.clicked.connect(self.saveFileDialog)
        
        self.btn_run.clicked.connect(lambda:  self.dyn.load_module(self.listWidget_3.currentItem().text()))
        self.btn_save_changes.clicked.connect(self.dyn.save_script)
        ###########      
        self.global_shortcuts = self._define_global_shortcuts()
        
        
    def _define_global_shortcuts(self):
        shortcuts = []
        sequence = {
            'Ctrl+Up': lambda:  self.toChannelID('Up'),
            'Ctrl+Down': lambda:  self.toChannelID('Down'),
            'Shift+Up': lambda:  self.toUnitID('Up'),
            'Shift+Down': lambda:  self.toUnitID('Down'),
            'Alt+0': lambda:  self.selected_unit2ID(0),
            'Alt+1': lambda:  self.selected_unit2ID(1),
            'Alt+2': lambda:  self.selected_unit2ID(2),
            'Alt+3': lambda:  self.selected_unit2ID(3),
            'Alt+4': lambda:  self.selected_unit2ID(4),
            'Alt+5': lambda:  self.selected_unit2ID(5),
            'Alt+6': lambda:  self.selected_unit2ID(6),
            'Alt+7': lambda:  self.selected_unit2ID(7),
            'Alt+8': lambda:  self.selected_unit2ID(8),
            'Alt+9': lambda:  self.selected_unit2ID(9),
            'Ctrl+d': self.delete,
            'Ctrl+z': self.undo,
            'Ctrl+c': self.spikes_clean,
            'Ctrl+s': self.sorting,
        }
        for key, value in list(sequence.items()):
            s = QShortcut(QKeySequence(key),self, value)
#            s.setEnabled(False)
            shortcuts.append(s)
        return shortcuts
            
    def toChannelID(self, action):
        self.log.myprint('ACTION == toChannelID->' + str(action))
        if action == 'Up':
            index = self.channel_comboBox.currentIndex()
            if index < self.channel_comboBox.count()-1:                
                self.channel_comboBox.setCurrentIndex(index+1)
        elif action == 'Down':
            index = self.channel_comboBox.currentIndex()
            if index > 0:
                self.channel_comboBox.setCurrentIndex(index-1)
        elif action == 'None':
            self.channel_comboBox.setCurrentIndex(0)
        index = self.dmg.show_channelID( self.channel_comboBox.currentText() )
        self.update_view(index)
        self.update_unit_combobox(self.channel_comboBox.currentText())
        
    def toUnitID(self, action):
        self.log.myprint('ACTION == toUnitID->' + str(action))
        if action == 'Up':
            index = self.unit_comboBox.currentIndex()
            if index < self.unit_comboBox.count()-1: 
                self.unit_comboBox.setCurrentIndex(index+1)
        elif action == 'Down':
            index = self.unit_comboBox.currentIndex()
            if index > 0:
                self.unit_comboBox.setCurrentIndex(index-1)
        elif action == 'None':
            self.unit_comboBox.setCurrentIndex(0)
        index = self.dmg.show_unitID( self.unit_comboBox.currentText() )
        self.update_view(index)
        
    def selected_unit2ID(self, unit):
        self.log.myprint('ACTION == selected_unit2ID->' + str(unit))
        if unit == 'Noise':
            self.U2ID_comboBox.setCurrentIndex(0)
        else:
            self.U2ID_comboBox.setCurrentIndex(unit) 
        index = self.dmg.selected_unit2ID( self.U2ID_comboBox.currentText() )
        
        # if unit == 'Noise':
        #     self.U2ID_comboBox.setCurrentIndex(0)
        # else:
        #     self.U2ID_comboBox.setCurrentIndex(unit) 
        self.update_unit_combobox(self.channel_comboBox.currentText())
        self.update_view(index)
        
    def delete(self):
        self.log.myprint('ACTION == Delete')
        index = self.dmg.delete()
        self.update_view(index)
        
    def undo(self):
        self.log.myprint('ACTION == Undo')
        index = self.dmg.undo()
        self.unit_comboBox.setCurrentIndex(0)
        self.update_unit_combobox(self.channel_comboBox.currentText())
        self.update_view(index)
        
    def spikes_clean(self):
        self.log.myprint('ACTION == spikes denoising')
        index = self.dmg.clean()
        self.unit_comboBox.setCurrentIndex(0)
        self.update_unit_combobox(self.channel_comboBox.currentText())
        self.update_view(index)
        
    def sorting(self):
        self.log.myprint('ACTION == spikes sorting')
        index = self.dmg.sort()
        self.unit_comboBox.setCurrentIndex(-2)
        self.update_unit_combobox(self.channel_comboBox.currentText())
        self.update_view(index)
        
    def update_view(self, index):
        self.log.myprint( 'channelID: ' + str(self.dmg.current['channelID']) + '-> unitID: ' + str(self.dmg.current['unitID']) )
        self.manage_plotting(index)
        self.manage_average_plotting(self.dmg.current['channelID'])

    def manage_plotting(self, index):
        if len(index) > 0:
            waveforms = np.asarray(self.dmg.spike_dict['Waveforms'])[index]
            units = np.unique(np.asarray(self.dmg.spike_dict['UnitID'])[index])
            self.MplWidget.clear_plot()
            numUnits = []
            for unit in units:
                subindex = np.asarray(self.dmg.spike_dict['UnitID'])[index] == unit
                waveforms_unit = waveforms[subindex,:]
                numUnits.append(len(waveforms_unit))
                self.MplWidget.plot(waveforms_unit,unit)
            self.MplWidget.plot_legend(units, numUnits)
                
    def manage_average_plotting(self, channelID):
        num = len(self.dmg.spike_dict['ChannelID'])
        index = [i for i in range(num)  if (self.dmg.spike_dict['ChannelID'][i] == channelID and self.dmg.spike_dict['UnitID'][i] != -1)]
        waveforms = np.asarray(self.dmg.spike_dict['Waveforms'])[index]
        units = np.unique(np.asarray(self.dmg.spike_dict['UnitID'])[index])
        self.MplWidget.clear_plot_units()
        for unit in units:
            subindex = np.asarray(self.dmg.spike_dict['UnitID'])[index] == unit
            waveforms_unit = waveforms[subindex,:]
            self.MplWidget.plot_units(waveforms_unit,unit)
        #self.MplWidget.units_legend(units)
            
        
    def manage_selection(self):
        x1 = self.MplWidget.regions['x1']
        y1 = self.MplWidget.regions['y1']
        x2 = self.MplWidget.regions['x2']
        y2 = self.MplWidget.regions['y2']
        x = np.arange(60)
        x_range = [i for i in range(60) if np.logical_and(x > x1, x < x2)[i]]
        
        if self.dmg.current['plotted']:
            plotted = np.asarray( self.dmg.current['plotted'] )
            waveforms = np.asarray(self.dmg.spike_dict['Waveforms'])[plotted]
            
            self.manage_plotting(self.dmg.current['plotted'])
            
            self.dmg.current['selected'] = []
            
            for index in plotted:
                waveform = self.dmg.spike_dict['Waveforms'][index]
                if np.sum( np.logical_and(waveform[x_range] > y1, waveform[x_range] < y2) ) > 0:
                    self.dmg.current['selected'].append(index)
            
            if self.dmg.current['selected']:
                selected = np.asarray(self.dmg.current['selected'])
                waveforms = np.asarray(self.dmg.spike_dict['Waveforms'])[selected]
                self.MplWidget.plot(waveforms,0)
            
        
    def update_channel_combobox(self):
        self.channel_comboBox.clear() 
        channels = np.unique(self.dmg.spike_dict['ChannelID'])
        for channel in channels:
            self.channel_comboBox.addItem(str(channel))
        self.channel_comboBox.setCurrentIndex(0)
        self.dmg.current['channelID'] = int(self.channel_comboBox.currentText())
            
    def update_unit_combobox(self, channelID):
        num = len(self.dmg.spike_dict['ChannelID'])
        units = np.unique([self.dmg.spike_dict['UnitID'][i] for i in range(num)  if (self.dmg.spike_dict['ChannelID'][i] == int(channelID) and self.dmg.spike_dict['UnitID'][i] != -1)])
        self.unit_comboBox.clear() 
        for unit in units:
            self.unit_comboBox.addItem(str(unit))
        self.unit_comboBox.addItem('All')
        self.unit_comboBox.addItem('Noise')
        
        print('que tenemos en unit combobox currrent text ', self.unit_comboBox.currentText())
        if self.unit_comboBox.currentText() != 'All' and self.unit_comboBox.currentText() != 'Noise':
            self.dmg.current['unitID'] = int(self.unit_comboBox.currentText())
        else:
            self.dmg.current['unitID'] = 0
        
    def update_U2ID_combobox(self):
        units = ['Noise',1,2,3,4,5,6,7,8,9]
        for unit in units:
            self.U2ID_comboBox.addItem(str(unit))
            
        self.U2ID_comboBox.setCurrentIndex(0)

    def openFileNameDialog(self, btn):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        fileTypes = "Python (*.npy);;NEV (*.nev)"
        fileNames, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileName()","",fileTypes, options=options)    
        #----------------- load data -----#
        for file in fileNames:
            self.log.myprint_in(file)
            
        try:
            self.dmg.load(fileNames)
            self.log.myprint_out('Loading completed.')
        except:
            self.log.myprint_error('Cannot load selected file.')
        self.update_channel_combobox()
        self.update_unit_combobox(self.channel_comboBox.currentText())
        self.update_U2ID_combobox()
        #####################################################
        
    def saveFileDialog(self):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, filetype = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","(*.npy)", options=options)

        #----------------- Save data -----#
        self.dmg.save(fileName)
        ###################################  

