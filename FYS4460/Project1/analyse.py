# analyse.py
# run with  in.myfirstmd
# velocity (temmperature) = 2.0
from ovito.io import import_file
from ovito.modifiers import *
from ovito import dataset
import matplotlib.pyplot as plt
import numpy as np
from ovito.data import *

def velocity_histogram(filename):
    pipeline = import_file(filename,\
    columns = ["Particle Identifier", "Particle Type", "Position.X", "Position.Y", "Position.Z",\
     "Velocity.X", "Velocity.Y", "Velocity.Z", "Potential Energy", "Kinetic Energy"], multiple_frames=True)

    myComputePropertyModifier = \
        ComputePropertyModifier(
                output_property="Velocity Magnitude",
                expressions=["sqrt( Velocity.X^2+Velocity.Y^2+Velocity.Z^2)"]
                )
    pipeline.modifiers.append(myComputePropertyModifier)

    myHistogramModifier = HistogramModifier(
                            property="Velocity Magnitude",
                            bin_count=200)
    pipeline.modifiers.append(myHistogramModifier)

    velocityhistogram = HistogramModifier(
                             property="Velocity.X",
                             bin_count=200)
    pipeline.modifiers.append(velocityhistogram)

    
    #Ploting histogram of velocity in X-direction    
    fig2 = plt.figure(1)
    max_boltz = fig2.add_subplot(1,1,1)
    max_boltz.set_xlabel('Velocity')
    fig2.suptitle('Velocity in X-direction')
    pipeline.compute(dataset.anim.first_frame)
    max_boltz.plot(velocityhistogram.histogram[:,1], label=str("frame {}:".format(dataset.anim.first_frame)))
    pipeline.compute(dataset.anim.last_frame)
    max_boltz.plot(velocityhistogram.histogram[:,1], label=str("frame {}:".format(dataset.anim.last_frame)))
    max_boltz.legend()

   
    #Ploting normalized innerproduct of the histogram
    fig1 = plt.figure(0)
    fig1.suptitle('Normalized innerproduct')

    norm = fig1.add_subplot(1,1,1)
    pipeline.compute(dataset.anim.last_frame)
    reference = myHistogramModifier.histogram[:,1]
    norm_innerprod = []

    
    for frame in range(dataset.anim.first_frame, dataset.anim.last_frame, 10):
        pipeline.compute(frame)
        histogram = myHistogramModifier.histogram[:,1]
        norm_innerprod.append(sum(abs(reference - histogram)))
        
    norm.plot(norm_innerprod/max(norm_innerprod))
    norm.legend(["Absolute error"])
    norm.set_xlabel('Frames')
    norm.set_ylabel('Normalized innerporduct')
    fig1.savefig('img/Normalized.png')
    fig2.savefig('img/Histogram.png')
    plt.show()

if __name__ == "__main__":
    velocity_histogram("lammps/dumptest.lammpstrj")


