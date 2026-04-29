import customtkinter as ctk
import serial

# Configuración de apariencia
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AudioControlGUI(ctk.CTk):
    def __init__(self, puerto='COM1'):
        super().__init__()

        # Configuración de la ventana
        self.title("GUMY Audio Control")
        self.geometry("400x500")
        self.resizable(False, False)

        # Intentar conectar al puerto Serial
        try:
            self.ser = serial.Serial(puerto, 9600)
            self.status_text = f"Conectado a {puerto}"
            self.status_color = "#2ecc71" # Verde
        except:
            self.ser = None
            self.status_text = "Error: COM1 no encontrado"
            self.status_color = "#e74c3c" # Rojo

        # --- Interfaz ---
        self.label_titulo = ctk.CTkLabel(self, text="PLAYER CONTROL", font=("Roboto", 24, "bold"))
        self.label_titulo.pack(pady=20)

        # Estado de conexión
        self.status_label = ctk.CTkLabel(self, text=self.status_text, text_color=self.status_color)
        self.status_label.pack(pady=5)

        # Contenedor de Controles Principales
        self.frame_controles = ctk.CTkFrame(self)
        self.frame_controles.pack(pady=20, padx=20, fill="both")

        # Botón Play/Pause (Grande)
        self.btn_play = ctk.CTkButton(self.frame_controles, text="PLAY / PAUSE", 
                                       command=lambda: self.enviar_comando('p'),
                                       height=60, font=("Roboto", 16, "bold"), fg_color="#1a73e8")
        self.btn_play.pack(pady=10, padx=20, fill="x")

        # Botones Next/Prev (Fila)
        self.frame_next_prev = ctk.CTkFrame(self.frame_controles, fg_color="transparent")
        self.frame_next_prev.pack(pady=10)

        self.btn_prev = ctk.CTkButton(self.frame_next_prev, text="⏮ BACK", width=120,
                                       command=lambda: self.enviar_comando('b'))
        self.btn_prev.grid(row=0, column=0, padx=10)

        self.btn_next = ctk.CTkButton(self.frame_next_prev, text="NEXT ⏭", width=120,
                                       command=lambda: self.enviar_comando('n'))
        self.btn_next.grid(row=0, column=1, padx=10)

        # Botón Stop
        self.btn_stop = ctk.CTkButton(self.frame_controles, text="STOP", fg_color="#c0392b", hover_color="#e74c3c",
                                       command=lambda: self.enviar_comando('s'))
        self.btn_stop.pack(pady=10, padx=20, fill="x")

        # Control de Volumen
        self.label_vol = ctk.CTkLabel(self, text="VOLUMEN", font=("Roboto", 12, "bold"))
        self.label_vol.pack(pady=(20, 0))

        self.frame_vol = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_vol.pack(pady=10)

        self.btn_v_down = ctk.CTkButton(self.frame_vol, text="-", width=60, 
                                         command=lambda: self.enviar_comando('-'))
        self.btn_v_down.grid(row=0, column=0, padx=10)

        self.btn_v_up = ctk.CTkButton(self.frame_vol, text="+", width=60, 
                                       command=lambda: self.enviar_comando('+'))
        self.btn_v_up.grid(row=0, column=1, padx=10)

    def enviar_comando(self, char):
        """Envía el comando por serial si la conexión existe"""
        if self.ser:
            self.ser.write(char.encode('utf-8'))
            print(f"Enviado: {char}")
        else:
            print("No hay conexión serial activa.")

if __name__ == "__main__":
    app = AudioControlGUI()
    app.mainloop()