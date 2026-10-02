
import wx


class CalculadoraWxPython(wx.Frame):

    def __init__(self):
        super().__init__(
            parent=None,
            title="Calculadora con Historial - wxPython",
            size=(700, 500)
        )

        self.historial = []
        self.expresion = ""

        # --- COLORES ---
        self.color_fondo = "#0F172A"
        self.color_panel = "#1E293B"
        self.color_pantalla = "#020617"
        self.color_numero = "#334155"
        self.color_operador = "#2563EB"
        self.color_igual = "#16A34A"
        self.color_limpiar = "#DC2626"

        # --- PANEL PRINCIPAL ---
        panel = wx.Panel(self)
        panel.SetBackgroundColour(self.color_fondo)

        sizer_general = wx.BoxSizer(wx.VERTICAL)

        # ==========================================
        # ENCABEZADO
        # ==========================================

        encabezado = wx.Panel(panel)
        encabezado.SetBackgroundColour("#1E3A8A")

        sizer_encabezado = wx.BoxSizer(wx.VERTICAL)

        titulo = wx.StaticText(
            encabezado,
            label="CALCULADORA MODERNA"
        )

        titulo.SetForegroundColour("#FFFFFF")
        titulo.SetFont(wx.Font(
            20,
            wx.FONTFAMILY_DEFAULT,
            wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_BOLD
        ))

        subtitulo = wx.StaticText(
            encabezado,
            label="Operaciones matemáticas con historial"
        )

        subtitulo.SetForegroundColour("#BFDBFE")
        subtitulo.SetFont(wx.Font(
            10,
            wx.FONTFAMILY_DEFAULT,
            wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_NORMAL
        ))

        sizer_encabezado.Add(titulo, 0, wx.ALIGN_CENTER | wx.TOP, 15)
        sizer_encabezado.Add(subtitulo, 0, wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, 10)

        encabezado.SetSizer(sizer_encabezado)
        encabezado.SetMinSize((-1, 85))

        sizer_general.Add(encabezado, 0, wx.EXPAND)

        # ==========================================
        # CONTENEDOR PRINCIPAL
        # ==========================================

        sizer_principal = wx.BoxSizer(wx.HORIZONTAL)

        # ==========================================
        # PANEL IZQUIERDO: CALCULADORA
        # ==========================================

        panel_calc = wx.Panel(panel)
        panel_calc.SetBackgroundColour(self.color_panel)

        sizer_calc = wx.BoxSizer(wx.VERTICAL)

        # TÍTULO
        lbl_calc = wx.StaticText(
            panel_calc,
            label="Calculadora"
        )

        lbl_calc.SetForegroundColour("#FFFFFF")
        lbl_calc.SetFont(wx.Font(
            14,
            wx.FONTFAMILY_DEFAULT,
            wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_BOLD
        ))

        sizer_calc.Add(
            lbl_calc,
            0,
            wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM,
            15
        )

        # PANTALLA
        self.pantalla = wx.TextCtrl(
            panel_calc,
            style=wx.TE_RIGHT | wx.TE_READONLY
        )

        self.pantalla.SetFont(wx.Font(
            22,
            wx.FONTFAMILY_DEFAULT,
            wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_BOLD
        ))

        self.pantalla.SetBackgroundColour(self.color_pantalla)
        self.pantalla.SetForegroundColour("#38BDF8")
        self.pantalla.SetMinSize((-1, 65))

        sizer_calc.Add(
            self.pantalla,
            0,
            wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM,
            15
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

            sizer_fila = wx.BoxSizer(wx.HORIZONTAL)

            for texto in fila:

                btn = wx.Button(
                    panel_calc,
                    label=texto,
                    size=(-1, 55)
                )

                btn.SetFont(wx.Font(
                    15,
                    wx.FONTFAMILY_DEFAULT,
                    wx.FONTSTYLE_NORMAL,
                    wx.FONTWEIGHT_BOLD
                ))

                # COLORES SEGÚN EL BOTÓN
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

                btn.SetBackgroundColour(color)
                btn.SetForegroundColour("#FFFFFF")

                # Efecto al pasar el cursor
                btn.Bind(
                    wx.EVT_ENTER_WINDOW,
                    lambda evt, b=btn, c=hover: (
                        b.SetBackgroundColour(c),
                        b.Refresh()
                    )
                )

                btn.Bind(
                    wx.EVT_LEAVE_WINDOW,
                    lambda evt, b=btn, c=color: (
                        b.SetBackgroundColour(c),
                        b.Refresh()
                    )
                )

                btn.Bind(
                    wx.EVT_BUTTON,
                    lambda evt, t=texto: self.al_pulsar_boton(t)
                )

                sizer_fila.Add(
                    btn,
                    1,
                    wx.EXPAND | wx.ALL,
                    4
                )

            sizer_calc.Add(
                sizer_fila,
                1,
                wx.EXPAND | wx.LEFT | wx.RIGHT,
                10
            )

        # PIE DE CALCULADORA
        lbl_pie = wx.StaticText(
            panel_calc,
            label="Calculadora | wxPython"
        )

        lbl_pie.SetForegroundColour("#94A3B8")
        lbl_pie.SetFont(wx.Font(
            9,
            wx.FONTFAMILY_DEFAULT,
            wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_NORMAL
        ))

        sizer_calc.Add(
            lbl_pie,
            0,
            wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM,
            12
        )

        panel_calc.SetSizer(sizer_calc)

        sizer_principal.Add(
            panel_calc,
            2,
            wx.EXPAND | wx.ALL,
            15
        )

        # ==========================================
        # PANEL DERECHO: HISTORIAL
        # ==========================================

        panel_hist = wx.Panel(panel)
        panel_hist.SetBackgroundColour(self.color_panel)

        sizer_hist = wx.BoxSizer(wx.VERTICAL)

        # TÍTULO HISTORIAL
        lbl_hist = wx.StaticText(
            panel_hist,
            label="HISTORIAL"
        )

        lbl_hist.SetForegroundColour("#FFFFFF")
        lbl_hist.SetFont(wx.Font(
            15,
            wx.FONTFAMILY_DEFAULT,
            wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_BOLD
        ))

        sizer_hist.Add(
            lbl_hist,
            0,
            wx.ALIGN_CENTER | wx.TOP,
            20
        )

        # SUBTÍTULO
        lbl_subhist = wx.StaticText(
            panel_hist,
            label="Últimas 5 operaciones"
        )

        lbl_subhist.SetForegroundColour("#94A3B8")
        lbl_subhist.SetFont(wx.Font(
            9,
            wx.FONTFAMILY_DEFAULT,
            wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_NORMAL
        ))

        sizer_hist.Add(
            lbl_subhist,
            0,
            wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM,
            12
        )

        # LISTA DE HISTORIAL
        self.lista_historial = wx.ListBox(
            panel_hist,
            style=wx.LB_SINGLE
        )

        self.lista_historial.SetFont(wx.Font(
            10,
            wx.FONTFAMILY_DEFAULT,
            wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_NORMAL
        ))

        self.lista_historial.SetBackgroundColour("#020617")
        self.lista_historial.SetForegroundColour("#38BDF8")

        sizer_hist.Add(
            self.lista_historial,
            1,
            wx.EXPAND | wx.ALL,
            12
        )

        # INFORMACIÓN INFERIOR
        lbl_info = wx.StaticText(
            panel_hist,
            label="Tus operaciones recientes"
        )

        lbl_info.SetForegroundColour("#64748B")

        sizer_hist.Add(
            lbl_info,
            0,
            wx.ALIGN_CENTER | wx.BOTTOM,
            15
        )

        panel_hist.SetSizer(sizer_hist)

        sizer_principal.Add(
            panel_hist,
            1,
            wx.EXPAND | wx.TOP | wx.BOTTOM | wx.RIGHT,
            15
        )

        sizer_general.Add(
            sizer_principal,
            1,
            wx.EXPAND
        )

        # ==========================================
        # PIE DE PÁGINA
        # ==========================================

        pie = wx.Panel(panel)
        pie.SetBackgroundColour("#1E293B")

        sizer_pie = wx.BoxSizer(wx.VERTICAL)

        lbl_pie_general = wx.StaticText(
            pie,
            label="Sistema de Calculadora | Desarrollado con wxPython"
        )

        lbl_pie_general.SetForegroundColour("#94A3B8")
        lbl_pie_general.SetFont(wx.Font(
            9,
            wx.FONTFAMILY_DEFAULT,
            wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_NORMAL
        ))

        sizer_pie.Add(
            lbl_pie_general,
            0,
            wx.ALIGN_CENTER | wx.ALL,
            8
        )

        pie.SetSizer(sizer_pie)

        sizer_general.Add(
            pie,
            0,
            wx.EXPAND
        )

        panel.SetSizer(sizer_general)

        self.Centre()

    # ==========================================
    # FUNCIÓN DE LOS BOTONES
    # ==========================================

    def al_pulsar_boton(self, caracter):

        if caracter == 'C':

            self.expresion = ""
            self.pantalla.SetValue("")

        elif caracter == '=':

            if self.expresion:

                try:

                    resultado = str(eval(self.expresion))

                    operacion = f"{self.expresion} = {resultado}"

                    self.pantalla.SetValue(resultado)

                    self.expresion = resultado

                    self.actualizar_historial(operacion)

                except Exception:

                    self.pantalla.SetValue("Error")

                    self.expresion = ""

        else:

            self.expresion += caracter

            self.pantalla.SetValue(self.expresion)

    # ==========================================
    # ACTUALIZAR HISTORIAL
    # ==========================================

    def actualizar_historial(self, operacion):

        self.historial.append(operacion)

        if len(self.historial) > 5:
            self.historial.pop(0)

        self.lista_historial.Clear()

        for op in reversed(self.historial):
            self.lista_historial.Append(op)


# ==========================================
# PUNTO DE ENTRADA
# ==========================================

if __name__ == '__main__':

    app = wx.App()

    frame = CalculadoraWxPython()

    frame.Show()

    app.MainLoop()
