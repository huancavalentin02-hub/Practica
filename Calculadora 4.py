
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QListWidget, QLabel, QMessageBox,
    QFrame
)
from PySide6.QtCore import Qt


class CalculadoraPySide6(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora con Historial - PySide6")
        self.setFixedSize(650, 460)

        self.historial = []
        self.expresion = ""

        # ==========================================
        # ESTILO GENERAL
        # ==========================================

        self.setStyleSheet("""
            QMainWindow {
                background-color: #0F172A;
            }

            QWidget {
                font-family: Segoe UI;
                color: #E2E8F0;
            }

            QMenuBar {
                background-color: #1E293B;
                color: white;
                padding: 5px;
                font-size: 11px;
            }

            QMenuBar::item {
                padding: 7px 14px;
            }

            QMenuBar::item:selected {
                background-color: #334155;
                border-radius: 5px;
            }

            QMenu {
                background-color: #1E293B;
                color: white;
                border: 1px solid #475569;
                padding: 5px;
            }

            QMenu::item {
                padding: 8px 20px;
            }

            QMenu::item:selected {
                background-color: #2563EB;
            }

            QMessageBox {
                background-color: #1E293B;
            }

            QMessageBox QLabel {
                color: white;
                font-size: 12px;
            }

            QMessageBox QPushButton {
                background-color: #2563EB;
                color: white;
                border-radius: 6px;
                padding: 6px 18px;
                min-width: 60px;
            }

            QMessageBox QPushButton:hover {
                background-color: #1D4ED8;
            }
        """)

        # ==========================================
        # MENÚ
        # ==========================================

        self.crear_menu()

        # ==========================================
        # WIDGET CENTRAL
        # ==========================================

        widget_central = QWidget()
        self.setCentralWidget(widget_central)

        layout_general = QVBoxLayout(widget_central)
        layout_general.setContentsMargins(0, 0, 0, 0)
        layout_general.setSpacing(0)

        # ==========================================
        # ENCABEZADO
        # ==========================================

        encabezado = QFrame()
        encabezado.setFixedHeight(75)

        encabezado.setStyleSheet("""
            QFrame {
                background-color: #1E3A8A;
                border: none;
            }
        """)

        layout_encabezado = QVBoxLayout(encabezado)
        layout_encabezado.setSpacing(2)

        titulo = QLabel("CALCULADORA MODERNA")

        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        titulo.setStyleSheet("""
            color: white;
            font-size: 20px;
            font-weight: bold;
        """)

        subtitulo = QLabel("Operaciones matemáticas con historial")

        subtitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        subtitulo.setStyleSheet("""
            color: #BFDBFE;
            font-size: 10px;
        """)

        layout_encabezado.addWidget(titulo)
        layout_encabezado.addWidget(subtitulo)

        layout_general.addWidget(encabezado)

        # ==========================================
        # CONTENEDOR PRINCIPAL
        # ==========================================

        contenedor = QWidget()

        layout_principal = QHBoxLayout(contenedor)

        layout_principal.setContentsMargins(15, 12, 15, 12)
        layout_principal.setSpacing(12)

        layout_general.addWidget(contenedor)

        # ==========================================
        # PANEL IZQUIERDO
        # ==========================================

        panel_calc_widget = QFrame()

        panel_calc_widget.setStyleSheet("""
            QFrame {
                background-color: #1E293B;
                border: 1px solid #334155;
                border-radius: 12px;
            }
        """)

        panel_calc = QVBoxLayout(panel_calc_widget)

        panel_calc.setContentsMargins(15, 12, 15, 12)
        panel_calc.setSpacing(8)

        # TÍTULO
        lbl_calc = QLabel("Calculadora")

        lbl_calc.setAlignment(Qt.AlignmentFlag.AlignCenter)

        lbl_calc.setStyleSheet("""
            font-size: 15px;
            font-weight: bold;
            color: #FFFFFF;
            border: none;
        """)

        panel_calc.addWidget(lbl_calc)

        # PANTALLA
        self.pantalla = QLineEdit()

        self.pantalla.setAlignment(
            Qt.AlignmentFlag.AlignRight
        )

        self.pantalla.setReadOnly(True)

        self.pantalla.setFixedHeight(58)

        self.pantalla.setStyleSheet("""
            QLineEdit {
                background-color: #020617;
                color: #38BDF8;
                border: 2px solid #475569;
                border-radius: 9px;
                padding: 8px;
                font-size: 23px;
                font-weight: bold;
            }

            QLineEdit:focus {
                border: 2px solid #38BDF8;
            }
        """)

        panel_calc.addWidget(self.pantalla)

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

            layout_fila = QHBoxLayout()
            layout_fila.setSpacing(7)

            for texto in fila:

                btn = QPushButton(texto)

                btn.setMinimumHeight(48)

                btn.setCursor(
                    Qt.CursorShape.PointingHandCursor
                )

                # COLORES
                if texto == 'C':

                    color = "#DC2626"
                    hover = "#B91C1C"

                elif texto == '=':

                    color = "#16A34A"
                    hover = "#15803D"

                elif texto in ['+', '-', '*', '/']:

                    color = "#2563EB"
                    hover = "#1D4ED8"

                else:

                    color = "#334155"
                    hover = "#475569"

                btn.setStyleSheet(f"""
                    QPushButton {{
                        background-color: {color};
                        color: white;
                        border: none;
                        border-radius: 8px;
                        font-size: 17px;
                        font-weight: bold;
                    }}

                    QPushButton:hover {{
                        background-color: {hover};
                    }}

                    QPushButton:pressed {{
                        background-color: #64748B;
                    }}
                """)

                btn.clicked.connect(
                    lambda _, t=texto: self.al_pulsar_boton(t)
                )

                layout_fila.addWidget(btn)

            panel_calc.addLayout(layout_fila)

        # PIE DEL PANEL
        lbl_pie = QLabel("Calculadora | PySide6")

        lbl_pie.setAlignment(Qt.AlignmentFlag.AlignCenter)

        lbl_pie.setStyleSheet("""
            color: #64748B;
            font-size: 9px;
            border: none;
            padding-top: 3px;
        """)

        panel_calc.addWidget(lbl_pie)

        layout_principal.addWidget(
            panel_calc_widget,
            stretch=2
        )

        # ==========================================
        # PANEL DERECHO: HISTORIAL
        # ==========================================

        panel_hist_widget = QFrame()

        panel_hist_widget.setStyleSheet("""
            QFrame {
                background-color: #1E293B;
                border: 1px solid #334155;
                border-radius: 12px;
            }
        """)

        panel_hist = QVBoxLayout(panel_hist_widget)

        panel_hist.setContentsMargins(12, 15, 12, 12)
        panel_hist.setSpacing(8)

        # TÍTULO
        lbl_hist = QLabel("HISTORIAL")

        lbl_hist.setAlignment(Qt.AlignmentFlag.AlignCenter)

        lbl_hist.setStyleSheet("""
            color: white;
            font-size: 15px;
            font-weight: bold;
            border: none;
        """)

        panel_hist.addWidget(lbl_hist)

        # SUBTÍTULO
        lbl_hist_sub = QLabel("Últimas 5 operaciones")

        lbl_hist_sub.setAlignment(Qt.AlignmentFlag.AlignCenter)

        lbl_hist_sub.setStyleSheet("""
            color: #94A3B8;
            font-size: 10px;
            border: none;
        """)

        panel_hist.addWidget(lbl_hist_sub)

        # LISTA DE HISTORIAL
        self.lista_historial = QListWidget()

        self.lista_historial.setStyleSheet("""
            QListWidget {
                background-color: #020617;
                color: #38BDF8;
                border: 1px solid #334155;
                border-radius: 8px;
                padding: 5px;
                font-size: 11px;
            }

            QListWidget::item {
                padding: 9px;
                border-bottom: 1px solid #1E293B;
            }

            QListWidget::item:selected {
                background-color: #1E3A8A;
                color: white;
            }
        """)

        panel_hist.addWidget(self.lista_historial)

        # INFORMACIÓN
        lbl_info = QLabel("Operaciones recientes")

        lbl_info.setAlignment(Qt.AlignmentFlag.AlignCenter)

        lbl_info.setStyleSheet("""
            color: #64748B;
            font-size: 9px;
            border: none;
        """)

        panel_hist.addWidget(lbl_info)

        layout_principal.addWidget(
            panel_hist_widget,
            stretch=1
        )

        # ==========================================
        # PIE DE PÁGINA
        # ==========================================

        pie = QLabel(
            "Sistema de Calculadora | Desarrollado con Python y Qt"
        )

        pie.setAlignment(Qt.AlignmentFlag.AlignCenter)

        pie.setFixedHeight(25)

        pie.setStyleSheet("""
            background-color: #1E293B;
            color: #94A3B8;
            font-size: 9px;
        """)

        layout_general.addWidget(pie)

    # ==========================================
    # CREAR MENÚ
    # ==========================================

    def crear_menu(self):

        barra_menu = self.menuBar()

        menu_archivo = barra_menu.addMenu("Archivo")

        accion_limpiar = menu_archivo.addAction("Limpiar todo")

        accion_limpiar.triggered.connect(
            self.reiniciar_calculadora
        )

        menu_archivo.addSeparator()

        accion_salir = menu_archivo.addAction("Salir")

        accion_salir.triggered.connect(self.close)

        menu_ayuda = barra_menu.addMenu("Ayuda")

        accion_acerca = menu_ayuda.addAction("Acerca de")

        accion_acerca.triggered.connect(
            self.mostrar_acerca_de
        )

    # ==========================================
    # REINICIAR CALCULADORA
    # ==========================================

    def reiniciar_calculadora(self):

        self.expresion = ""

        self.pantalla.setText("")

        self.historial.clear()

        self.lista_historial.clear()

    # ==========================================
    # ACERCA DE
    # ==========================================

    def mostrar_acerca_de(self):

        QMessageBox.information(
            self,
            "Acerca de la Calculadora",
            "Calculadora con Historial en PySide6\n"
            "Desarrollada con Python y Qt."
        )

    # ==========================================
    # FUNCIÓN DE LOS BOTONES
    # ==========================================

    def al_pulsar_boton(self, caracter):

        if caracter == 'C':

            self.expresion = ""
            self.pantalla.setText("")

        elif caracter == '=':

            if self.expresion:

                try:

                    resultado = str(eval(self.expresion))

                    operacion = f"{self.expresion} = {resultado}"

                    self.pantalla.setText(resultado)

                    self.expresion = resultado

                    self.actualizar_historial(operacion)

                except Exception:

                    self.pantalla.setText("Error")

                    self.expresion = ""

        else:

            self.expresion += caracter

            self.pantalla.setText(self.expresion)

    # ==========================================
    # ACTUALIZAR HISTORIAL
    # ==========================================

    def actualizar_historial(self, operacion):

        self.historial.append(operacion)

        if len(self.historial) > 5:
            self.historial.pop(0)

        self.lista_historial.clear()

        for op in reversed(self.historial):

            self.lista_historial.addItem(op)


# ==========================================
# PUNTO DE ENTRADA
# ==========================================

if __name__ == '__main__':

    app = QApplication(sys.argv)

    app.setStyle("Fusion")

    win = CalculadoraPySide6()

    win.show()

    sys.exit(app.exec())
