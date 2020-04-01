# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 16:36:29 2019

@author: Javie
"""

import core_functions_spike_sorter as yeah_mama

nev_file, data = yeah_mama.load_data('D:/Spike Sorter Project/barra_v_thresholding_30012.nev')

scores, spikes = yeah_mama.clean_spikes(data)

IDX = yeah_mama.sort_spikes(spikes)