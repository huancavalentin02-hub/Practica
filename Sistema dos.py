import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDialog,
    QFormLayout,
    QGridLayout,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QRadioButton,
    QTableWidget,
    QTableWidgetItem,
    QTabWidget,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


# --- ESTILO GLOBAL (QSS) APLICADO A TODA LA APLICACIÓN ---
ESTILO_GLOBAL = """
* {
    font-family: "Segoe UI", "Inter", "Helvetica Neue", sans-serif;
}

/* ---------- Fondo general ---------- */
QMainWindow, QDialog {
    background-color: #eef2f7;
}

/* ---------- Encabezado ---------- */
QLabel#titulo {
    font-size: 22px;
    font-weight: 700;
    color: #0f172a;
    padding: 4px 2px 2px 2px;
}

QLabel#subtitulo {
    font-size: 13px;
    font-weight: 500;
    color: #64748b;
}

QLabel#titulo_seccion {
    font-size: 14px;
    font-weight: 700;
    color: #0f172a;
    padding: 4px 2px;
}

/* ---------- Contenedor con borde de "tarjeta" ---------- */
QFrame#tarjeta {
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
}

/* ---------- Pestañas ---------- */
QTabWidget::pane {
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    top: -1px;
}

QTabBar::tab {
    background: transparent;
    color: #64748b;
    padding: 10px 22px;
    margin-right: 4px;
    border: none;
    border-bottom: 3px solid transparent;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    font-size: 13px;
    font-weight: 600;
}

QTabBar::tab:hover {
    color: #4f46e5;
    background-color: #f1f5ff;
}

QTabBar::tab:selected {
    color: #4f46e5;
    border-bottom: 3px solid #4f46e5;
    background-color: #f8faff;
}

/* ---------- Botones ---------- */
QPushButton {
    background-color: #4f46e5;
    color: #ffffff;
    border: none;
    border-radius: 8px;
    padding: 9px 18px;
    font-size: 13px;
    font-weight: 600;
    min-height: 18px;
}

QPushButton:hover {
    background-color: #4338ca;
}

QPushButton:pressed {
    background-color: #3730a3;
    padding-top: 10px;
    padding-bottom: 8px;
}

QPushButton:disabled {
    background-color: #cbd5e1;
    color: #94a3b8;
}

QPushButton#btnNuevo {
    background-color: #4f46e5;
}
QPushButton#btnNuevo:hover {
    background-color: #4338ca;
}

QPushButton#btnEliminar {
    background-color: #ef4444;
}
QPushButton#btnEliminar:hover {
    background-color: #dc2626;
}
QPushButton#btnEliminar:pressed {
    background-color: #b91c1c;
}

QPushButton#btnGuardar {
    background-color: #10b981;
}
QPushButton#btnGuardar:hover {
    background-color: #059669;
}
QPushButton#btnGuardar:pressed {
    background-color: #047857;
}

QPushButton#btnCancelar {
    background-color: #eef2f7;
    color: #475569;
    border: 1px solid #cbd5e1;
}
QPushButton#btnCancelar:hover {
    background-color: #e2e8f0;
    color: #0f172a;
}
QPushButton#btnCancelar:pressed {
    background-color: #cbd5e1;
}

/* ---------- Campos de texto y combos ---------- */
QLineEdit, QComboBox, QSpinBox, QDoubleSpinBox, QTextEdit, QPlainTextEdit {
    background-color: #ffffff;
    border: 1px solid #d8dee9;
    border-radius: 8px;
    padding: 8px 12px;
    color: #0f172a;
    font-size: 13px;
    selection-background-color: #4f46e5;
    selection-color: #ffffff;
}

QLineEdit::placeholder, QTextEdit::placeholder {
    color: #94a3b8;
}

QLineEdit:hover, QComboBox:hover, QSpinBox:hover, QDoubleSpinBox:hover {
    border: 1px solid #a5b4fc;
}

QLineEdit:focus, QComboBox:focus, QSpinBox:focus,
QDoubleSpinBox:focus, QTextEdit:focus, QPlainTextEdit:focus {
    border: 2px solid #4f46e5;
    padding: 7px 11px;
}

QComboBox::drop-down {
    border: none;
    width: 26px;
    subcontrol-origin: padding;
    subcontrol-position: center right;
}

QComboBox::down-arrow {
    image: none;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 6px solid #64748b;
    width: 0px;
    height: 0px;
    margin-right: 10px;
}

QComboBox QAbstractItemView {
    background-color: #ffffff;
    border: 1px solid #d8dee9;
    border-radius: 8px;
    padding: 4px;
    outline: none;
    selection-background-color: #eef2ff;
    selection-color: #0f172a;
}

/* ---------- Casillas y opciones ---------- */
QCheckBox, QRadioButton {
    color: #334155;
    font-size: 13px;
    spacing: 9px;
    padding: 3px 0px;
}

QCheckBox::indicator, QRadioButton::indicator {
    width: 18px;
    height: 18px;
}

QCheckBox::indicator {
    border: 1px solid #cbd5e1;
    border-radius: 5px;
    background-color: #ffffff;
}

QCheckBox::indicator:hover {
    border: 1px solid #4f46e5;
    background-color: #f5f3ff;
}

QCheckBox::indicator:checked {
    background-color: #4f46e5;
    border: 1px solid #4f46e5;
    image: none;
}

QRadioButton::indicator {
    border: 2px solid #cbd5e1;
    border-radius: 10px;
    background-color: #ffffff;
}

QRadioButton::indicator:hover {
    border: 2px solid #4f46e5;
}

QRadioButton::indicator:checked {
    border: 5px solid #4f46e5;
    background-color: #ffffff;
}

/* ---------- Tabla ---------- */
QTableWidget {
    background-color: #ffffff;
    alternate-background-color: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    gridline-color: #eef2f7;
    font-size: 13px;
    color: #1e293b;
    selection-background-color: #e0e7ff;
    selection-color: #0f172a;
}

QTableWidget::item {
    padding: 7px 10px;
    border: none;
}

QTableWidget::item:selected {
    background-color: #e0e7ff;
    color: #0f172a;
}

QTableWidget::item:hover {
    background-color: #f1f5ff;
}

QHeaderView::section {
    background-color: #f1f5f9;
    color: #475569;
    padding: 10px 8px;
    border: none;
    border-bottom: 1px solid #e2e8f0;
    border-right: 1px solid #eef2f7;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
}

QHeaderView::section:hover {
    background-color: #e8edf5;
    color: #0f172a;
}

QHeaderView::section:last {
    border-right: none;
}

/* ---------- Barra de desplazamiento ---------- */
QScrollBar:vertical {
    background: transparent;
    width: 11px;
    margin: 2px;
    border: none;
}

QScrollBar::handle:vertical {
    background: #cbd5e1;
    border-radius: 5px;
    min-height: 30px;
}

QScrollBar::handle:vertical:hover {
    background: #94a3b8;
}

QScrollBar:horizontal {
    background: transparent;
    height: 11px;
    margin: 2px;
    border: none;
}

QScrollBar::handle:horizontal {
    background: #cbd5e1;
    border-radius: 5px;
    min-width: 30px;
}

QScrollBar::handle:horizontal:hover {
    background: #94a3b8;
}

QScrollBar::add-line, QScrollBar::sub-line {
    height: 0px;
    width: 0px;
    border: none;
    background: none;
}

QScrollBar::add-page, QScrollBar::sub-page {
    background: none;
}

/* ---------- Consola de reportes ---------- */
QTextEdit {
    background-color: #0f172a;
    color: #e2e8f0;
    border: 1px solid #1e293b;
    border-radius: 10px;
    font-family: "Cascadia Mono", "Consolas", "Courier New", monospace;
    font-size: 12px;
    padding: 14px;
}

QTextEdit:focus {
    border: 2px solid #6366f1;
    padding: 13px;
}

/* ---------- Diálogo ---------- */
QDialog QLabel {
    color: #475569;
    font-size: 13px;
    font-weight: 600;
}
"""


