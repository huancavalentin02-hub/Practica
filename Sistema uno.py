import tkinter as tk
from tkinter import messagebox, ttk

# --- PALETA DE COLORES Y FUENTES (estilo visual moderno tipo "flat") ---
FONTE = "Segoe UI"
FONTE_TITULO = ("Segoe UI", 18, "bold")
FONTE_SUBTITULO = ("Segoe UI", 10)
FONTE_SECCION = ("Segoe UI", 10, "bold")
FONTE_NORMAL = ("Segoe UI", 10)
FONTE_BOTON = ("Segoe UI", 10, "bold")

COLOR_FONDO = "#EEF2F7"      # Fondo general de la app
COLOR_TARJETA = "#FFFFFF"   # Tarjetas / paneles
COLOR_BORDE = "#D8DEE9"     # Bordes suaves
COLOR_TEXTO = "#1E293B"     # Texto principal
COLOR_SUAVE = "#64748B"     # Texto secundario
COLOR_ACENTO = "#2563EB"    # Azul principal
COLOR_ACENTO_HOVER = "#1D4ED8"
COLOR_PRESIONADO = "#1E40AF"
COLOR_EXITO = "#16A34A"
COLOR_EXITO_HOVER = "#15803D"
COLOR_PELIGRO = "#DC2626"
COLOR_PELIGRO_HOVER = "#B91C1C"
COLOR_LISTA = "#F8FAFC"     # Fondo del visor de texto
COLOR_SOMBRA = "#CBD5E1"


