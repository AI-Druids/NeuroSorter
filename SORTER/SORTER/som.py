#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: %(Mikel Val Calvo)s
@email: %(mikel1982mail@gmail.com)
@institution: %(Dpto. de Inteligencia Artificial, Universidad Nacional de Educación a Distancia (UNED))
"""
#%%
import numpy as np

aux = np.load('./data/prueba.npy', allow_pickle=True)
data = aux.item()

#%%
index_ch19 = np.asarray([i for i in range(len(data['ChannelID'])) if ( data['ChannelID'][i] == 19 and data['UnitID'][i] != -1)])
labels_19 = np.asarray([data['UnitID'][i] for i in range(len(data['ChannelID'])) if ( data['ChannelID'][i] == 19 and data['UnitID'][i] != -1)])
print(index_ch19.shape)
print(labels_19.shape)
#%%
spikes = np.asarray([data['Waveforms'][i] for i in range(len(data['ChannelID']))])[index_ch19]
print(spikes.shape)
#%% AUTOENCODER
from keras.layers import Dense, Input, Conv1D, Flatten, Reshape
from keras.models import Model
from keras import callbacks
import numpy as np

spikes = spikes[:,10:45]
shape = np.shape(spikes)[1]
print(shape)
# normalize
for i in range(np.shape(spikes)[0]):
    spikes[i,:] = spikes[i,:]-np.min(spikes[i,:])
    spikes[i,:] = spikes[i,:]/spikes[i,:].max()

    
#if spikes.shape[-1] != 1:
#    spikes = np.expand_dims(spikes,axis = -1)

spikes = np.squeeze(spikes)
inputs = Input(shape =(spikes.shape[1],)) 

x = Dense(6, activation='sigmoid')(inputs)
predictions = Dense(shape, activation='sigmoid')(x)
model = Model(inputs=inputs, outputs=predictions)
model.compile(optimizer='nadam',loss='mse',metrics=['accuracy'])
call = callbacks.EarlyStopping(monitor='val_loss', min_delta=0, patience=5, verbose=0, mode='auto', baseline=None, restore_best_weights=True)
model.fit(spikes, spikes, batch_size=64, epochs=1000, verbose=1, callbacks=[call], validation_split=0.2)

model = Model(inputs=inputs, outputs=predictions)
model.summary()
   
model.compile(optimizer='nadam',loss='mse',metrics=['accuracy'])
model_hidden = Model(inputs=inputs, outputs=x)
call = callbacks.EarlyStopping(monitor='val_loss', min_delta=0, patience=5, verbose=0, mode='auto', baseline=None, restore_best_weights=True)
model.fit(spikes, spikes, batch_size=64, epochs=1000, verbose=1, callbacks=[call], validation_split=0.2)
   
latent = model_hidden.predict(spikes)     

#%%
from minisom import MiniSom
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale

data = scale(spikes)
num = labels_19 

som = MiniSom(10, 10, data.shape[1], sigma=4,
              learning_rate=0.5, neighborhood_function='triangle')
som.pca_weights_init(data)
print("Training...")
som.train_random(data, 5000, verbose=True) 
print("\n...ready!")


plt.figure(figsize=(8, 8))
wmap = {}
im = 0
for x, t in zip(data, num): 
    w = som.winner(x)
    wmap[w] = im
    plt.text(w[0]+.5,  w[1]+.5,  str(t),
              color=plt.cm.rainbow(t / 10.), fontdict={'weight': 'bold',  'size': 11})
    im = im + 1
plt.axis([0, som.get_weights().shape[0], 0,  som.get_weights().shape[1]])
plt.show()

#%% OUTLIERS DETECTION
outliers_percentage = 0.3
inliers = data.shape[0]
outliers = int(inliers * outliers_percentage)

som = MiniSom(2, 1, data.shape[1], sigma=1, learning_rate=0.5,
              neighborhood_function='triangle', random_seed=10)


som.train_batch(data, 100, verbose=True)  
    
quantization_errors = np.linalg.norm(som.quantization(data) - data, axis=1)
error_treshold = np.percentile(quantization_errors, 
                               100*(1-outliers_percentage)+5)
is_outlier = quantization_errors > error_treshold
    
plt.figure()
plt.hist(quantization_errors)
plt.axvline(error_treshold, color='k', linestyle='--')
plt.xlabel('error')
plt.ylabel('frequency')
    
plt.figure(figsize=(8, 8))
plt.scatter(data[~is_outlier, 0], data[~is_outlier, 1],
            label='inlier')
plt.scatter(data[is_outlier, 0], data[is_outlier, 1],
            label='outlier')
plt.legend()
plt.show()
    
    
    
    
    