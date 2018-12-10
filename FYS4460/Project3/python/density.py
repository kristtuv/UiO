import numpy as np
import matplotlib as mpl
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from scipy.ndimage.measurements import label
from skimage.color import label2rgb
from skimage.measure import regionprops
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square

################################
L = 150 #Length of sides 
prob = np.linspace(0.4, 1.0, 150) #Prbability
p_len = len(prob)
Ni = np.zeros(p_len)
Mi = np.zeros(p_len)
N = 15 # Number of random L-matrices in loop
################################

def density(plot = False):
    for i in range(N):
        z = np.random.rand(L,L)
        for p in range(p_len):
            m = z < prob[p]
            lw = label(m, 4)
            bbox = np.asarray([region.bbox for region in regionprops(lw)])
            area = np.asarray([region.area for region in regionprops(lw)])
            jx = np.where(np.abs(bbox[:, 3] - bbox[:, 1]) == L)[0]
            jy = np.where(np.abs(bbox[:, 2] - bbox[:, 0]) == L)[0]
            union =  list(set(jx).union(jy))
            if union:
                Ni[p] += 1
                Mi[p] += np.sum(area[union])          
    Pi = Ni/N
    P = Mi/(N*L*L)
    p_index = np.argwhere(prob>0.5975)[0][0] # Index where p > p_c
    P_large = P[p_index:] # p > p_c
    p_large = prob[p_index:] - 0.5975 # p > p_c
    P1 = np.sum(np.log(P_large))
    p1= np.sum(np.log(p_large ))
    
    P3= np.log(np.sum(P_large))
    p3= np.log(np.sum(p_large ))


    P2= np.log(P_large[-1]) - np.log(P_large[1])
    p2= np.log(p_large[ -1]) - np.log(p_large [1])
   
    P4= np.log(P_large[10]) - np.log(P_large[1])
    p4= np.log(p_large[ 10]) - np.log(p_large [1])
    b1 = P1/p1
    b2 = P2/p2
    b4 = P4/p4
    print(b1, b2, b4)

    if plot:
        fig = plt.figure()
        ax = fig.add_subplot(211)
        bx = fig.add_subplot(212)
        ax.plot(prob, Pi)
        bx.plot(prob, P)
        bx.plot(prob[p_index:], p_large**b1, label='b1')
        bx.plot(prob[p_index:], p_large**b2, label='b2')
        bx.plot(prob[p_index:], p_large**b4, label='b4')  
        plt.legend()
        plt.show()
if __name__ == '__main__':
    #find_beta()
    density(plot = True)

















# z = np.random.rand(L,L)
# m = z < p

# lw = label(m, 4)

# img = label2rgb(lw, bg_label = 0, colors=colors)
# fig, ax = plt.subplots(figsize=(10, 6))
# ax.imshow(img, extent=[0,20,20,0])
# for region in regionprops(lw):
#     minr, minc, maxr, maxc = region.bbox
#     print (region.bbox)
#     rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
#                               fill=False, edgecolor='red', linewidth=2)
#     ax.add_patch(rect)

# # ax.set_axis_off()
# plt.tight_layout()
# plt.show()
