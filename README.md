# PySorter Basics

Note: This document covers the basic information to use PySorter Beta version

## 1 Dependencies

Numpy, Matplotlib, Tensorflow==2.0.0, PyQT5, sklearn 

All depencendies can be installed using
pip install requirements.txt

## 2 Overview

PySorter is a spike cleaner and sorter. It works at three levels: First, it normalizes the data and discard abnormal shapes to remove noise events using a CNN; this network can be trained with previously cleaned data do adapt it to the specific recording of each setup. Then, putative units are sorted using a combination of an autoencoder to reduce dimensionality and clustering using Gaussian Mixture Models. This second step can be repeated to subsequently split desired units. At last, all units are visualized for manual curation; in addition, different functions are provided to facilitate the data curation (acor, data visualization, ISI).

## 3 PySorter interface


PySorter uses an interactive interface to perform the spike sorting. In [fig:PySorter-Interface], the main elements of the interface are shown.

![PySorter Scheme](https://raw.githubusercontent.com/AI-Druids/PySorter/master/Images/scheme_PySorter.PNG?token=AKY2HR4ZK6P7IZXXJTEKAGS6R4YHC)

1) Loading button

2) Saving button

3) Index with all the channels in the recording

4) Index with all the units in the present channel

5) Indicates to which channel to send the selected events

6) Sends the selected events to the unit selected in 5 (equivalent to Alt+[number of units]) // Noise unit has assinged the Unit nº = 0

7) Undoes the last action (Does not stack)

8) Loads the CNN and uses it to clean all electrodes. The events considered as noise will be sent to the “noise” unit of each channel

9) Applies the sorting pipeline to the data displayed in the axis

10) Main scree

11) Color code of each units and number of events

12) Averga waveshape of each unit

13) Utilities

## 4 Hotkeys
**Ctrl+Up/Down** -> move across channels.

**Shift+Up/Down** -> move across units on each channel.

**Alt+[0,1,2,3,4,5,6,7,8,9]** -> sends selected spikes to the specified unit, 0 unit is used for noise.

**Ctrl+c** -> clean spikes from noise for all the loaded waveforms.

**Ctrl+s** -> Sorting of current visualized waveforms.

**Ctrl+d** -> Send selected waveforms to noise, equivalent to Alt+0.

**Ctrl+z** -> Undo, only available for the last modification.

## 5 Algorithms

### 5.1 Cleaning

Cleaning of non-spike events is performed with a CNN trained for such porpouse. This enables a faster spike sorting in those cases on which the signal-to-noise ratio is not good or small multiunits should be recovered. An additional script “train_cleaner_script” is provided to train your own CNN if you have already sorted data that can be representative of your recording setup. Events should be normalized beween [0 1] before using them for the training, as the CNN is designed to distinguish events based on their shape at this stage of the pipeline.

### 5.2 Sorting

In order to sort the units, their dimensionality is reduced using an autencoder and then they are clusterized using a GMM. The number of clusters is based stablished using information-theoretic criteria (BIC).

Clustering is performed on the events ploted in the axis (10). Recursive clustering and/or re-clustering can be performed if considered benefitial.

### 5.3 Utilities

Several functions are available to help in the sorting procedure in the “Scripts_Manager” tab. They operate using the events that are plotted in the main axis (10) when the script is executed. At this moment, ISI, autocorrelogram and temporal representation of the spikes are included. Source code can be edited in the right panel. Additional scripts with new analysis/visualization tools can be easily added including them in the folder “AUXILIAR_CODE”.
