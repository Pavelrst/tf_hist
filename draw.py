import pickle
import matplotlib.pyplot as plt
import numpy as np

myList = []

with open('with_dropouts_weights.pkl' , 'rb') as handler:
    myList = pickle.load(handler)
with open('no_dropouts_weights.pkl' , 'rb') as handler2:
    myList2 = pickle.load(handler2)

# Count of parameters. It should be approximately the same value.
count1 = len(myList)
count2 = len(myList2)

# Calc the range of the plot
tmin = np.round(min((np.min(myList), np.min(myList2))))-1
tmax = np.round(max((np.max(myList), np.max(myList2))))+1

# Calc the statistics of the data
std1 = np.round(np.std(myList), 7)
std2 = np.round(np.std(myList2), 7)
min1 = np.round(np.min(myList), 2)
max1 = np.round(np.max(myList), 2)
min2 = np.round(np.min(myList2), 2)
max2 = np.round(np.max(myList2), 2)

num_of_bins = 10000

label1 = 'No TD, std=' + str(std1) + " range=[" + str(min1) + "," + str(max1) + "]"
label2 = 'With TD, std=' + str(std2) + " range=[" + str(min2) + "," + str(max2) + "]"
plt.hist(myList, bins=num_of_bins, label=label1, range=(tmin, tmax) , alpha=0.5)
plt.hist(myList2 , bins=num_of_bins, label=label2, range=(tmin, tmax), alpha=0.5)
plt.legend(bbox_to_anchor=(1, 1))
plt.yscale('log')
plt.xlim(tmin, tmax)
plt.show()
