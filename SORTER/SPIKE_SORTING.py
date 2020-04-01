# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 14:02:49 2018

@author: LENOVO
"""
#%%
from GUI.sorter_GUI import GUI 
from DATA_MANAGER.data_manager import data_manager
from CLEANER.cleaner import spike_denoiser
from SORTER.sorter import AutoEncoder_GM
from PyQt5.QtWidgets import QApplication

import sys

class MyApp(QApplication):
    def __init__(self):
        QApplication.__init__(self,[''])
        ################# init GUI ################################
        self.spk = spike_denoiser()
        self.ae = AutoEncoder_GM()
        self.dmg = data_manager(self.spk, self.ae)
        self.gui = GUI(self.dmg)       
        #-------------------
        self.loadStyle()     

    def loadStyle(self):
        #Aplicamos CSS
        with open("QTDesigner/style_dark_orange.css") as f:
            self.setStyleSheet(f.read())
        
    def execute_gui(self):
        ret = self.exec_()
        sys.exit(ret)
         
main = MyApp()
sys.exit(main.execute_gui())