from pizza.src.log import log
import matplotlib.pyplot as plt
import glob
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
def pressure():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    files = glob.glob("lammps/T*D0.01")

    p = []
    t = []
    for filename in files:
        lg = log(filename)
        press, temp =lg.get("Press", "Temp")
        p.append(np.average(press))
        t.append(temp[0])

    ax.plot(t, p)
    ax.set_xlabel("Temperature [T/T0]")
    ax.set_ylabel("Pressure []")
    fig.savefig("img/PressureTemperature.png")
    plt.show()

def pressure_and_temperature():
    fig = plt.figure()
    ax = fig.gca(projection="3d")
    files = glob.glob("lammps/T*D*")

    p = []
    t = []
    d = []
    for filename in files:
        lg = log(filename)
        press, temp, dens =lg.get("Press", "Temp", "Density")
        p.append(np.average(press[500:]))
        t.append(np.average(temp[500:]))
        d.append(np.average(dens[500:]))
    
  
    surf = ax.plot_trisurf(d, t, p, cmap=cm.coolwarm)
    fig.savefig('img/TemperaturePressureDensity.png')
    plt.show()

if __name__ == "__main__":
    pressure()
    pressure_and_temperature()
