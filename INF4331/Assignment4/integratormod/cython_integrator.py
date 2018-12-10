import cython_integrator as cy
import time
for i in range(4):
    time_start = time.clock()
    cy.cython_integrate(a = 0.0, b = 0.0, N = 200000000)
    time_stop = time.clock()
    print("Runtime for cython integral: {}".format(time_stop - time_start))
