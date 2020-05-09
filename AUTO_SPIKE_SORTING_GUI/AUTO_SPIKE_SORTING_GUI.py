# -*- coding: utf-8 -*-
"""
@authors: %(Val-Calvo, Mikel and Alegre-Cortés, Javier)
@emails: %(mikel1982mail@gmail.com, jalegre@umh.es)
@institutions: %(Dpto. de Inteligencia Artificial, Universidad Nacional de Educación a Distancia (UNED), Postdoctoral Researcher Instituto de Neurociencias UMH-CSIC)
"""
#%%
from GLOBAL_CONSTANTS import APP_CSS_STYLE
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
        with open(APP_CSS_STYLE) as f:
            self.setStyleSheet(f.read())
        
    def execute_gui(self):
        ret = self.exec_()
        sys.exit(ret)
       
if __name__ == "__main__":
    main = MyApp()
    main.execute_gui()
