# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 16:19:09 2019

@author: Javie
"""

def load_data(filename):

    from brpylib import NevFile
    import numpy as np
    datafile = filename  
    nev_file = NevFile(datafile)
    cont_data = nev_file.getdata()
    a = cont_data['spike_events']
    b =a['Waveforms']
    b2 = np.vstack(b)
    
    
    ini = np.zeros((b2.shape[0],10))
    for i in range(10):
        ini[:,i] = b2[:,0]
    
    finish = np.zeros((b2.shape[0],2))
    for i in range(2):
        finish[:,i] = b2[:,47]
    
    
    b3 = np.hstack((ini,b2,finish))
    
    
    data = b3

    data = np.expand_dims(data,axis=-1)

    return nev_file, data


def clean_spikes(data):
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.utils import plot_model
    from tensorflow.keras.models import model_from_json
    from tensorflow.keras import regularizers
    from tensorflow.keras import optimizers
    from scipy import signal
    json_file = open('D:/Spike Sorter Project/model_2.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("D:/Spike Sorter Project/model_weights_2.h5")
    print("Loaded model from disk")
    
    ## compilar el model
    loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    # evaluar el model
    scores = loaded_model.predict_proba(data, batch_size=16)
    spikes = data[scores[:,0]==1,:]
        
    return scores, spikes    
    
    
    


def sort_spikes(spikes):
    
    import keras
    from tensorflow.keras.layers import Activation, Dense, Input
    from tensorflow.keras.models import Model
    from tensorflow.keras import backend as K
    import itertools
    from sklearn import mixture
    import numpy as np
    

    for i in range(np.shape(spikes)[0]):
        spikes[i,:] = spikes[i,:]-np.min(spikes[i,:])
        spikes[i,:] = spikes[i,:]/spikes[i,:].max()
        
    
    
    spikes = np.squeeze(spikes)
    # This returns a tensor
    inputs = Input(shape=(60,))
    # a layer instance is callable on a tensor, and returns a tensor
    #x = Dense(784, activation='sigmoid')(inputs)
    
    x = Dense(6, activation='sigmoid')(inputs)
    predictions = Dense(60, activation='sigmoid')(x)
    
    # This creates a model that includes
    # the Input layer and three Dense layers
    model = Model(inputs=inputs, outputs=predictions)
    model.compile(optimizer='nadam',
                  loss='mse',
                  metrics=['accuracy'])
    


    model_hidden = Model(inputs=inputs, outputs=x)
    
    model_hidden.summary()
    
 
    latent = model_hidden.predict(spikes)
    
    
    
    X = latent
    lowest_bic = np.infty
    bic = []
    n_components_range = range(1, 7)
    
    for n_components in n_components_range:
        # Fit a Gaussian mixture with EM
        gmm = mixture.GaussianMixture(n_components=n_components,
                                  covariance_type='diag')
        gmm.fit(X)
#        bic.append(gmm.bic(X))
        bic = np.append(bic, gmm.bic(X))
        if bic[-1] < lowest_bic:
            lowest_bic = bic[-1]
            best_gmm = gmm
            
            bic = np.array(bic)

    clf = best_gmm
    
    IDX = clf.predict(X)

    return IDX, clf, latent
