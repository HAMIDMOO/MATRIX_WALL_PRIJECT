import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors 

n= int(input("Enter the N: "))

N = np.empty((n, n)) ; N.fill(0)

for i in range(0, n):
    for j in range(0, n):
        N[i][j]= random.randint(0, 1)
        

cmap = mcolors.ListedColormap(['#95D2B3'])      
plt.imshow(N, cmap= cmap)    

for i in range (n):
    for j in range (n):
            plt.text(j,i, str(int(N[i,j])), va='center', ha='center', color='black' )


plt.show()



