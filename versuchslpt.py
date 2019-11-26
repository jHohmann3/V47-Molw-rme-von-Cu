
import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Graphikbitte')
print('Steigung','Y-Achsenabschnitt')
x, y = np.loadtxt('tab1.txt', unpack=True,delimiter=',')

def f(x,a,b):
    return a*x+b
Werte, Fehler = curve_fit(f, x, y)
print(Werte)
print(np.sqrt(np.diag(Fehler)))

x_new = np.linspace(x[0], x[-1], 500)



plt.figure(1)
plt.plot(x,y,'x')
plt.plot(x_new,f(x_new,*Werte),'-', label='Lineare Regression')
plt.xlabel('$t² $/$ms$')
plt.ylabel('$\ln( \frac {U_c}{U_o})$')
plt.grid()
plt.legend()




plt.savefig('Graphibitte.pdf')
print ('Fertig')