def aplicar_tema(widget):
    """Registra los estilos personalizados (QSS) en el widget raíz."""
    estilo = ttk.Style(widget)
    estilo.theme_use("clam")

    # Fondo global de la ventana
    widget.configure(bg=COLOR_FONDO)

    # Etiquetas de sección dentro de las tarjetas
    estilo.configure(
        "Seccion.TLabel",
        background=COLOR_TARJETA,
        foreground=COLOR_TEXTO,
        font=FONTE_SECCION,
    )
    # Etiquetas de campo
    estilo.configure(
        "Campo.TLabel",
        background=COLOR_TARJETA,
        foreground=COLOR_SUAVE,
        font=FONTE_NORMAL,
    )
    # Título y subtítulo sobre el fondo de la app
    estilo.configure(
        "Titulo.TLabel",
        background=COLOR_FONDO,
        foreground=COLOR_TEXTO,
        font=FONTE_TITULO,
    )
    estilo.configure(
        "Subtitulo.TLabel",
        background=COLOR_FONDO,
        foreground=COLOR_SUAVE,
        font=FONTE_SUBTITULO,
    )

    # Tarjeta: marco blanco con borde (LabelFrame sin texto visible)
    estilo.configure(
        "Tarjeta.TLabelframe",
        background=COLOR_TARJETA,
        bordercolor=COLOR_BORDE,
        lightcolor=COLOR_BORDE,
        darkcolor=COLOR_BORDE,
        relief="solid",
        borderwidth=1,
    )
    estilo.configure(
        "Tarjeta.TLabelframe.Label",
        background=COLOR_FONDO,
        foreground=COLOR_ACENTO,
        font=FONTE_SECCION,
    )

    # Campos de entrada (QLineEdit)
    estilo.configure(
        "Campo.TEntry",
        fieldbackground=COLOR_TARJETA,
        foreground=COLOR_TEXTO,
        bordercolor=COLOR_BORDE,
        lightcolor=COLOR_BORDE,
        darkcolor=COLOR_BORDE,
        borderwidth=1,
        relief="solid",
        padding=8,
        font=FONTE_NORMAL,
    )
    estilo.map(
        "Campo.TEntry",
        bordercolor=[("focus", COLOR_ACENTO)],
        lightcolor=[("focus", COLOR_ACENTO)],
        darkcolor=[("focus", COLOR_ACENTO)],
    )

    # Desplegable (QComboBox)
    estilo.configure(
        "Campo.TCombobox",
        fieldbackground=COLOR_TARJETA,
        background=COLOR_TARJETA,
        foreground=COLOR_TEXTO,
        bordercolor=COLOR_BORDE,
        lightcolor=COLOR_BORDE,
        darkcolor=COLOR_BORDE,
        arrowcolor=COLOR_SUAVE,
        borderwidth=1,
        relief="solid",
        padding=8,
        font=FONTE_NORMAL,
    )
    estilo.map(
        "Campo.TCombobox",
        fieldbackground=[("readonly", COLOR_TARJETA)],
        bordercolor=[("focus", COLOR_ACENTO), ("hover", COLOR_ACENTO)],
        lightcolor=[("focus", COLOR_ACENTO), ("hover", COLOR_ACENTO)],
        darkcolor=[("focus", COLOR_ACENTO), ("hover", COLOR_ACENTO)],
        arrowcolor=[("hover", COLOR_ACENTO)],
    )
    estilo.configure(
        "Campo.TCombobox",
        selectbackground=COLOR_ACENTO,
        selectforeground="#FFFFFF",
    )

    # Botones base / primario / secundario
    estilo.configure(
        "Secundario.TButton",
        background=COLOR_TARJETA,
        foreground=COLOR_SUAVE,
        bordercolor=COLOR_BORDE,
        lightcolor=COLOR_BORDE,
        darkcolor=COLOR_BORDE,
        borderwidth=1,
        relief="solid",
        padding=(14, 10),
        font=FONTE_BOTON,
        anchor="center",
    )
    estilo.map(
        "Secundario.TButton",
        background=[("active", "#F1F5F9"), ("pressed", "#E2E8F0")],
        foreground=[("active", COLOR_TEXTO)],
        bordercolor=[("active", COLOR_ACENTO), ("pressed", COLOR_ACENTO)],
        lightcolor=[("active", COLOR_ACENTO)],
        darkcolor=[("active", COLOR_ACENTO)],
    )

    estilo.configure(
        "Primario.TButton",
        background=COLOR_ACENTO,
        foreground="#FFFFFF",
        bordercolor=COLOR_ACENTO,
        lightcolor=COLOR_ACENTO,
        darkcolor=COLOR_ACENTO,
        borderwidth=1,
        relief="flat",
        padding=(14, 10),
        font=FONTE_BOTON,
        anchor="center",
    )
    estilo.map(
        "Primario.TButton",
        background=[("active", COLOR_ACENTO_HOVER), ("pressed", COLOR_PRESIONADO)],
        bordercolor=[("active", COLOR_ACENTO_HOVER), ("pressed", COLOR_PRESIONADO)],
        lightcolor=[("active", COLOR_ACENTO_HOVER)],
        darkcolor=[("active", COLOR_ACENTO_HOVER)],
    )

    estilo.configure(
        "Exito.TButton",
        background=COLOR_EXITO,
        foreground="#FFFFFF",
        bordercolor=COLOR_EXITO,
        lightcolor=COLOR_EXITO,
        darkcolor=COLOR_EXITO,
        relief="flat",
        padding=(12, 8),
        font=FONTE_BOTON,
        anchor="center",
    )
    estilo.map(
        "Exito.TButton",
        background=[("active", COLOR_EXITO_HOVER), ("pressed", "#166534")],
        bordercolor=[("active", COLOR_EXITO_HOVER), ("pressed", "#166534")],
        lightcolor=[("active", COLOR_EXITO_HOVER)],
        darkcolor=[("active", COLOR_EXITO_HOVER)],
    )

    estilo.configure(
        "Peligro.TButton",
        background=COLOR_TARJETA,
        foreground=COLOR_PELIGRO,
        bordercolor=COLOR_PELIGRO,
        lightcolor=COLOR_PELIGRO,
        darkcolor=COLOR_PELIGRO,
        borderwidth=1,
        relief="solid",
        padding=(12, 8),
        font=FONTE_BOTON,
        anchor="center",
    )
    estilo.map(
        "Peligro.TButton",
        background=[("active", "#FEF2F2"), ("pressed", "#FEE2E2")],
        foreground=[("active", COLOR_PELIGRO)],
    )

    # Casillas y radio buttons (QCheckBox / QRadioButton)
    estilo.configure(
        "Tarjeta.TCheckbutton",
        background=COLOR_TARJETA,
        foreground=COLOR_TEXTO,
        font=FONTE_NORMAL,
        focuscolor=COLOR_TARJETA,
    )
    estilo.map(
        "Tarjeta.TCheckbutton",
        background=[("active", COLOR_TARJETA)],
        foreground=[("active", COLOR_ACENTO), ("disabled", COLOR_SUAVE)],
    )
    estilo.configure(
        "Tarjeta.TRadiobutton",
        background=COLOR_TARJETA,
        foreground=COLOR_TEXTO,
        font=FONTE_NORMAL,
        focuscolor=COLOR_TARJETA,
    )
    estilo.map(
        "Tarjeta.TRadiobutton",
        background=[("active", COLOR_TARJETA)],
        foreground=[("active", COLOR_ACENTO), ("disabled", COLOR_SUAVE)],
    )

    return estilo


