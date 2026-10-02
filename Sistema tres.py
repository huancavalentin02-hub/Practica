
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QLabel,
    QMessageBox, QGroupBox, QFormLayout, QHeaderView
)
from PySide6.QtCore import Qt


class SistemaRegistroToga(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema de Registro - Interfaz Toga")
        self.setFixedSize(900, 580)

        # --- DISEÑO GENERAL ---
        self.setStyleSheet("""
            QMainWindow {
                background-color: #F1F5F9;
            }

            QWidget {
                font-family: Segoe UI;
                color: #334155;
            }

            QGroupBox {
                background-color: white;
                border: 1px solid #DCE4EF;
                border-radius: 12px;
                margin-top: 15px;
                padding: 20px 15px 15px 15px;
                font-size: 14px;
                font-weight: bold;
                color: #1E3A8A;
            }

            QGroupBox::title {
                subcontrol-origin: margin;
                left: 15px;
                padding: 0 8px;
                background-color: white;
            }

            QLineEdit {
                background-color: #F8FAFC;
                color: #1E293B;
                border: 1px solid #CBD5E1;
                border-radius: 7px;
                padding: 10px;
                font-size: 11px;
            }

            QLineEdit:focus {
                border: 2px solid #3B82F6;
                background-color: white;
            }

            QPushButton {
                background-color: #2563EB;
                color: white;
                border: none;
                border-radius: 7px;
                padding: 11px;
                font-weight: bold;
                font-size: 10pt;
            }

            QPushButton:hover {
                background-color: #1D4ED8;
            }

            QPushButton:pressed {
                background-color: #1E40AF;
            }

            QTableWidget {
                background-color: white;
                alternate-background-color: #F1F5F9;
                color: #334155;
                border: 1px solid #DCE4EF;
                border-radius: 10px;
                gridline-color: #E2E8F0;
                selection-background-color: #DBEAFE;
                selection-color: #1E3A8A;
                font-size: 10pt;
            }

            QHeaderView::section {
                background-color: #1E3A8A;
                color: white;
                padding: 12px;
                border: none;
                font-weight: bold;
                font-size: 10pt;
            }

            QLabel {
                background-color: transparent;
            }
        """)

        # --- WIDGET CENTRAL ---
        widget_central = QWidget()
        self.setCentralWidget(widget_central)

        layout_general = QVBoxLayout(widget_central)
        layout_general.setContentsMargins(0, 0, 0, 0)
        layout_general.setSpacing(0)

        # --- ENCABEZADO ---
        encabezado = QWidget()
        encabezado.setFixedHeight(110)

        encabezado.setStyleSheet("""
            background-color: #1E3A8A;
        """)

        layout_encabezado = QVBoxLayout(encabezado)
        layout_encabezado.setContentsMargins(30, 15, 30, 15)
        layout_encabezado.setSpacing(5)

        titulo = QLabel("SISTEMA DE REGISTRO")
        titulo.setStyleSheet("""
            color: white;
            font-size: 23px;
            font-weight: bold;
        """)

        subtitulo = QLabel(
            "Administración y gestión de usuarios"
        )
        subtitulo.setStyleSheet("""
            color: #BFDBFE;
            font-size: 11px;
        """)

        layout_encabezado.addWidget(titulo)
        layout_encabezado.addWidget(subtitulo)

        layout_general.addWidget(encabezado)

        # --- CONTENEDOR PRINCIPAL ---
        widget_contenido = QWidget()

        layout_principal = QHBoxLayout(widget_contenido)
        layout_principal.setContentsMargins(25, 20, 25, 20)
        layout_principal.setSpacing(20)

        layout_general.addWidget(widget_contenido)

        # ==========================================
        # PANEL IZQUIERDO: FORMULARIO
        # ==========================================

        grupo_form = QGroupBox("Nuevo Registro")

        layout_form = QFormLayout(grupo_form)
        layout_form.setSpacing(18)
        layout_form.setContentsMargins(18, 25, 18, 20)
        layout_form.setLabelAlignment(
            Qt.AlignmentFlag.AlignLeft
        )

        # Campo nombre
        self.input_nombre = QLineEdit()
        self.input_nombre.setPlaceholderText("Ej. Juan Pérez")

        # Campo correo
        self.input_correo = QLineEdit()
        self.input_correo.setPlaceholderText(
            "Ej. juan@correo.com"
        )

        # Campo teléfono
        self.input_telefono = QLineEdit()
        self.input_telefono.setPlaceholderText("Ej. 70000000")

        layout_form.addRow(
            QLabel("Nombre:"),
            self.input_nombre
        )

        layout_form.addRow(
            QLabel("Correo:"),
            self.input_correo
        )

        layout_form.addRow(
            QLabel("Teléfono:"),
            self.input_telefono
        )

        # --- BOTONES ---
        layout_botones = QHBoxLayout()
        layout_botones.setSpacing(10)

        self.btn_guardar = QPushButton("Registrar")

        self.btn_guardar.setStyleSheet("""
            QPushButton {
                background-color: #2563EB;
                color: white;
                border: none;
                border-radius: 7px;
                padding: 11px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #1D4ED8;
            }

            QPushButton:pressed {
                background-color: #1E40AF;
            }
        """)

        self.btn_guardar.clicked.connect(
            self.agregar_registro
        )

        self.btn_limpiar = QPushButton("Limpiar")

        self.btn_limpiar.setStyleSheet("""
            QPushButton {
                background-color: #E2E8F0;
                color: #334155;
                border: 1px solid #CBD5E1;
                border-radius: 7px;
                padding: 11px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #CBD5E1;
            }

            QPushButton:pressed {
                background-color: #94A3B8;
            }
        """)

        self.btn_limpiar.clicked.connect(
            self.limpiar_formulario
        )

        layout_botones.addWidget(self.btn_guardar)
        layout_botones.addWidget(self.btn_limpiar)

        layout_form.addRow(layout_botones)

        layout_principal.addWidget(grupo_form, stretch=1)

        # ==========================================
        # PANEL DERECHO: TABLA DE REGISTROS
        # ==========================================

        panel_derecho = QVBoxLayout()
        panel_derecho.setSpacing(12)

        # Título de la tabla
        label_tabla = QLabel("Registros Guardados")

        label_tabla.setStyleSheet("""
            font-size: 16px;
            font-weight: bold;
            color: #1E3A8A;
            padding: 5px;
        """)

        panel_derecho.addWidget(label_tabla)

        # Tabla
        self.tabla = QTableWidget()

        self.tabla.setColumnCount(3)

        self.tabla.setHorizontalHeaderLabels([
            "Nombre",
            "Correo",
            "Teléfono"
        ])

        # Ajustar columnas automáticamente
        header = self.tabla.horizontalHeader()

        header.setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        # Ocultar números de filas
        self.tabla.verticalHeader().setVisible(False)

        # Filas alternadas
        self.tabla.setAlternatingRowColors(True)

        # Seleccionar filas completas
        self.tabla.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )

        # Evitar edición directa
        self.tabla.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )

        self.tabla.setShowGrid(True)

        panel_derecho.addWidget(self.tabla)

        layout_principal.addLayout(
            panel_derecho,
            stretch=2
        )

        # --- PIE DE PÁGINA ---
        pie = QLabel(
            "Sistema de Registro | Desarrollado con PySide6"
        )

        pie.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        pie.setFixedHeight(35)

        pie.setStyleSheet("""
            background-color: #E2E8F0;
            color: #64748B;
            font-size: 9px;
            padding: 5px;
        """)

        layout_general.addWidget(pie)

    # ==========================================
    # AGREGAR REGISTRO
    # ==========================================

    def agregar_registro(self):

        nombre = self.input_nombre.text().strip()
        correo = self.input_correo.text().strip()
        telefono = self.input_telefono.text().strip()

        # Validar campos vacíos
        if not nombre or not correo or not telefono:

            QMessageBox.warning(
                self,
                "Campos Vacíos",
                "Por favor completa todos los campos del formulario."
            )

            return

        # Insertar fila en la tabla
        fila_actual = self.tabla.rowCount()

        self.tabla.insertRow(fila_actual)

        self.tabla.setItem(
            fila_actual,
            0,
            QTableWidgetItem(nombre)
        )

        self.tabla.setItem(
            fila_actual,
            1,
            QTableWidgetItem(correo)
        )

        self.tabla.setItem(
            fila_actual,
            2,
            QTableWidgetItem(telefono)
        )

        # Limpiar formulario
        self.limpiar_formulario()

        # Mensaje de confirmación
        QMessageBox.information(
            self,
            "Éxito",
            "Registro guardado correctamente."
        )

    # ==========================================
    # LIMPIAR FORMULARIO
    # ==========================================

    def limpiar_formulario(self):

        self.input_nombre.clear()
        self.input_correo.clear()
        self.input_telefono.clear()


# ==========================================
# PUNTO DE ENTRADA
# ==========================================

if __name__ == '__main__':

    app = QApplication(sys.argv)

    # Forzar estilo claro
    app.setStyle("Fusion")

    ventana = SistemaRegistroToga()

    ventana.show()

    sys.exit(app.exec())
