import numpy as np
import matplotlib as mpl
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from scipy.ndimage import measurements
from skimage.color import label2rgb
from skimage.measure import regionprops
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
import time

M = 1000
L = 200
# probability = [0.45, 0.50, 0.54, 0.57, 0.58]
probability = [0.61, 0.60, 0.598, 0.596, 0.595]
problen = len(probability)
allarea = []

# start = time.clock()
for p in range(problen):
    print(p)
    allarea.append([]) #for evyer p, create a new list of areas
    # starlcc = time.clock()
    for i in range(M):
        z = np.random.rand(L, L)
        m = z < probability[p]
        lw = label(m, 4)


        # print( lw[lw > 0]) print(lw > 0)
        # print(lw)
        # (lw[:][0] > 053814095381409)
        #(lw[:][-1] > 0)
        # print(p)
        # print(lw[:][0][lw[:][0] > 0])
        # print(lw[:][-1][lw[:][-1] > 0])
        #  =.()
        cols = np.isin(lw[:,0][lw[:,0] > 0], lw[:,-1][lw[:,-1] > 0])
        rows = np.isin(lw[0,:][lw[0,:] > 0], lw[-1,:][lw[-1,:] > 0])
     

        if np.any(cols) or np.any(rows):
            
            continue
        else:
        
            Labels = np.arange(1, np.max(lw + 1))
  
            area = measurements.sum(m, lw,Labels) 


            allarea[p] = np.concatenate((allarea[p], area))     
  
a = 1.2
allarea = np.asarray(allarea)
logamax = np.ceil(np.log(np.max(np.concatenate(allarea)))/np.log(a))
binexponents = np.arange(logamax + 1)

bins = a**binexponents
hist = [np.histogram(allarea_row, bins = bins) for allarea_row in allarea]
hist, bin_edges = map(list, zip(*hist))



ds = np.diff(bins)
sl = (bins[:-1] + bins[1:])*0.5
nsl = hist/(M*L**2*ds)


for i in range(len(nsl)):

    plt.loglog(sl, nsl[i], label='p = {}'.format(probability[i]))

# print('starth: ', time.clock() - starth)
plt.legend()
plt.show()

