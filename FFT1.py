import numpy as np, matplotlib.pyplot as plt

FREQ_0 = 1000
FREQ_1 = 50
SAMPLE = 44100
S_RATE = 44100.0

S_1 = [np.sin(2 * np.pi * FREQ_0 * t / S_RATE) for t in range(SAMPLE)]
S_2 = [np.sin(2 * np.pi * FREQ_1 * t / S_RATE) for t in range(SAMPLE)]
W_1 = np.array(S_1) ; W_2 = np.array(S_2)
w12 = W_1 + W_2

# FFT
fft_result = np.fft.fft(w12)
freqs = np.fft.fftfreq(len(w12), 1 / S_RATE)

# Solo parte positiva
half = len(freqs) // 2

# Crear figura
plt.figure(figsize=(7,5), facecolor="lightgray")

# Onda original (1000 Hz)
plt.subplot(4,1,1)
plt.plot(S_1[:500], 'b')
plt.title("Onda Original")
plt.ylim(-1.1, 1.1)
plt.xlim(0, 499)

# Onda ruido (50 Hz)
plt.subplot(4,1,2)
plt.plot(S_2[:4000], 'b')
plt.title("Onda Ruido")
plt.ylim(-1.1, 1.1)
plt.xlim(0, 3999)

# Suma de ambas
plt.subplot(4,1,3)
plt.plot(w12[:3000], 'b')
plt.title("Onda Original + Ruidosa")
plt.ylim(-2.2, 2.2)
plt.xlim(0, 2999)

# FFT
plt.subplot(4,1,4)
plt.plot(freqs[:half], np.abs(fft_result[:half]), 'b')
plt.title("Frecuencias en las Ondas (FFT)")
plt.xlim(0, 1200)

plt.tight_layout()
plt.show()