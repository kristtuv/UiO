import numpy as np
import numba
import time

def numba_integrate(f=lambda x: x**2, a = 0.0, b = 1.0, N = 60000):

    """ Uses numba to integrate function using Riemann integral

        Example usage: numba_integrate(f=lambda x: x**2 , a=0, b=1, N=6000000)
    """
    y = np.linspace(0, 2, 2)
    if isinstance(f(y), (int, float)):
        return f(y)
    else:

        f_jit = numba.jit("f8(f8)", nopython=True)(f) #Make the f-function into a jit function
        @numba.jit("f8(f8, f8, i4)", nopython=True) #decorate the function and tell ut to use jit
        def numba_int(a, b, N):
            x = np.linspace(a, b, N + 1)
            dx = float(b - a)/N
            _sum = 0
            for xi in x:
                _sum += f_jit(xi)*dx
            return _sum

        return numba_int(a, b, N)

def numba_midpoint_integrate(f=lambda x: x**2, a = 0.0, b = 1.0, N = 60000):
    """ Uses numba to integrate function using midpoint integral

        Example usage: numba_midpoint_integrate(f=lambda x: x**2 , a=0, b=1, N=6000000)
    """
    y = np.zeros(1)
    if isinstance(f(y), (int, float)): #Checking if the function is constant
        return(f(y))
    else:
        f_jit = numba.jit("f8(f8)", nopython=True)(f) #Make the f-function into a jit function
        @numba.jit("f8(f8, f8, i4)", nopython=True)#decorate the function and tell ut to use jit

        def numba_int(a, b, N):
            dx = float(b-a)/N
            dx_midpoint = dx*0.5
            x = np.linspace(a, b, N + 1) - dx_midpoint #Creating an array with the midpoints
            x[0] = 0 #Replace first element with zero
            _sum = 0
            for xi in x:
                _sum += f_jit(xi)*dx
            return _sum

        return numba_int(a, b, N)

if __name__ == "__main__":

    for i in range(4):
        t_start = time.clock()
        numba_integrate(f = lambda x: x**2, a=0, b=1, N = 200000000)
        t_stop = time.clock()
        print("Runtime for numba integral: {}".format(t_stop - t_start))
        # t_start = time.clock()
        # numba_midpoint_integrate(f = lambda x: x**2, a=0, b=1, N = 200000000)
        # t_stop = time.clock()
        # print("Runtime for numba midpoint integral: {}".format(t_stop - t_start))
