
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi, 500) # array de valores
yCos = np.cos(4*t)
ySen = np.sin(4*t)

#
# CASO 1: Gráfico base:
#
plt.plot(t,yCos)
plt.title('Grafico do Cosseno')
plt.xlabel('Tempo(S)')
plt.ylabel('Amplitude')

#
# CASO 2: Camada da FIGURE:
#
plt.title('Grafico do Cosseno')
plt.xlabel('Tempo(S)')
plt.ylabel('Amplitude')

#
# CASO 3: uso de .figure(num)
#
plt.figure(1)
plt.plot(t,yCos)
plt.title('Grafico do Cosseno')
plt.xlabel('Tempo(S)')
plt.ylabel('Amplitude')

plt.figure(2)
plt.plot(t,ySen)
plt.title('Grafico do Seno')
plt.xlabel('Tempo(S)')
plt.ylabel('Amplitude')

#
# CASO 4: uso de .figure(largura, altura)
#
plt.figure(1, figsize=(5,4))
plt.plot(t,yCos)
plt.title('Grafico do Cosseno')
plt.xlabel('Tempo(S)')
plt.ylabel('Amplitude')

plt.figure(2, figsize=(6,7))
plt.plot(t,ySen)
plt.title('Grafico do Seno')
plt.xlabel('Tempo(S)')
plt.ylabel('Amplitude')

plt.show()