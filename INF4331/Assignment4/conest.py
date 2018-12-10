from integratormod import numba_integrator as nbi
from integratormod import numpy_integrator as npi
from numpy import pi, sin
a = 0.00000001
b = 1e7
N = 25000000
def f1(x):
    return (sin(x)/x) * (sin(x/3.0)/(x/3.0)) * (sin(x/5.0)/(x/5.0))


def f2(x):
    return (sin(x)/x) * (sin(x/3.0)/(x/3.0)) * (sin(x/5.0)/(x/5.0)) * (sin(x/7.0)/(x/7.0))

def f3(x):
    return (sin(x)/x) * (sin(x/3.0)/(x/3.0)) * (sin(x/5.0)/(x/5.0)) * (sin(x/7.0)/(x/7.0))\
            * (sin(x/9.0)/(x/9.0)) * (sin(x/11.0)/(x/11.0))

def f4(x):
    return (sin(x)/x) * (sin(x/3.0)/(x/3.0)) * (sin(x/5.0)/(x/5.0)) * (sin(x/7.0)/(x/7.0))\
            * (sin(x/9.0)/(x/9.0)) * (sin(x/11.0)/(x/11.0)) * (sin(x/13.0)/(x/13.0))


def f5(x):
    return (sin(x)/x) * (sin(x/3.0)/(x/3.0)) * (sin(x/5.0)/(x/5.0)) * (sin(x/7.0)/(x/7.0))\
            * (sin(x/9.0)/(x/9.0)) * (sin(x/11.0)/(x/11.0)) * (sin(x/13.0)/(x/13.0)) * (sin(x/15.0)/(x/15.0))

def f6(x):
    return (sin(x)/x) * (sin(x/4.0)/(x/4.0)) * (sin(x/4.0)/(x/4.0)) * (sin(x/7.0)/(x/7.0))\
    * (sin(x/7.0)/(x/7.0)) * (sin(x/9.0)/(x/9.0)) * (sin(x/9.0)/(x/9.0))

print("Integral 1: {}".format(1./pi*npi.numpy_integrate(f1, a, b, N)))
print("Integral 2: {}".format(1./pi*npi.numpy_integrate(f2, a, b, N)))
print("Integral 3: {}".format(1./pi*npi.numpy_integrate(f3, a, b, N)))
print("Integral 4: {}".format(1./pi*npi.numpy_integrate(f4, a, b, N)))
print("Integral 5: {}".format(1./pi*npi.numpy_integrate(f5, a, b, N)))
print("Integral 6: {}".format(1./pi*npi.numpy_integrate(f6, a, b, N)))
