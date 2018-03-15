import pylab as pl
import nest.voltage_trace
import nest.raster_plot

nest.ResetKernel()

neuron = nest.Create("iaf_psc_alpha")
nest.SetStatus(neuron, {"I_e": 376.0})
