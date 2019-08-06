import pickle
import matplotlib.pyplot as plt
import numpy as np

myList = []

with open('with_dropouts_weights.pkl' , 'rb') as handler:
    myList = pickle.load(handler)
    plt.yscale('log')    
    plt.ylim(0,100000)
    plt.xlim(-13,13)
    with open('no_dropouts_weights.pkl' , 'rb') as handler2:
     myList2 = pickle.load(handler2)
     plt.hist(myList, bins=100 , label='No Targeted Dropout' , range=(-10,10) , alpha = 0.5)
     plt.hist(myList2 , bins=100 , label='With Targeted Dropout' ,range=(-10,10), alpha = 0.5)
     plt.legend(loc='upper right')
     plt.show()
