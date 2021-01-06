# -*- coding: utf-8 -*-
"""
@authors: %(Val-Calvo, Mikel and Alegre-Cortés, Javier)
@emails: %(mikel1982mail@gmail.com, jalegre@umh.es)
@institutions: %(Dpto. de Inteligencia Artificial, Universidad Nacional de Educación a Distancia (UNED), Postdoctoral Researcher Instituto de Neurociencias UMH-CSIC)
"""
#%%

import QTDesigner.sorter_mpl as ui
from PyQt5.QtWidgets import QMainWindow

class GUI(QMainWindow):#

    def __init__(self):
        QMainWindow.__init__(self, parent=None)
        self.ui = ui()
#%%

