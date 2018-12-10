import numpy as np
import timeit
import time

def numpy_integrate(f=lambda x: x**2 , a=0, b=1, N=6000000):
    """ Uses numpy to integrate function using Riemann integral

        Example usage: numpy_integrate(f=lambda x: x**2 , a=0, b=1, N=6000000)
    """
    y = np.zeros(1)
    if isinstance(f(y), (int, float)): #Checking if the function is constant
        return(f(y))

    else:
        x = np.linspace(a, b, N + 1)
        dx = float(b-a)/N
        _sum = np.sum(f(x)*dx)
    return _sum

def numpy_midpoint_integrate(f=lambda x: x**2 , a=0.0, b=1.0, N=6000000):
    """ Uses numpy to integrate function using midpoint method

        Example usage:
        numpy_midpoint_integrate(f=lambda x: x**2 , a=0, b=1, N=6000000)
    """
    y = np.zeros(1)
    if isinstance(f(y), (int, float)): #Checking if the function is constant
        return(f(y))
    else:
        dx = float(b-a)/N
        dx_midpoint = dx*0.5
        x = np.linspace(a, b, N + 1) - dx_midpoint #Creating an array with the midpoints
        x[0] = 0 #Replace first element with zero
        if isinstance(f(x), (int,float)): #Checking if the function is constant
            return f(x)
        else:
            _sum = np.sum(f(x)*dx)
        return _sum



if __name__ == "__main__":

    for i in range(4):
        t_start = time.clock()
        numpy_integrate(f = lambda x: x**2, a=0, b=1, N = 2000000)
        t_stop = time.clock()
        print("Runtime for numpy integral: {}".format(t_stop - t_start))
        # t_start = time.clock()
        # print(numpy_midpoint_integrate(f = lambda x: x**2, a=0, b=1, N = 20000000))
        # t_stop = time.clock()
        # print("Runtime for numpy midpoint integral: {}".format(t_stop - t_start))
