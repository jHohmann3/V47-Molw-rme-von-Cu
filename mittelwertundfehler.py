import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

g, b = np.loadtxt('tab1.txt', unpack=True,delimiter=',')

f = 1/((1/g)+(1/b))
print('Die Brennweiten:')
print(f)
fm=np.mean(f)
ff=np.std(f, ddof=1)/np.sqrt(len(f))

print('der Mittelwert und der Fehler:')
print(fm, ff)