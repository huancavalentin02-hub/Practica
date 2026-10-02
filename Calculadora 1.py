import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

ESTILO = """
QWidget#Raiz {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 #1f2233, stop:1 #12141f);
}

QLabel#Titulo {
    color: #ffffff;
    font-size: 17px;
    font-weight: 700;
    letter-spacing: 1px;
}

QLabel#Subtitulo {
    color: #7d84a0;
    font-size: 11px;
}

QLabel#HistorialTitulo {
    color: #8f97b5;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
}

QLineEdit#Pantalla {
    background: #0c0e17;
    border: 1px solid #2a2f45;
    border-radius: 14px;
    color: #eef2ff;
    font-family: "Consolas", "Menlo", monospace;
    font-size: 30px;
    font-weight: 600;
    padding: 14px 16px;
    selection-background-color: #4f7cff;
}

QLineEdit#Pantalla:focus {
    border: 1px solid #4f7cff;
}

QPushButton {
    background: #262b40;
    border: none;
    border-radius: 12px;
    color: #e8ecfb;
    font-size: 19px;
    font-weight: 600;
    min-height: 46px;
}

QPushButton:hover {
    background: #333a55;
}

QPushButton:pressed {
    background: #4f7cff;
    color: #ffffff;
}

QPushButton#Numero {
    background: #2a3050;
}

QPushButton#Numero:hover {
    background: #364070;
}

QPushButton#Operador {
    background: #3a2c63;
    color: #c9b6ff;
    font-size: 22px;
}

QPushButton#Operador:hover {
    background: #4a3785;
}

QPushButton#Operador:pressed {
    background: #6f4fd8;
    color: #ffffff;
}

QPushButton#Igual {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 #4f7cff, stop:1 #7a4dff);
    color: #ffffff;
    font-size: 22px;
}

QPushButton#Igual:hover {
    background: #5f8bff;
}

QPushButton#Borrar {
    background: #5c2740;
    color: #ffb8c8;
}

QPushButton#Borrar:hover {
    background: #7a3352;
}

QPushButton#Borrar:pressed {
    background: #d3456b;
    color: #ffffff;
}

QListWidget {
    background: #171a29;
    border: 1px solid #2a2f45;
    border-radius: 14px;
    color: #b9c0dc;
    font-size: 12px;
    padding: 6px;
    outline: none;
}

QListWidget::item {
    padding: 8px 6px;
    border-radius: 8px;
}

QListWidget::item:selected {
    background: #2a3350;
    color: #ffffff;
}

QListWidget::item:hover {
    background: #21263a;
}

QFrame#Separador {
    background: #2a2f45;
    max-height: 1px;
    min-height: 1px;
    border: none;
}
"""


class CalculadoraPySide6(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora con Historial - PySide6")
        self.setFixedSize(520, 430)

        self.historial = []
        self.expresion = ""

        # Widget principal
        widget_central = QWidget()
        widget_central.setObjectName("Raiz")
        self.setCentralWidget(widget_central)
        layout_principal = QHBoxLayout(widget_central)
        layout_principal.setContentsMargins(24, 22, 24, 22)
        layout_principal.setSpacing(20)

        # --- PANEL IZQUIERDO: CALCULADORA ---
        panel_calc = QVBoxLayout()
        panel_calc.setSpacing(12)

        encabezado = QLabel("Calculadora")
        encabezado.setObjectName("Titulo")
        panel_calc.addWidget(encabezado)

        subtitulo = QLabel("PySide6 · historial de las últimas 5 operaciones")
        subtitulo.setObjectName("Subtitulo")
        panel_calc.addWidget(subtitulo)

        self.pantalla = QLineEdit()
        self.pantalla.setObjectName("Pantalla")
        self.pantalla.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.pantalla.setReadOnly(True)
        self.pantalla.setFont(QFont("Consolas", 22, QFont.Weight.Bold))
        self.pantalla.setMinimumHeight(70)
        panel_calc.addWidget(self.pantalla)

        # Botones
        botones = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        grid = QGridLayout()
        grid.setSpacing(10)

        estilos = {
            'C': 'Borrar',
            '=': 'Igual',
            '/': 'Operador',
            '*': 'Operador',
            '-': 'Operador',
            '+': 'Operador',
        }

        for fila_idx, fila in enumerate(botones):
            for col_idx, texto in enumerate(fila):
                btn = QPushButton(texto)
                btn.setObjectName(estilos.get(texto, 'Numero'))
                btn.setCursor(Qt.CursorShape.PointingHandCursor)
                btn.clicked.connect(lambda _, t=texto: self.al_pulsar_boton(t))
                grid.addWidget(btn, fila_idx, col_idx)

        panel_calc.addLayout(grid)
        panel_calc.addStretch(1)

        layout_principal.addLayout(panel_calc, stretch=3)

        # --- PANEL DERECHO: HISTORIAL (Últimas 5) ---
        panel_hist = QVBoxLayout()
        panel_hist.setSpacing(12)

        separador = QFrame()
        separador.setObjectName("Separador")
        separador.setFrameShape(QFrame.Shape.NoFrame)
        panel_hist.addWidget(separador)

        titulo_hist = QLabel("HISTORIAL")
        titulo_hist.setObjectName("HistorialTitulo")
        panel_hist.addWidget(titulo_hist)

        self.lista_historial = QListWidget()
        self.lista_historial.setAlternatingRowColors(False)
        self.lista_historial.setMinimumWidth(170)
        panel_hist.addWidget(self.lista_historial)

        layout_principal.addLayout(panel_hist, stretch=2)

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

    def actualizar_historial(self, operacion):
        self.historial.append(operacion)
        if len(self.historial) > 5:
            self.historial.pop(0)

        self.lista_historial.clear()
        for op in reversed(self.historial):
            self.lista_historial.addItem(op)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(ESTILO)
    win = CalculadoraPySide6()
    win.show()
    sys.exit(app.exec())