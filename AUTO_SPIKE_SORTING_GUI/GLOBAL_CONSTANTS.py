# -*- coding: utf-8 -*-
"""
@authors: %(Val-Calvo, Mikel and Alegre-Cortés, Javier)
@emails: %(mikel1982mail@gmail.com, jalegre@umh.es)
@institutions: %(Dpto. de Inteligencia Artificial, Universidad Nacional de Educación a Distancia (UNED), Postdoctoral Researcher Instituto de Neurociencias UMH-CSIC)
"""
#%%

''' GRAPHICAL INTERFACE ASPECT ''' 
APP_CSS_STYLE = "QTDesigner/style_dark_orange.css"

''' THE DEEP LEARNING MODEL WHICH MAKES THE INFERENCE BETWEEN NOISE AND SPIKE EVENTS '''
CLEANER_DEEPL_JSON = './CLEANER/model_4.json'
CLEANER_DEEPL_WEIGHTS = "./CLEANER/model_weights_4.h5"
CLEANER_DEEPL_H5_MODEL = "./CLEANER/checkmodel_javi_model1.h5"
CLEANER_MODEL_LOAD_METHOD = 'json_weights'
LOSS='categorical_crossentropy'
OPTIMIZER='Nadam'
BATCH_SIZE = 16

'''RANGE OF THE EVENT TO BE ANALYZED'''
SPIKES_RANGE = range(15,50)
SPIKES_EXPAND = 6