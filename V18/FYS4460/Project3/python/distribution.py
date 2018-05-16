import matplotlib.pyplot as plt
import numpy as np

z = np.random.rand(10**6)**(-3 + 1)
l = len(z)
logamax = np.ceil(np.log(np.max(z)))
binexponents= np.arange(logamax)
bins = 0.6**(-binexponents)
hist, bin_edges = np.histogram(z, bins = bins)
ds = np.diff(bins)
print(bins[:-1].shape, bins[1:].shape) 
sl = (bins[:-1] + bins[1:])*0.5
# nsl = hist[:-1]
nsl = hist/(l*ds)
fig = plt.figure()
fig.add_subplot(311).loglog(sl, nsl, 'ok')
fig.add_subplot(312).plot(sl, nsl)
fig.add_subplot(313).plot(nsl)
# plt.loglog(sl,nsl, 'ok')
# plt.loglog(bins, ns1[:-1])
plt.show()
# sorted_data = np.sort(z)[::-1]

# yvals=np.arange(len(sorted_data))/float(len(sorted_data)-1)

# plt.plot(sorted_data,yvals)

# plt.show()
# exit()
# # y = z/int(np.max(z))
# # print( np.max(z), np.max(z, axis = 1),np.max(z, axis = 0), max(z))
# # exit()
# CS = np.cumsum(z)
# fig = plt.figure()
# # ax = fig.add_subplot(112)
# fig.add_subplot(211).hist(z)
# fig.add_subplot(212).plot(z,CS, '-o')
# plt.show()