# --- DIÁLOGO PARA AGREGAR/EDITAR PRODUCTO (QDialog) ---
class FormularioProductoDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Nuevo Producto")
        self.setObjectName("dialogoProducto")
        self.setStyleSheet(ESTILO_GLOBAL)
        self.resize(380, 280)

        layout_principal = QVBoxLayout()
        layout_principal.setContentsMargins(22, 20, 22, 20)
        layout_principal.setSpacing(14)

        # Encabezado del formulario
        lbl_encabezado = QLabel("Registrar nuevo producto")
        lbl_encabezado.setObjectName("titulo")
        layout_principal.addWidget(lbl_encabezado)

        # Formulario de datos (QFormLayout)
        layout_form = QFormLayout()
        layout_form.setContentsMargins(0, 0, 0, 0)
        layout_form.setSpacing(12)
        layout_form.setLabelAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.input_nombre = QLineEdit()
        self.input_nombre.setPlaceholderText("Ej. Laptop Pro 15")

        self.combo_categoria = QComboBox()
        self.combo_categoria.addItems(
            ["Electrónica", "Ropa", "Hogar", "Accesorios"]
        )

        self.input_precio = QLineEdit()
        self.input_precio.setPlaceholderText("0.00")

        layout_form.addRow("Producto:", self.input_nombre)
        layout_form.addRow("Categoría:", self.combo_categoria)
        layout_form.addRow("Precio ($):", self.input_precio)

        layout_principal.addLayout(layout_form)

        # Estado del producto (QRadioButton)
        lbl_estado = QLabel("Estado inicial:")
        lbl_estado.setObjectName("titulo_seccion")
        layout_principal.addWidget(lbl_estado)

        box_radio = QWidget()
        layout_radio = QHBoxLayout()
        layout_radio.setContentsMargins(0, 0, 0, 0)
        layout_radio.setSpacing(18)
        self.radio_activo = QRadioButton("Disponible")
        self.radio_agotado = QRadioButton("Agotado")
        self.radio_activo.setChecked(True)
        layout_radio.addWidget(self.radio_activo)
        layout_radio.addWidget(self.radio_agotado)
        layout_radio.addStretch()
        box_radio.setLayout(layout_radio)
        layout_principal.addWidget(box_radio)

        # Botones de Acción (QHBoxLayout & QPushButton)
        layout_botones = QHBoxLayout()
        layout_botones.setSpacing(10)
        layout_botones.addStretch()

        btn_cancelar = QPushButton("Cancelar")
        btn_cancelar.setObjectName("btnCancelar")
        btn_cancelar.setCursor(Qt.PointingHandCursor)
        btn_cancelar.clicked.connect(self.reject)

        btn_guardar = QPushButton("Guardar Producto")
        btn_guardar.setObjectName("btnGuardar")
        btn_guardar.setDefault(True)
        btn_guardar.setCursor(Qt.PointingHandCursor)
        btn_guardar.clicked.connect(self.accept)

        layout_botones.addWidget(btn_cancelar)
        layout_botones.addWidget(btn_guardar)

        layout_principal.addSpacing(4)
        layout_principal.addLayout(layout_botones)
        self.setLayout(layout_principal)

    def obtener_datos(self):
        return {
            "nombre": self.input_nombre.text(),
            "categoria": self.combo_categoria.currentText(),
            "precio": self.input_precio.text(),
            "estado": (
                "Disponible"
                if self.radio_activo.isChecked()
                else "Agotado"
            ),
        }


