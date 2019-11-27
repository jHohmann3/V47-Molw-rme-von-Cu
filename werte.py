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

dTn=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
i = 0
while i < 21:
    dTn[i]= T[i+1] - T[i]
    #print(dT)
    i += 1

dT=[9.4,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]

g = 0
while g < 21:
    dT[g+1]= dTn[g]
    g += 1
    
#print(dT)

TK = TC+273.2 

#print(T, t)
#print(TK)
#print(T0)

#cp=63.546*U*t*I*342**(-1)/dT
cp=63.546/342*U*I*t/dT
#cp=63.546*U*I*t/(342*dT)
print(cp)


#plt.savefig('Werte.pdf')
print ('Fertig')
