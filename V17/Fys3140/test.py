from pylab import *
import matplotlib.pyplot  as pyplot
f = [20, 200, 2000, 5000, 10000, 15000, 20000]
Vmax = [3.36, 4.28, 4.04, 3.24, 2.20, 1.56, 1.22]
Vmid  =[1.64, 2.02, 2.00, 1.88, 1.60, 1.30, 1.07]
V = 20e-3
#dBmax = [10*log10(((Vi-V)**2/1)/(V**2/1)) for Vi in Vmax]
dBmid = [20*log10(Vj/V) for Vj in Vmid]
dBmax = [20*log10(Vi/V) for Vi in Vmax]


fig = pyplot.figure(1)
ax = fig.add_subplot(1,1,1)
plot(f, dBmax, "-o")
ax.set_xscale('log')
title("Maximum Gain")
xlabel("Hz")
ylabel("dB")

fig = pyplot.figure(2)
ax = fig.add_subplot(1,1,1)
plot(f, dBmid, "-o")
ax.set_xscale('log')
title("Half maximum gain")
xlabel("Hz")
ylabel("dB")
show()

#plot(log10(f), dBmax)
#show()
#print zip(dBmax, dBmid)
