
import customtkinter as ctk

# --- CONFIGURACIÓN GENERAL ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class CalculadoraCustomTkinter(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Calculadora Moderna")
        self.geometry("650x470")
        self.resizable(False, False)

        self.historial = []
        self.expresion = ""

        # COLORES
        self.color_fondo = "#141B2D"
        self.color_panel = "#1E293B"
        self.color_pantalla = "#0F172A"
        self.color_numero = "#334155"
        self.color_operador = "#2563EB"
        self.color_igual = "#16A34A"
        self.color_limpiar = "#DC2626"

        self.configure(fg_color=self.color_fondo)

        # CONFIGURACIÓN DE COLUMNAS
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ==========================================
        # PANEL IZQUIERDO: CALCULADORA
        # ==========================================

        frame_calc = ctk.CTkFrame(
            self,
            fg_color=self.color_panel,
            corner_radius=18
        )

        frame_calc.grid(
            row=0,
            column=0,
            padx=(15, 8),
            pady=15,
            sticky="nsew"
        )

        frame_calc.grid_columnconfigure(
            (0, 1, 2, 3),
            weight=1
        )

        # TÍTULO
        lbl_titulo = ctk.CTkLabel(
            frame_calc,
            text="CALCULADORA",
            font=("Arial", 20, "bold"),
            text_color="#E2E8F0"
        )

        lbl_titulo.pack(pady=(20, 5))

        lbl_subtitulo = ctk.CTkLabel(
            frame_calc,
            text="Operaciones matemáticas básicas",
            font=("Arial", 10),
            text_color="#94A3B8"
        )

        lbl_subtitulo.pack(pady=(0, 15))

        # PANTALLA
        self.pantalla = ctk.CTkEntry(
            frame_calc,
            font=("Arial", 26, "bold"),
            justify="right",
            height=65,
            corner_radius=12,
            fg_color=self.color_pantalla,
            text_color="#38BDF8",
            border_color="#334155",
            border_width=2
        )

        self.pantalla.pack(
            fill="x",
            padx=18,
            pady=(0, 20)
        )

        # ==========================================
        # BOTONES
        # ==========================================

        botones = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        for fila in botones:

            f_frame = ctk.CTkFrame(
                frame_calc,
                fg_color="transparent"
            )

            f_frame.pack(
                fill="x",
                padx=15,
                pady=5,
                expand=True
            )

            for texto in fila:

                # COLORES SEGÚN BOTÓN
                if texto == 'C':
                    color = self.color_limpiar
                    hover = "#B91C1C"

                elif texto == '=':
                    color = self.color_igual
                    hover = "#15803D"

                elif texto in ['+', '-', '*', '/']:
                    color = self.color_operador
                    hover = "#1D4ED8"

                else:
                    color = self.color_numero
                    hover = "#475569"

                btn = ctk.CTkButton(
                    f_frame,
                    text=texto,
                    width=55,
                    height=48,
                    corner_radius=10,
                    font=("Arial", 17, "bold"),
                    fg_color=color,
                    hover_color=hover,
                    text_color="white",
                    command=lambda t=texto: self.al_pulsar_boton(t)
                )

                btn.pack(
                    side="left",
                    expand=True,
                    fill="both",
                    padx=4
                )

        # PIE DE CALCULADORA
        lbl_pie = ctk.CTkLabel(
            frame_calc,
            text="Calculadora | CustomTkinter",
            font=("Arial", 9),
            text_color="#64748B"
        )

        lbl_pie.pack(pady=(15, 10))

        # ==========================================
        # PANEL DERECHO: HISTORIAL
        # ==========================================

        frame_hist = ctk.CTkFrame(
            self,
            fg_color=self.color_panel,
            corner_radius=18
        )

        frame_hist.grid(
            row=0,
            column=1,
            padx=(8, 15),
            pady=15,
            sticky="nsew"
        )

        # TÍTULO HISTORIAL
        lbl_hist = ctk.CTkLabel(
            frame_hist,
            text="HISTORIAL",
            font=("Arial", 16, "bold"),
            text_color="#E2E8F0"
        )

        lbl_hist.pack(pady=(22, 5))

        lbl_hist_sub = ctk.CTkLabel(
            frame_hist,
            text="Últimas 5 operaciones",
            font=("Arial", 10),
            text_color="#94A3B8"
        )

        lbl_hist_sub.pack(pady=(0, 15))

        # CAJA DEL HISTORIAL
        self.txt_historial = ctk.CTkTextbox(
            frame_hist,
            width=180,
            state="disabled",
            corner_radius=12,
            fg_color=self.color_pantalla,
            text_color="#CBD5E1",
            font=("Consolas", 11),
            border_width=1,
            border_color="#334155"
        )

        self.txt_historial.pack(
            fill="both",
            expand=True,
            padx=12,
            pady=(0, 12)
        )

        # ETIQUETA INFERIOR
        lbl_info = ctk.CTkLabel(
            frame_hist,
            text="Las operaciones recientes\naparecen aquí",
            font=("Arial", 9),
            text_color="#64748B",
            justify="center"
        )

        lbl_info.pack(pady=(0, 15))

    # ==========================================
    # FUNCIÓN DE LOS BOTONES
    # ==========================================

    def al_pulsar_boton(self, caracter):

        if caracter == 'C':

            self.expresion = ""
            self.pantalla.delete(0, 'end')

        elif caracter == '=':

            if self.expresion:

                try:

                    resultado = str(eval(self.expresion))

                    operacion = f"{self.expresion} = {resultado}"

                    self.pantalla.delete(0, 'end')
                    self.pantalla.insert(0, resultado)

                    self.expresion = resultado

                    self.actualizar_historial(operacion)

                except Exception:

                    self.pantalla.delete(0, 'end')
                    self.pantalla.insert(0, "Error")

                    self.expresion = ""

        else:

            self.expresion += caracter

            self.pantalla.delete(0, 'end')
            self.pantalla.insert(0, self.expresion)

    # ==========================================
    # ACTUALIZAR HISTORIAL
    # ==========================================

    def actualizar_historial(self, operacion):

        self.historial.append(operacion)

        if len(self.historial) > 5:
            self.historial.pop(0)

        self.txt_historial.configure(state="normal")

        self.txt_historial.delete("1.0", "end")

        for op in reversed(self.historial):

            self.txt_historial.insert(
                "end",
                f"  {op}\n\n"
            )

        self.txt_historial.configure(state="disabled")


# ==========================================
# PUNTO DE ENTRADA
# ==========================================

if __name__ == '__main__':

    app = CalculadoraCustomTkinter()

    app.mainloop()

