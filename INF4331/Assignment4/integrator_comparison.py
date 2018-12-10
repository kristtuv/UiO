from integratormod import integrator as itg
from integratormod import cython_integrator as cy
from integratormod import numba_integrator as nmb
from integratormod import numpy_integrator as npi

import time
import numpy as np

#Defining function variables and error
error = 9*1e-11 # Making error a little smaller to compensate for roundoff
f = lambda x: np.sin(x)
a = 0.0
b = np.pi
N = 1

#List of integrators
integrators = [itg.integrate, itg.midpoint_integrate, npi.numpy_integrate,\
npi.numpy_midpoint_integrate, nmb.numba_integrate, nmb.numba_midpoint_integrate]

#List of integratornames
integrator_names = ["pure python", "pure python midpoint", "numpy", "numpy_midpoint",\
"numba", "numba_midpoint"]

#Loop over integrators until error requirement is fulfilled
for i in range(len(integrators)):
    while abs(2.0 - integrators[i](f, a, b, N)) > error:
         N += 1000
    else:
        print("Error for {} at N value {} is {} ".format(integrator_names[i], N, abs(2.0 - integrators[i](f, a, b, N))))
        N = 1

#Separate list for cython because f value is hardcoded in cython code
c_int = [cy.cython_integrate_sin, cy.cython_midpoint_integrate_sin]
c_int_name= ["cython", "cython_midpoint"]

M = 1
for i in range(len(c_int)):
    while abs(2.0 - c_int[i](a, b, M)) > error:
         M += 1000
    else:
        print("Error for {} at N value {} is {} ".format(c_int_name[i], M, abs(2.0 - c_int[i](a, b, M))))
        M = 1
