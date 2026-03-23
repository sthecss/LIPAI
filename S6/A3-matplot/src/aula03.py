# matplotlib
# https://www.youtube.com/watch?v=QZyFklCAbxk&list=PL5jigOsyxDtBEgO2zUUyf_2LNt3Zenrl6&index=3

import matplotlib.pyplot as plt
import numpy as np

#
# CASO 1: Camada da FIGURE:
#
t1 = np.arange(0,100)
y = np.exp(t1)

plt.figure("Grafico Exp()", figsize=(10,5))
plt.plot(t1,y)


#
# CASO 2: Sen e Cos mais elegantes
#
t2 = np.linspace(0,2*np.pi, 100)
yCos = np.cos(t2)
ySen = np.sin(t2)

plt.figure("Grafico Sen e Cos", figsize=(10,5))
plt.plot(t2,ySen)
plt.plot(t2,yCos)
plt.grid()
plt.title("Grafico Sen e Cos:")
plt.xlabel("Tempo")
plt.ylabel("Amplitude")

plt.show()