# --- VENTANA PRINCIPAL DASHBOARD (QMainWindow) ---
class DashboardAdmin(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema Dashboard - Control de Inventario")
        self.resize(900, 600)

        # Aplicar estilos globales CSS (QSS) para una interfaz moderna
        app = QApplication.instance()
        fuente_base = QFont("Segoe UI", 10)
        if app is not None:
            app.setFont(fuente_base)
        self.setStyleSheet(ESTILO_GLOBAL)

        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        layout_principal = QVBoxLayout()
        layout_principal.setContentsMargins(20, 18, 20, 18)
        layout_principal.setSpacing(14)

        # Encabezado (QLabel)
        lbl_titulo = QLabel("Panel de Gestión e Inventario")
        lbl_titulo.setObjectName("titulo")
        layout_principal.addWidget(lbl_titulo)

        lbl_subtitulo = QLabel(
            "Administra tus productos, niveles de stock y reportes"
        )
        lbl_subtitulo.setObjectName("subtitulo")
        layout_principal.addWidget(lbl_subtitulo)

        # Sistema de Pestañas (QTabWidget)
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)

        # Pestaña 1: Productos (Tabla y Gestión)
        self.tab_productos = QWidget()
        self.configurar_tab_productos()
        self.tabs.addTab(self.tab_productos, "Inventario de Productos")

        # Pestaña 2: Reportes y Notas
        self.tab_reportes = QWidget()
        self.configurar_tab_reportes()
        self.tabs.addTab(self.tab_reportes, "Bitácora / Reportes")

        layout_principal.addWidget(self.tabs)
        widget_central.setLayout(layout_principal)

        self.statusBar().showMessage("Sistema listo")
        self.statusBar().setStyleSheet(
            "QStatusBar { background-color: #ffffff; color: #64748b;"
            " border-top: 1px solid #e2e8f0; font-size: 11px; }"
        )

    def configurar_tab_productos(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)

        # Barra de Herramientas Superior (QHBoxLayout)
        layout_herramientas = QHBoxLayout()
        layout_herramientas.setSpacing(10)

        self.input_buscar = QLineEdit()
        self.input_buscar.setPlaceholderText("Buscar producto...")
        self.input_buscar.setClearButtonEnabled(True)

        btn_nuevo = QPushButton("+ Agregar Producto")
        btn_nuevo.setObjectName("btnNuevo")
        btn_nuevo.setCursor(Qt.PointingHandCursor)
        btn_nuevo.clicked.connect(self.abrir_dialogo_nuevo)

        btn_eliminar = QPushButton("Eliminar Fila")
        btn_eliminar.setObjectName("btnEliminar")
        btn_eliminar.setCursor(Qt.PointingHandCursor)
        btn_eliminar.clicked.connect(self.eliminar_fila)

        layout_herramientas.addWidget(self.input_buscar, 1)
        layout_herramientas.addWidget(btn_nuevo)
        layout_herramientas.addWidget(btn_eliminar)

        layout.addLayout(layout_herramientas)

        # Tabla de Datos (QTableWidget)
        self.tabla_productos = QTableWidget()
        self.tabla_productos.setColumnCount(4)
        self.tabla_productos.setHorizontalHeaderLabels(
            ["Producto", "Categoría", "Precio ($)", "Estado"]
        )
        self.tabla_productos.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        self.tabla_productos.verticalHeader().setVisible(False)
        self.tabla_productos.setAlternatingRowColors(True)
        self.tabla_productos.setShowGrid(False)
        self.tabla_productos.setSelectionBehavior(
            self.tabla_productos.SelectRows
        )
        self.tabla_productos.setSelectionMode(
            self.tabla_productos.SingleSelection
        )
        self.tabla_productos.setEditTriggers(
            self.tabla_productos.NoEditTriggers
        )
        self.tabla_productos.verticalHeader().setDefaultSectionSize(40)

        # Cargar datos iniciales de prueba
        datos_prueba = [
            ("Teclado Mecánico", "Electrónica", "45.00", "Disponible"),
            ("Silla Ergonómica", "Hogar", "180.00", "Disponible"),
            ("Monitor 27''", "Electrónica", "250.00", "Agotado"),
        ]
        self.tabla_productos.setRowCount(len(datos_prueba))
        for i, fila in enumerate(datos_prueba):
            for j, val in enumerate(fila):
                item = QTableWidgetItem(val)
                if j == 2:
                    item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                elif j in (0, 3):
                    item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                else:
                    item.setTextAlignment(Qt.AlignCenter)
                self.tabla_productos.setItem(i, j, item)

        layout.addWidget(self.tabla_productos)
        self.tab_productos.setLayout(layout)

    def configurar_tab_reportes(self):
        layout = QGridLayout()
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setHorizontalSpacing(20)
        layout.setVerticalSpacing(12)

        # Izquierda: Opciones de exportación
        lbl_opciones = QLabel("Opciones de Generación de Reporte:")
        lbl_opciones.setObjectName("titulo_seccion")
        layout.addWidget(lbl_opciones, 0, 0)

        self.check_incluir_agotados = QCheckBox(
            "Incluir productos agotados"
        )
        self.check_incluir_agotados.setChecked(True)
        self.check_resumen_precios = QCheckBox("Calcular total de inventario")

        layout.addWidget(self.check_incluir_agotados, 1, 0)
        layout.addWidget(self.check_resumen_precios, 2, 0)

        btn_generar = QPushButton("Generar Resumen")
        btn_generar.setObjectName("btnNuevo")
        btn_generar.setCursor(Qt.PointingHandCursor)
        btn_generar.clicked.connect(self.generar_reporte)
        layout.addWidget(btn_generar, 3, 0, 1, 1, Qt.AlignLeft)

        # Derecha: Consola de Texto (QTextEdit)
        lbl_vista = QLabel("Vista Previa del Reporte:")
        lbl_vista.setObjectName("titulo_seccion")
        layout.addWidget(lbl_vista, 0, 1)
        self.txt_reporte = QTextEdit()
        self.txt_reporte.setReadOnly(True)
        self.txt_reporte.setPlaceholderText(
            "Haga clic en 'Generar Resumen' para ver el informe aquí..."
        )
        layout.addWidget(self.txt_reporte, 1, 1, 3, 1)

        layout.setColumnStretch(0, 0)
        layout.setColumnStretch(1, 1)
        self.tab_reportes.setLayout(layout)

    # --- LÓGICA DE LA APLICACIÓN ---
    def abrir_dialogo_nuevo(self):
        dialogo = FormularioProductoDialog(self)
        if dialogo.exec_() == QDialog.Accepted:
            datos = dialogo.obtener_datos()
            row = self.tabla_productos.rowCount()
            self.tabla_productos.insertRow(row)
            item_nombre = QTableWidgetItem(datos["nombre"])
            item_categoria = QTableWidgetItem(datos["categoria"])
            item_precio = QTableWidgetItem(datos["precio"])
            item_estado = QTableWidgetItem(datos["estado"])

            item_categoria.setTextAlignment(Qt.AlignCenter)
            item_precio.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

            self.tabla_productos.setItem(row, 0, item_nombre)
            self.tabla_productos.setItem(row, 1, item_categoria)
            self.tabla_productos.setItem(row, 2, item_precio)
            self.tabla_productos.setItem(row, 3, item_estado)

    def eliminar_fila(self):
        row = self.tabla_productos.currentRow()
        if row >= 0:
            self.tabla_productos.removeRow(row)

    def generar_reporte(self):
        filas = self.tabla_productos.rowCount()
        total_items = 0
        suma_precios = 0.0

        texto_reporte = "=== REPORTE DE INVENTARIO ===\n\n"

        for row in range(filas):
            item_nombre = self.tabla_productos.item(row, 0)
            item_categoria = self.tabla_productos.item(row, 1)
            item_precio = self.tabla_productos.item(row, 2)
            item_estado = self.tabla_productos.item(row, 3)

            nombre = item_nombre.text() if item_nombre else ""
            categoria = item_categoria.text() if item_categoria else ""
            precio_str = item_precio.text() if item_precio else ""
            estado = item_estado.text() if item_estado else ""

            if not self.check_incluir_agotados.isChecked() and estado == "Agotado":
                continue

            try:
                precio = float(precio_str)
            except ValueError:
                precio = 0.0

            suma_precios += precio
            total_items += 1
            texto_reporte += f"• [{categoria}] {nombre} - ${precio:.2f} ({estado})\n"

        texto_reporte += f"\nTotal de registros procesados: {total_items}\n"

        if self.check_resumen_precios.isChecked():
            texto_reporte += f"Valor total acumulado: ${suma_precios:.2f}\n"

        self.txt_reporte.setText(texto_reporte)


# --- EJECUCIÓN DEL PROGRAMA ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setFont(QFont("Segoe UI", 10))
    ventana = DashboardAdmin()
    ventana.show()
    sys.exit(app.exec_())