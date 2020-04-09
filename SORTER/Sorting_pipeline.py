# -*- coding: utf-8 -*-
"""
@authors: %(Val-Calvo, Mikel and Alegre-Cortés, Javier)
@emails: %(mikel1982mail@gmail.com, jalegre@umh.es)
@institutions: %(Dpto. de Inteligencia Artificial, Universidad Nacional de Educación a Distancia (UNED), Postdoctoral Researcher Instituto de Neurociencias UMH-CSIC)
"""
#%%

import core_functions_spike_sorter as yeah_mama

nev_file, data = yeah_mama.load_data('D:/Spike Sorter Project/barra_v_thresholding_30012.nev')

scores, spikes = yeah_mama.clean_spikes(data)

IDX = yeah_mama.sort_spikes(spikes)