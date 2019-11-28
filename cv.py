import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Graphikbitte')
print('Steigung','Y-Achsenabschnitt')
cv, T = np.loadtxt('tab2.txt', unpack=True,delimiter=',')

#def f(x,a,b):
#    return a*x+b
#Werte, Fehler = curve_fit(f, x, y)
#print(Werte)
#print(np.sqrt(np.diag(Fehler)))
#
#x_new = np.linspace(x[0], x[-1], 500)



plt.figure(1)
plt.plot(T,cv,'x')
#plt.plot(x_new,f(x_new,*Werte),'-', label='Lineare Regression')
plt.xlabel('$C_{v}$/$..$')
plt.ylabel('$T$/K')
plt.grid()
plt.legend()




plt.savefig('cv.pdf')
print ('Fertig')
