import numpy as np
import matplotlib.pyplot as plt

FREQ_0 = 9000
FREQ_1 = 5000
FREQ_2 = 100
SAMPLE = 20000
S_RATE = 20000.0

t = np.arange(SAMPLE)

# Ondas

aW = [
    2*np.sin(2*np.pi * FREQ_0 * t/S_RATE),
    3*np.sin(2*np.pi * FREQ_1 * t/S_RATE),
    9*np.sin(2*np.pi * FREQ_2 * t/S_RATE)
]

# Señales

aS = [
    aW[0] + aW[1],      # Signal 1
    aW[0] + aW[2],      # Signal 2
    aW[1] * aW[2]       # Signal 3
]

def Filter_Comp(aV, nA):
    aF = np.zeros(len(aV))
    # CAMBIO 1: Inicializamos en 0 para que no empiece desde el pico de la señal
    aF[0] = 0

    for i in range(1, len(aV)):
        aF[i] = nA * aV[i] + (1.0 - nA) * aF[i-1]

    return aF

alpha_gral = 0.1
f1 = Filter_Comp(aS[0], alpha_gral)
f2 = Filter_Comp(aS[1], 0.001)
f3 = Filter_Comp(aS[2], alpha_gral)

plt.figure(figsize=(9, 9), facecolor="silver")

# Signal 1

plt.subplot(3,1,1)
plt.plot(aS[0][:200], 'b', linewidth=0.8)
plt.plot(f1[:200], 'r', linewidth=1.2)
plt.title("Signal 1")
plt.ylim(-6, 6)
plt.xlim(0, 200)

# Signal 2 - LA IMPORTANTE

plt.subplot(3,1,2)
plt.plot(aS[1][:200], 'b', linewidth=0.8)
plt.plot(f2[:200], 'r', linewidth=1.5) # Esta línea ahora debería estar en el centro
plt.title("Signal 2")
plt.ylim(-15, 15) # CAMBIO 3: Escala fija para que se vea pequeña la roja
plt.xlim(0, 200)

# Signal 3

plt.subplot(3,1,3)
plt.plot(aS[2][:200], 'b', linewidth=0.8)
plt.plot(f3[:200], 'r', linewidth=1.2)
plt.title("Signal 3")
plt.ylim(-30, 30)
plt.xlim(0, 200)
plt.tight_layout()
plt.show()