import numpy as np
import matplotlib.pyplot as plt
import time

def integrate(f, a, b, N):
    """ Uses pure python to integrate function using Riemann sum

        Example usage:
        integrate(f=lambda x: x**2 , a=0, b=1, N=6000000)
    """
    y = np.zeros(1)
    if isinstance(f(y), (int, float)): #Checking if the function is constant
        return(f(y))
    else:
        x = np.linspace(a, b, N + 1)
        _sum = 0
        dx = float(b - a)/N
        for xi in x:
            _sum += f(xi)*dx
        return _sum

def midpoint_integrate(f, a, b, N):
    """ Uses pure python to integrate function using midpoint method

        Example usage:
        midpoint_integrate(f=lambda x: x**2 , a=0, b=1, N=6000000)
    """
    y = np.zeros(1)
    if isinstance(f(y), (int, float)):
        return(f(y))

    else:
        _sum = 0
        dx = float(b-a)/N
        dx_midpoint = dx*0.5
        x = np.linspace(a, b, N + 1) - dx_midpoint #Creating an array with the midpoints
        x[0] = 0 #Replace first element with zero
        for xi in x:
            _sum += f(xi)*dx
        return _sum


def plot_error(f = lambda x: x**2, a=0, b=1, Nmax=500, Nmin=10, stepsize=10, plot = True):
    "Plots the error of a x^2 compared to the real answer which is 1/3 "
    error = []
    mesh = []

    for N in range(Nmin, Nmax + 1, stepsize):
        mesh.append(N)
        error.append(abs(1./3 - integrate(f, a, b, N)))
    if plot:
        fig = plt.figure(figsize=[7,5])
        ax = plt.subplot(111)
        ax.plot(mesh, error)
        ax.set_xlabel('Number of mesh points (N)')
        ax.set_ylabel('Error')
        ax.set_title("Error for nummerical integral of f(x) = x^2")
        fig.savefig("quadratic_error.png")
        plt.show()
if __name__ == "__main__":
    for i in range(4):

        t_start = time.clock()
        integrate(f = lambda x: x**2, a=0, b=1, N = 10000)
        t_stop = time.clock()
        print("Runtime for pure python integral: {}".format(t_stop - t_start))
        # t_start = time.clock()
        # midpoint_integrate(f = lambda x: x**2, a=0, b=1, N = 2000)
        # t_stop = time.clock()
        # print("Runtime for pure python midpoint integral: {}".format(t_stop - t_start))
    #plot_error()
