import wave
import struct
import math

# 1. Configuración de notas (Usando las 7 que listaste)
# Nota: Aunque se llaman "pentatónicas" en tu texto, listaste 7 (escala mayor).
# El código sigue tu lista: Do, Re, Mi, Fa, Sol, La, Si.
frecuencias = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]
duracion = 1 

def generar_escala(nombre, freqs, rate, mono=True):
    with wave.open(nombre, 'w') as f:
        f.setnchannels(1 if mono else 2)
        f.setsampwidth(2) # 16 bits
        f.setframerate(rate)
        for hz in freqs:
            for i in range(int(rate * duracion)):
                val = int(16383 * math.sin(2 * math.pi * hz * i / rate))
                # Uso de PACK para convertir a bytes
                data = struct.pack('<h', val)
                f.writeframesraw(data)
                if not mono: f.writeframesraw(data) # Segundo canal si es stereo

# Ejecución puntos 1, 2 y 3
generar_escala("1_escala_44100_mono.wav", frecuencias, 44100, True)
generar_escala("2_escala_22050_stereo.wav", frecuencias[::-1], 22050, False)
generar_escala("3_escala_8000_mono.wav", frecuencias, 8000, True)

# 4. Generar onda dual (Stereo, 44100, 10s)
rate_4 = 44100
with wave.open("4_onda_dual.wav", 'w') as f:
    f.setnchannels(2); f.setsampwidth(2); f.setframerate(rate_4)
    for i in range(rate_4 * 10):
        # Fórmula exacta del enunciado
        y = int(8000 * math.sin(2*math.pi*500.0/rate_4*i) + 8000*math.sin(2*math.pi*250.0/rate_4*i))
        data = struct.pack('<h', y)
        f.writeframesraw(data * 2) # Escribe el mismo sample en L y R

# 5. Bajar volumen al 75% usando UNPACK (Modificando el archivo anterior)
with wave.open("4_onda_dual.wav", 'r') as original:
    frames = original.readframes(original.getnframes())
    # Convertimos los bytes de vuelta a números usando UNPACK
    # 'h' es para 2 bytes, así que dividimos el largo de frames por 2
    muestras = list(struct.unpack(f'<{len(frames)//2}h', frames))
    
    # Bajamos el volumen (multiplicar por 0.25 para reducir un 75%)
    muestras_bajas = [int(m * 0.25) for m in muestras]
    
    with wave.open("5_onda_volumen_bajo.wav", 'w') as f:
        f.setparams(original.getparams())
        f.writeframes(struct.pack(f'<{len(muestras_bajas)}h', *muestras_bajas))

# 6. Limpiar canal izquierdo (Silenciar L)
with wave.open("5_onda_volumen_bajo.wav", 'r') as original:
    frames = original.readframes(original.getnframes())
    muestras = list(struct.unpack(f'<{len(frames)//2}h', frames))
    
    # En Stereo, los índices pares [0, 2, 4...] son el canal izquierdo (L)
    for i in range(0, len(muestras), 2):
        muestras[i] = 0 
        
    with wave.open("6_onda_canal_limpio.wav", 'w') as f:
        f.setparams(original.getparams())
        f.writeframes(struct.pack(f'<{len(muestras)}h', *muestras))