import serial
import ctypes
import time
import os

# Configuración de teclas multimedia
KEYS = {
    'play_pause': 0xB3,
    'stop': 0xB2,
    'next': 0xB0,
    'prev': 0xB1,
    'vol_up': 0xAF,
    'vol_down': 0xAE
}

def iniciar_reproductor():
    """Abre la primera canción para iniciar el programa """
    ruta_audio = os.path.join(os.getcwd(), 'audio_files')
    
    if os.path.exists(ruta_audio):
        archivos = [f for f in os.listdir(ruta_audio) if f.endswith(('.mp3', '.mp4'))]
        
        if archivos:
            print(f"--- Iniciando reproductor con: {archivos[0]} ---")
            # Abrimos solo el primer archivo de la lista
            primera_cancion = os.path.join(ruta_audio, archivos[0])
            os.startfile(primera_cancion)
            
            print(f"Se detectaron {len(archivos)} archivos en total.")
            print("Usa el comando 'Next' en el cliente para pasar a las siguientes.")
        else:
            print("Aviso: La carpeta 'audio_files' está vacía.")
    else:
        print("Error: No se encontró la carpeta 'audio_files'")

def press_key(hex_code):
    """Simula la presión de tecla a nivel de sistema"""
    ctypes.windll.user32.keybd_event(hex_code, 0, 0, 0)
    time.sleep(0.05)
    ctypes.windll.user32.keybd_event(hex_code, 0, 2, 0)

def iniciar_servidor(puerto='COM2'):
    # Solo llamamos a abrir el reproductor una vez al inicio
    iniciar_reproductor() 
    
    try:
        ser = serial.Serial(puerto, 9600, timeout=1)
        print(f"\n--- SERVIDOR ESCUCHANDO EN {puerto} ---")
        
        while True:
            if ser.in_waiting > 0:
                comando = ser.read().decode('utf-8').lower()
                
                # Mapeo de comandos
                if comando == 'p': press_key(KEYS['play_pause'])
                elif comando == 's': press_key(KEYS['stop'])
                elif comando == 'n': press_key(KEYS['next'])
                elif comando == 'b': press_key(KEYS['prev'])
                elif comando == '+': press_key(KEYS['vol_up'])
                elif comando == '-': press_key(KEYS['vol_down'])
                
                print(f"Ejecutado: {comando}")
                
    except Exception as e:
        print(f"Error en el servidor: {e}")
    finally:
        if 'ser' in locals(): ser.close()

if __name__ == "__main__":
    iniciar_servidor()