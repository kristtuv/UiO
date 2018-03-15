import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
a = []
b = []
with open('/Users/Tuv/Documents/UiO/H17/FYS3710/EPR/3710e3h.dat','r') as f:
    df = pd.DataFrame(l.rstrip().split() for l in f)

B_H = (3131.8 + 3639.2)/2.0
B_D = (3325.6 + 3480.7)/2.0
f = 9.5396e9
h = 6.62607004e-34
beta = 9.274009e-24
g_H = h*f/(beta * B_H*10**-4)
g_D = h*f/(beta * B_D*10**-4)
print g_H, g_D
print B_H, B_D
a_H = 50.74e-3
a_D = 7.755e-3
corrH = 50.75**2/(4*3385.5)
corrD = 7.755**2/(4*3403.15)
print corrH, corrD
print -corrH*10**-4 + g_H, -corrD*10**-4 + g_D
mu = 1.257e-6 #T*m/A
g_N_H = 5.585
g_N_D = 0.857
bohr = 0.529e-10
psi = (3*a_H)/(2*mu*beta*g_N_H)
psi2 = 1./(np.pi*(bohr**3))
psi3 = (3*a_D)/(2*mu*beta*g_N_D)
print psi, psi2, psi3













exit()
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(list(df[0]),list(df[1]), label= "EPR Data")
ax.plot([3131, 3639], [109798, 109798], "r-")
ax.plot([3325, 3480], [38410, 38410], "r-", label = "a-values")
ax.plot([3480, 3480], [38410, 19759], "r-")
ax.plot([B_H, B_H], [100000, 120000],label="B_0 Hydrogen" )
ax.plot([B_D, B_D], [31000, 45000], label="B_0 Deuterium")

ax.annotate(r"$a_H$", xy=((3131 + 3639)/2.0, 109789), xytext=(-15,-15), textcoords='offset points')
ax.annotate(r"$2\times a_D$", xy=((3325 + 3480)/2.0, 38410), xytext=(-5,15), textcoords='offset points')



plt.xlabel("Gauss")
plt.ylabel("Amplitude")


# Now add the legend with some customizations.
legend = ax.legend(loc=3)

# The frame is matplotlib.patches.Rectangle instance surrounding the legend.
frame = legend.get_frame()
frame.set_facecolor('0.90')
plt.savefig("epr.png")
