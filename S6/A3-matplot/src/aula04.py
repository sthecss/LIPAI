
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2*np.pi, 500)

#
# CASO 1: Seno e Cos numa mesma figure. 2x1
#
cos = np.cos(x)
sen = np.sin(x)

plt.subplot(1,2,1)
plt.plot(x,cos)

plt.subplot(1,2,2)
plt.plot(x,sen)

plt.show()

#
# CASO 2: Seno e Cos numa mesma figure. Grid 1X2
#
cos = np.cos(x)
sen = np.sin(x)

plt.subplot(2,1,1)
plt.plot(x,cos)

plt.subplot(2,1,2)
plt.plot(x,sen)

plt.show()

#
# CASO 4: Seno e Cos numa mesma figure. Grid 2x2
#
cos = np.cos(x)
sen = np.sin(x)

plt.subplot(2,2,1)
plt.plot(x,cos)

plt.subplot(2,2,2)
plt.plot(x,sen)

plt.subplot(2,2,3)
plt.plot(x,cos)

plt.subplot(2,2,4)
plt.plot(x,sen)

plt.show()

#
# CASO 5: Seno e Cos numa mesma figure. Grid 2x2 + elegante
#
cos = np.cos(x)
sen = np.sin(x)

# Configurar a config do gráfico
plt.figure("Graficos Cosenoidais", figsize=(10,5))
plt.subplots(
    left = 0.15,
    bottom = 0.15,
    right = 0.9,
    top = 0.9,
    wspace = 0.5,
)

ax1 = plt.subplot(1,2,1)
plt.plot(x,cos)
ax1.set_title("Grafico do Cos")
ax1.set_xlabel("Eixo do Tempo")
ax1.set_ylabel("Eixo da Amplitude")

ax2 = plt.subplot(1,2,2)
plt.plot(x,sen)
ax2.set_title("Grafico do Sen")
ax2.set_xlabel("Eixo do Tempo")
ax2.set_ylabel("Eixo da Amplitude")

plt.show()