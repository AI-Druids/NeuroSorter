# -*- coding: utf-8 -*-
"""
@authors: %(Val-Calvo, Mikel and Alegre-Cortés, Javier)
@emails: %(mikel1982mail@gmail.com, jalegre@umh.es)
@institutions: %(Dpto. de Inteligencia Artificial, Universidad Nacional de Educación a Distancia (UNED), Postdoctoral Researcher Instituto de Neurociencias UMH-CSIC)
"""
#%%

from tensorflow.keras.layers import Dense, Input, Conv1D, Flatten, Reshape
from tensorflow.keras.models import Model
from tensorflow.keras import callbacks
from sklearn import mixture
import numpy as np
    
class AutoEncoder_GM:
    def __init__(self):
        print('sorter')
        
    def sort_spikes(self, spikes):
        spikes = spikes[:,15:50]
        shape = np.shape(spikes)[1]
        print(shape)
        # normalize
        for i in range(np.shape(spikes)[0]):
            spikes[i,:] = spikes[i,:]-np.min(spikes[i,:])
            spikes[i,:] = spikes[i,:]/spikes[i,:].max()

        spikes = np.squeeze(spikes)
        inputs = Input(shape=(shape,)) 

                #   ---------------- DENSE AUTOENCODER JAVI -------------------
        # a layer instance is callable on a tensor, and returns a tensor
        x = Dense(6, activation='sigmoid')(inputs)
        predictions = Dense(shape, activation='sigmoid')(x)
        # This creates a model that includes
        # the Input layer and three Dense layers
        model = Model(inputs=inputs, outputs=predictions)
        model.compile(optimizer='nadam',loss='mse',metrics=['accuracy'])
        model_hidden = Model(inputs=inputs, outputs=x)
        call = callbacks.EarlyStopping(monitor='val_loss', min_delta=0, patience=5, verbose=0, mode='auto', baseline=None, restore_best_weights=True)
        model.fit(spikes, spikes, batch_size=64, epochs=250, verbose=1, callbacks=[call], validation_split=0.2)
        

        
        latent = model_hidden.predict(spikes)

        #%% clustering
        
        X = latent
        lowest_bic = np.infty
        bic = []
        n_components_range = range(1, 4)
        
        for n_components in n_components_range:
            # Fit a Gaussian mixture with EM
            gmm = mixture.GaussianMixture(n_components=n_components,covariance_type='diag')
            gmm.fit(X)
    #        bic.append(gmm.bic(X))
            bic = np.append(bic, gmm.bic(X))
            if bic[-1] < lowest_bic:
                lowest_bic = bic[-1]
                best_gmm = gmm
                
                bic = np.array(bic)
    
        clf = best_gmm
        
        unit_IDs = clf.predict(X)
    
        return unit_IDs