from numpy import *
import matplotlib.pylab as plt



def simulate(
   beta=0.9,                 # dimensionless parameter
   Theta=30,                 # initial angle in degrees
   epsilon=0,                # initial stretch of wire
   num_periods=6,            # simulate for num_periods
   time_steps_per_period=60, # time step resolution
   plot=True,                # make plots or not
   ):


	P = 2*pi; #Period of pendulum	
	T = num_periods*P #Total time of simulation
	dt = P/float(time_steps_per_period) #delta t

	
	Nt = int(round(T/dt)) #Number of time steps
	t = linspace(0, Nt*dt, Nt+1)
	
   	y = zeros(Nt + 1)
   	x = zeros(Nt + 1)
   	
   	#Initial conditions
	x[0] = (1 + epsilon)*sin(radians(Theta));
	x[1] = - beta/(1 - beta)*(1 - beta/L)*x[n]*dt**2 + 2*x[n]x[0]
	y[0] = 1 - (1 + epsilon)*cos(radians(Theta));
	y[1] = y[0] 

	for n in range(1, Nt):
		L = sqrt(x[n + 1]**2 + (y[n + 1] - 1)**2)
		x[n+1] = - beta/(1 - beta)*(1 - beta/L)*x[n]*dt**2                    + 2*x[n] - x[n-1]
		y[n+1] = - beta/(1 - beta)*(1 - beta/L)*(y[n] - 1)*dt**2 - beta*dt**2 + 2*y[n] - y[n-1]
		

	return x, y
x, y = simulate()
plt.plot(x,y)
plt.gca().set_aspect('equal')
plt.show()


