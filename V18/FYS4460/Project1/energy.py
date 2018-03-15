from ovito.io import import_file
from ovito.modifiers import PythonScriptModifier
from ovito.data import ParticleProperty
from ovito import dataset
import matplotlib.pylab as plt
import glob
import re
import numpy as np

def import_dump(filetype):
    return glob.glob(filetype)
    
def find_energies(filetype):
    node = import_file(filetype)
    potentialenergy = []
    kineticenergy = []
    totalenergy = []

    for frame in range(dataset.anim.first_frame, dataset.anim.last_frame + 1, 1):
        num_particles = node.output.number_of_particles
        pe = sum(node.compute(frame).particle_properties["c_peatom"])/num_particles 
        ke = sum(node.compute(frame).particle_properties["c_keatom"])/num_particles 
        tot = ke + pe
        potentialenergy.append(pe)
        kineticenergy.append(ke)
        totalenergy.append(tot)

    return potentialenergy, kineticenergy, totalenergy, num_particles 


def plot_energies(filetype = "lammps/energy/*.lammpstrj"):
    fig  = plt.figure()
    ax = fig.add_subplot(1,1,1)
    dumpfiles = import_dump(filetype)
    for filename in dumpfiles:
        timestep = re.findall("\d+", filename)
        potentalenergy, kineticenergy, totalenergy, num_particles =  find_energies(filename) 
        ax.plot(totalenergy, label="Timestep: {}".format(str(timestep)))
        #ax.plot(kineticenergy) # label="Timestep: 0.{}".format(timestep[0])
        #ax.plot(potentialenergy, label="Timestep: 0.{}".format(timestep[0]))
    plt.xlabel("Time")   
    plt.ylabel("Total Energy [Lj]")
    plt.legend()

    plt.show()
def find_temperature(filetype):
    potentalenergy, kineticenergy, totalenergy, num_particles  =  find_energies(filetype) 
    temperature = 2./3*np.array(kineticenergy)[:]
    avg_temp = sum(temperature[200:])/len(temperature[200:]) #average temp after equilibration
    fig  = plt.figure()
    ax = fig.add_subplot(311)
    bx = fig.add_subplot(3, 1, 2)
    cx = fig.add_subplot(3, 1, 3)
    ax.plot(temperature/avg_temp)
    bx.plot(temperature)
    cx.plot(temperature / temperature[0])
    plt.show()
   
if __name__ == "__main__":
    #plot_energies()
    find_temperature("lammps/dumptest.lammpstrj")