def centrar_ventana(ventana, ancho, alto):
    """Centra la ventana en la pantalla y fija su tamaño."""
    ventana.geometry(f"{ancho}x{alto}")
    ventana.update_idletasks()
    x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{max(x, 0)}+{max(y, 0)}")


# --- EQUIVALENTE A QDialog (Ventana Emergente Secundario) 
class VentanaResumenDialog(tk.Toplevel):

    def __init__(self, parent, datos):
        super().__init__(parent)
        self.title("Resumen del Registro (QDialog)")
        centrar_ventana(self, 440, 380)
        self.resizable(False, False)
        self.configure(bg=COLOR_FONDO)
        self.transient(parent)  # QDialog: siempre delante de su ventana padre

        aplicar_tema(self)
        self.style = ttk.Style(self)

        # Franja decorativa superior de acento
        franja = tk.Frame(self, bg=COLOR_ACENTO, height=6)
        franja.pack(fill=tk.X, side=tk.TOP)
        franja.pack_propagate(False)

        # Layout Vertical del Diálogo (QVBoxLayout)
        layout_dialogo = ttk.Frame(self, padding=22)
        layout_dialogo.pack(fill=tk.BOTH, expand=True)

        # Título del diálogo
        ttk.Label(
            layout_dialogo,
            text="Resumen del Registro",
            style="Titulo.TLabel",
        ).pack(anchor=tk.W)

        # Etiqueta de encabezado (QLabel)
        lbl_titulo = ttk.Label(
            layout_dialogo,
            text="Información Procesada:",
            style="Campo.TLabel",
        )
        lbl_titulo.pack(anchor=tk.W, pady=(6, 10))

        # Tarjeta que envuelve al visor de texto
        tarjeta_visor = ttk.Frame(
            layout_dialogo, style="Tarjeta.TFrame", padding=2
        )
        self.style.configure(
            "Tarjeta.TFrame",
            background=COLOR_BORDE,
            borderwidth=1,
            relief="solid",
        )
        tarjeta_visor.pack(fill=tk.BOTH, expand=True)

        # Editor/Visor de texto multilínea (QTextEdit)
        self.txt_resumen = tk.Text(
            tarjeta_visor,
            height=10,
            wrap=tk.WORD,
            font=FONTE_NORMAL,
            bg=COLOR_LISTA,
            fg=COLOR_TEXTO,
            relief=tk.FLAT,
            bd=0,
            padx=14,
            pady=12,
            spacing1=2,
            spacing3=6,
            highlightthickness=0,
            cursor="arrow",
        )
        self.txt_resumen.insert(tk.END, datos)
        self.txt_resumen.config(state=tk.DISABLED)  # Solo lectura
        self.txt_resumen.pack(fill=tk.BOTH, expand=True)

        # Resaltado visual de los datos dentro del visor
        self.txt_resumen.tag_configure("clave", foreground=COLOR_SUAVE, font=FONTE_NORMAL)
        self.txt_resumen.tag_configure("valor", foreground=COLOR_TEXTO, font=("Segoe UI", 10, "bold"))
        self._resaltar_campos()

        # Botón de cierre (QPushButton)
        btn_cerrar = ttk.Button(
            layout_dialogo, text="✕  Cerrar Ventana", style="Primario.TButton",
            command=self.destroy
        )
        btn_cerrar.pack(fill=tk.X, pady=(18, 0))

        self.bind("<Escape>", lambda e: self.destroy())
        self.grab_set()  # Comportamiento modal (QDialog.exec())


