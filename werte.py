import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Graphikbitte')
print('Steigung','Y-Achsenabschnitt')
U,I0,t0,R,TC=np.loadtxt('tab1.txt', unpack=True,delimiter=',')

#def f(x,a,b):
#    return a*x+b
#Werte, Fehler = curve_fit(f, x, y)
#print(Werte)
#print(np.sqrt(np.diag(Fehler)))
#
#x_new = np.linspace(x[0], x[-1], 500)



#plt.figure(1)
#plt.plot(x,y,'x')
#plt.plot(x_new,f(x_new,*Werte),'-', label='Lineare Regression')
#plt.xlabel('$t² $/$ms$')
#plt.ylabel('$\ln( \frac {U_c}{U_o})$')
#plt.grid()
#plt.legend()

I=I0*10**(-3)
t=t0*60
T=0.00134*R**2+2.296*R-243.02
T0=0.00134*23**2+2.296*23-243.02

i = 0
while i < 21:
    dT= T[i] - T[i+1]
    #print(dT)
    i += 1

TK = TC+273.2 

print(T, t)
print(TK)
print(T0)


#plt.savefig('Werte.pdf')
print ('Fertig')
