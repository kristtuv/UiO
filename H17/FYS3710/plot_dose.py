import numpy as np
import matplotlib.pylab as plt
dose = [10, 20, 68]
H1 = [65356, 82503, 2.105e5]
H2 = [3.481e4, 4.307e4, 1.078e5]
a1, b1 = np.polyfit(dose, H1, 1)
a2, b2 = np.polyfit(dose, H2, 1)
LBH1 = 1.222e5
LBH2 = 6.575e4


fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(dose, H1, "o")
plt.plot(dose, H2, "o")
plt.plot(dose, a1*np.array(dose) + b1)
plt.plot(dose, a2*np.array(dose) + b2)
plt.plot((LBH1 - b1)/a1, LBH1, "o")
plt.plot((LBH2 - b2)/a2, LBH2, "o")
plt.plot([4,4], [0, 80000], "--")
ax.annotate("J.L dose H1: %.2f" %((LBH1 - b1)/a1), xy=((LBH1 - b1)/a1, LBH1), xytext=(10,-3), textcoords='offset points')
ax.annotate("J.L dose H2: %.2f" %((LBH2 - b2)/a2), xy=((LBH2 - b2)/a2, LBH2), xytext=(10,-5), textcoords='offset points')
plt.xlabel("Grey")
plt.ylabel("Peak to Peak")
plt.legend(["H1 data", "H2 data", "H1 best fit", "H2 best fit", "J.L dose H1", "J.L dose H2", r"$\approx$$LD_{50}$"])
plt.savefig("JL.jpg")
plt.show()