# --- EQUIVALENTE A QMainWindow / QApplication (Ventana Principal) ---
class VentanaPrincipalApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Sistema de Registro (Tkinter)")
        centrar_ventana(self, 620, 720)
        self.resizable(False, False)

        aplicar_tema(self)
        self.style = ttk.Style(self)

        # Franja decorativa superior de acento
        franja = tk.Frame(self, bg=COLOR_ACENTO, height=6)
        franja.pack(fill=tk.X, side=tk.TOP)
        franja.pack_propagate(False)

        # Widget Contenedor Central / Layout Principal Vertical (QWidget / QVBoxLayout)
        layout_principal = ttk.Frame(self, padding=(28, 22, 28, 24))
        layout_principal.pack(fill=tk.BOTH, expand=True)

        # 1. ENCABEZADO (QLabel)
        lbl_encabezado = ttk.Label(
            layout_principal,
            text="Formulario de Alta de Usuario",
            style="Titulo.TLabel",
        )
        lbl_encabezado.pack(anchor=tk.W)

        lbl_sub = ttk.Label(
            layout_principal,
            text="Complete los datos para registrar un nuevo usuario en el sistema.",
            style="Subtitulo.TLabel",
        )
        lbl_sub.pack(anchor=tk.W, pady=(4, 18))

        # ========== TARJETA 1: DATOS PERSONALES (QFormLayout & QLineEdit) ==========
        tarjeta_datos = ttk.LabelFrame(
            layout_principal, text="  Datos personales  ", style="Tarjeta.TLabelframe",
            padding=18
        )
        tarjeta_datos.pack(fill=tk.X)
        tarjeta_datos.columnconfigure(1, weight=1)

        # 2. FORMULARIO DE ENTRADA DE TEXTO (QFormLayout & QLineEdit)
        layout_form = ttk.Frame(tarjeta_datos)
        layout_form.pack(fill=tk.X, pady=2)
        layout_form.columnconfigure(1, weight=1)

        ttk.Label(layout_form, text="Nombre Completo:", style="Campo.TLabel").grid(
            row=0, column=0, sticky=tk.W, pady=6, padx=(0, 16)
        )
        self.input_nombre = ttk.Entry(layout_form, style="Campo.TEntry")
        self.input_nombre.grid(row=0, column=1, sticky=tk.EW, pady=6)

        ttk.Label(layout_form, text="Correo Electrónico:", style="Campo.TLabel").grid(
            row=1, column=0, sticky=tk.W, pady=6, padx=(0, 16)
        )
        self.input_correo = ttk.Entry(layout_form, style="Campo.TEntry")
        self.input_correo.grid(row=1, column=1, sticky=tk.EW, pady=6)

        # 3. SELECCIÓN DE OPCIONES Y ROL (QGridLayout, QComboBox & QRadioButton)
        tarjeta_opciones = ttk.LabelFrame(
            layout_principal, text="  Configuración de la cuenta  ", style="Tarjeta.TLabelframe",
            padding=18
        )
        tarjeta_opciones.pack(fill=tk.X, pady=(16, 0))
        tarjeta_opciones.columnconfigure(1, weight=1)

        layout_grid = ttk.Frame(tarjeta_opciones)
        layout_grid.pack(fill=tk.X, pady=2)
        layout_grid.columnconfigure(1, weight=1)

        # QComboBox (Desplegable)
        ttk.Label(layout_grid, text="Rol de Usuario:", style="Campo.TLabel").grid(
            row=0, column=0, sticky=tk.W, pady=6, padx=(0, 16)
        )
        self.combo_rol = ttk.Combobox(
            layout_grid,
            values=["Usuario", "Administrador", "Invitado"],
            state="readonly",
            width=29,
            style="Campo.TCombobox",
        )
        self.combo_rol.current(0)
        self.combo_rol.grid(row=0, column=1, sticky=tk.EW, pady=6)

        # QRadioButton (Opciones dentro de un QHBoxLayout)
        ttk.Label(layout_grid, text="Modalidad:", style="Campo.TLabel").grid(
            row=1, column=0, sticky=tk.W, pady=6, padx=(0, 16)
        )
        self.var_modalidad = tk.StringVar(value="Presencial")

        box_radio = ttk.Frame(layout_grid)
        box_radio.grid(row=1, column=1, sticky=tk.W, pady=6)

        radio_presencial = ttk.Radiobutton(
            box_radio,
            text="Presencial",
            value="Presencial",
            variable=self.var_modalidad,
            style="Tarjeta.TRadiobutton",
        )
        radio_presencial.pack(side=tk.LEFT, padx=(0, 18))

        radio_remoto = ttk.Radiobutton(
            box_radio, text="Remoto", value="Remoto", variable=self.var_modalidad,
            style="Tarjeta.TRadiobutton"
        )
        radio_remoto.pack(side=tk.LEFT)

        # ========== TARJETA 2: PREFERENCIAS (QCheckBox) ==========
        tarjeta_preferencias = ttk.LabelFrame(
            layout_principal, text="  Preferencias  ", style="Tarjeta.TLabelframe",
            padding=18
        )
        tarjeta_preferencias.pack(fill=tk.X, pady=(16, 0))

        # 4. CASILLAS DE VERIFICACIÓN (QCheckBox)
        frame_checks = ttk.Frame(tarjeta_preferencias)
        frame_checks.pack(fill=tk.X, pady=2)

        self.var_terminos = tk.BooleanVar(value=False)
        self.check_terminos = ttk.Checkbutton(
            frame_checks,
            text="Acepto los términos y condiciones",
            variable=self.var_terminos,
            style="Tarjeta.TCheckbutton",
        )
        self.check_terminos.pack(anchor=tk.W, pady=4)

        self.var_boletin = tk.BooleanVar(value=False)
        self.check_boletin = ttk.Checkbutton(
            frame_checks,
            text="Deseo recibir información por correo",
            variable=self.var_boletin,
            style="Tarjeta.TCheckbutton",
        )
        self.check_boletin.pack(anchor=tk.W, pady=4)

        # ========== BARRA DE ESTADO / PISTA ==========
        lbl_pista = ttk.Label(
            layout_principal,
            text="Los campos marcados son obligatorios para poder guardar el registro.",
            style="Subtitulo.TLabel",
        )
        lbl_pista.pack(anchor=tk.W, pady=(14, 0))

        # Separador (QFrame / QLine con efecto HLine)
        separador = ttk.Frame(layout_principal)
        separador.pack(fill=tk.X, pady=(14, 0))
        separador.configure(style="TSeparator")

        # 5. BOTONES DE ACCIÓN (QHBoxLayout & QPushButton)
        layout_botones = ttk.Frame(layout_principal)
        layout_botones.pack(fill=tk.X, pady=(14, 0))

        btn_limpiar = ttk.Button(
            layout_botones,
            text="Limpiar Formulario",
            style="Secundario.TButton",
            command=self.limpiar_campos,
        )
        btn_limpiar.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 8))

        btn_guardar = ttk.Button(
            layout_botones,
            text="Guardar y Ver Resumen  →",
            style="Primario.TButton",
            command=self.procesar_y_mostrar,
        )
        btn_guardar.pack(side=tk.RIGHT, expand=True, fill=tk.X, padx=(8, 0))

        # Atajos de teclado y foco inicial
        self.bind("<Return>", lambda e: self.procesar_y_mostrar())
        self.bind("<Escape>", lambda e: self.limpiar_campos())
        self.input_nombre.focus_set()

    # --- MÉTODOS Y LÓGICA DE FUNCIONAMIENTO ---
    def limpiar_campos(self):
        self.input_nombre.delete(0, tk.END)
        self.input_correo.delete(0, tk.END)
        self.combo_rol.current(0)
        self.var_modalidad.set("Presencial")
        self.var_terminos.set(False)
        self.var_boletin.set(False)

    def procesar_y_mostrar(self):
        nombre = self.input_nombre.get().strip()
        correo = self.input_correo.get().strip()

        if not nombre or not correo:
            messagebox.showwarning(
                "Advertencia", "Por favor ingrese el Nombre y el Correo."
            )
            return

        rol = self.combo_rol.get()
        modalidad = self.var_modalidad.get()
        terminos = "Aceptados" if self.var_terminos.get() else "No Aceptados"
        boletin = "Sí" if self.var_boletin.get() else "No"

        datos_texto = (
            f"Nombre: {nombre}\n"
            f"Correo: {correo}\n"
            f"Rol: {rol}\n"
            f"Modalidad: {modalidad}\n"
            f"Términos: {terminos}\n"
            f"Boletín informativo: {boletin}"
        )

        # Despliegue de la ventana emergente (QDialog equivalente)
        VentanaResumenDialog(self, datos_texto)

    def _resaltar_campos(self):
        """Aplica el estilo a las etiquetas del visor del resumen."""
        texto = self.txt_resumen
        texto.tag_remove("clave", "1.0", tk.END)
        texto.tag_remove("valor", "1.0", tk.END)
        for i, linea in enumerate(texto.get("1.0", tk.END).splitlines(), start=1):
            if ":" in linea:
                clave, valor = linea.split(":", 1)
                texto.tag_add("clave", f"{i}.0", f"{i}.{len(clave)}")
                texto.tag_add("valor", f"{i}.{len(clave) + 1}", f"{i}.end")


# --- PUNTO DE ENTRADA ---
if __name__ == "__main__":
    app = VentanaPrincipalApp()
    app.mainloop()
