import subprocess
import numpy as np
import os
import re
import fileinput
def run_lammps(filename):
    subprocess.call("lmp_mpi < " + filename, shell=True)

def delete_lammps(filename):
    try:
        os.remove(filename)
    except OSError:
       pass 

def sub_lammps_system_size(infile):
    for systemsize in systemsizes: 
        pass

def sub_lammps_temp(infile):
    temperatures = [1, 2, 3, 4, 5]

    lammps = "lammps/in.runlammpsT"
    delete_lammps(lammps)
    
    for temperature in temperatures:
        with open(infile, "r") as f:
            text = f.read()
            temp = re.sub (r"velocity all create [0-9\.]+", "velocity all create {}".format(temperature), text)
            log = re.sub("log lammps/[A-z0-9\.]*", "log lammps/T{}".format(temperature), temp) 
        with open (lammps, "w") as l:
            l.write(log)
        run_lammps(lammps)

def sub_lammps_temp_dens(infile):
    temperatures = np.linspace(1, 3, 10)
    densities = np.linspace(0.01, 0.5, 10)
    lammps = "lammps/in.runlammpsTD"
    delete_lammps(lammps)

    for temperature in temperatures:
        with open(infile, "r") as f:
            text = f.read()
            temp = re.sub (r"velocity all create [0-9\.]+", "velocity all create {}".format(temperature), text)

        for density in densities:
            dens = re.sub(r"lattice fcc [0-9\.]+", "lattice fcc {}".format(density), temp )
            log = re.sub("log lammps/[A-z0-9\.]*", "log lammps/T{}D{}".format(temperature, density), dens) 
            with open (lammps, "w") as l:
                l.write(log)
            run_lammps(lammps)


if __name__ == "__main__":
    # sub_lammps_temp("lammps/in.myfirstmd")
    sub_lammps_temp_dens("lammps/in.myfirstmd")
