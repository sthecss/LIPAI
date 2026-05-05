# matplotlib
# https://www.youtube.com/watch?v=QLACZgfUAhY&list=PL5jigOsyxDtBEgO2zUUyf_2LNt3Zenrl6&index=1&t=704s

# tive que instalar o: sudo pacman -S tk no arch linux

import matplotlib.pyplot as plt
import numpy as np

# CASO 1: bruto
t = np.linspace(0, 2, 10) # array de valores

print('\n- Nosso vetor de tempo: ', t)

y = np.cos(t)

print('\n- Funcao seno em funcao de t : ', y)

plt.plot(t,y)
plt.show()

# CASO 2: curva
t = np.linspace(0, 2*np.pi, 10) # array de valores

print('\n- Nosso vetor de tempo: ', t)

y = np.cos(t)

print('\n- Funcao seno em funcao de t : ', y)

plt.plot(t,y)
plt.show()

# CASO 3: tornando a curva mais suave
t = np.linspace(0, 2*np.pi, 100) # array de valores

print('\n- Nosso vetor de tempo: ', t)

y = np.cos(t)

print('\n- Funcao seno em funcao de t : ', y)

plt.plot(t,y)
plt.show()

# CASO 4: grafico maior
t = np.linspace(0, 2*np.pi, 500) # array de valores

print('\n- Nosso vetor de tempo: ', t)

y = np.cos(4*t)

print('\n- Funcao seno em funcao de t : ', y)

plt.plot(t,y)
plt.show()

# CASO 5: customizando
t = np.linspace(0, 2*np.pi, 500) # array de valores

print('\n- Nosso vetor de tempo: ', t)

y = np.cos(4*t)

print('\n- Funcao seno em funcao de t : ', y)

plt.plot(t,y)
plt.title('Grafico do Cosseno')
plt.xlabel('Tempo(S)')
plt.ylabel('Amplitude')
plt.show()