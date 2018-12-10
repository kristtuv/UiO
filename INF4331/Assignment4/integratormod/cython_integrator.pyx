import numpy as np
cimport numpy as np

cpdef np.double_t cython_integrate(np.double_t a, np.double_t b, np.int_t N):

    cdef np.ndarray[np.double_t, ndim = 1] x = np.linspace(a, b, N + 1)
    cdef np.double_t dx = (b-a)/N
    cdef np.double_t Sum = 0.0
    cdef np.int_t i
    for i in range(N + 1):
      Sum += x[i]*x[i]*dx
    return Sum

cpdef np.double_t cython_integrate_sin(np.double_t a, np.double_t b, np.int_t N):

    cdef np.ndarray[np.double_t, ndim = 1] x = np.linspace(a, b, N + 1)
    cdef np.double_t dx = (b-a)/N
    cdef np.double_t Sum = 0.0
    cdef np.int_t i
    for i in range(N+1):
      Sum += np.sin(x[i])*dx
    return Sum

cpdef np.double_t cython_midpoint_integrate_sin(np.double_t a, np.double_t b, np.int_t N):
    cdef np.double_t dx = (b-a)/N
    cdef np.double_t dx_midpoint = 0.5*dx
    cdef np.ndarray[np.double_t, ndim = 1] x = np.linspace(a, b, N + 1) - dx_midpoint

    cdef np.double_t Sum = 0.0
    cdef np.int_t i
    for i in range(1, N+1):
      Sum += np.sin(x[i])*dx
    return Sum
