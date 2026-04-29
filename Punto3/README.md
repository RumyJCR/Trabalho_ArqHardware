# PUNTO 3 - Control de WINAMP/AIMP por Puerto Serial

## Descripción
Sistema cliente-servidor que controla un reproductor de audio (Winamp, AIMP) usando:
- **Servidor:** Escucha puerto serial COM y emula teclas multimedia con Win32 API
- **Cliente:** Envía comandos por puerto serial (PLAY, STOP, NEXT, PREV, VOL+, VOL-, PAUSE, MUTE)
- **Protocolo:** Comunicación serial ASCII simple a través de VSPE

## Archivos
- `servidor.py` - Servidor (emula teclas multimedia)
- `cliente.py` - Cliente interactivo
- `audio_files/` - 12 archivos MP3 para reproducir

## Requisitos
```bash
pip install pyserial
```

## Instalación VSPE
1. Descargar VSPE: https://www.virtual-serial-port.org/
2. Instalar y abrir VSPE
3. Crear par de puertos: **COM3** ↔ **COM4**

## Verificar Puertos
Windows + X → Administrador de dispositivos → Puertos (COM y LPT)
Deberías ver COM3 y COM4 (Virtual Serial Port)

## Uso

### Terminal 1 - Servidor
```bash
python servidor.py COM3 9600
```
Espera mensajes de: `Servidor en COM3 @ 9600 baud`

### Terminal 2 - Cliente
```bash
python cliente.py COM3 9600
```
Verás prompt: `>`

## Comandos
Desde el cliente, escribe:
```
> PLAY        (reproducir)
> PAUSE       (pausar)
> STOP        (detener)
> NEXT        (siguiente)
> PREV        (anterior)
> VOL+        (volumen +)
> VOL-        (volumen -)
> MUTE        (silenciar)
> HELP        (listar comandos)
> EXIT        (salir)
```

## Arquitectura
```
CLIENTE                VSPE              SERVIDOR           WINAMP/AIMP
python cliente.py ←→ COM3 ↔ COM4 ←→ python servidor.py ←→ Win32 API
    (envía)        Virtual Port    (escucha/emula)      (controla)
```

## Protocolo Serial
- **Baudrate:** 9600
- **Formato:** ASCII texto + newline (`\n`)
- **Ejemplo:**
  ```
  Cliente → Servidor:  "PLAY\n"
  Servidor → Cliente:  "OK: PLAY\n"
  ```

## Códigos de Teclas Win32 Usados
| Comando | Código |
|---------|--------|
| PLAY    | 0xB3   |
| STOP    | 0xB2   |
| NEXT    | 0xB0   |
| PREV    | 0xB1   |
| VOL+    | 0xAF   |
| VOL-    | 0xAE   |
| MUTE    | 0xAD   |

## Troubleshooting

### "Puerto COM3 no encontrado"
- Verifica que VSPE tiene puertos activos
- Usa el puerto correcto si VSPE asignó otro (COM5, etc.)
- Asegúrate que VSPE está ejecutándose

### "Sin respuesta del servidor"
- Verifica que terminal 1 (servidor) está corriendo
- Usa el MISMO puerto en ambos: `COM3 COM3`
- Intenta reiniciar VSPE

### "Teclas no funcionan"
- Winamp/AIMP debe estar en primer plano (ventana activa)
- Verifica que las teclas multimedia funcionan manualmente (prueba Fn+Play, etc.)
- Algunos reproductores no soportan estas teclas

## Carpeta audio_files/
Contiene 12 archivos MP3:
1. AIRBAG.mp3
2. Bruce Wayne.mp3
3. Fentanyl.mp3
4. MOOD.mp3
5. Ojos empapados.mp3
6. Paquepu.mp3
7. Rush.mp3
8. Shiny.mp3
9. Whyme.mp3
10. wtfff.mp3
11. Ya entregamos el depa.mp3
12. Zundada de fondo.mp3

**Instrucciones:**
1. Abre Winamp/AIMP
2. Carga carpeta `audio_files/` en la playlist
3. Deja en pausa
4. Ejecuta servidor y cliente
5. En cliente: `> PLAY` y controla desde ahí

## Ejemplo de Sesión
```
Terminal 1 (Servidor):
  20:30:45 - Servidor en COM3 @ 9600 baud
  20:30:45 - Esperando comandos...
  20:30:50 - Recibido: PLAY
  20:30:50 - Tecla emulada: 0xB3
  20:30:50 - Respuesta: OK: PLAY

Terminal 2 (Cliente):
  > PLAY
  Respuesta: OK: PLAY
  
  > VOL+
  Respuesta: OK: VOL+
  
  > NEXT
  Respuesta: OK: NEXT
  
  > EXIT
  Respuesta: BYE
```

---

**Punto 3 Completado:**
✅ Control WINAMP/AIMP por puerto serial
✅ Win32 API (User32.Keybd_event)
✅ VSPE para comunicación serial
✅ Cliente-Servidor con protocolo ASCII
✅ 12 archivos MP3 listos
