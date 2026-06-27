from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QToolButton,
)

from PySide6.QtCore import Qt, Signal
import qtawesome as qta


class Header(QFrame):

    # Señal que enviará la URL al MainWindow
    buscarSolicitado = Signal(str)

    def __init__(self):
        super().__init__()

        self.setObjectName("header")

        layout = QHBoxLayout(self)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(18)

        # =======================
        # Buscador
        # =======================

        buscador = QHBoxLayout()
        buscador.setSpacing(0)

        self.url = QLineEdit()
        self.url.setObjectName("urlInput")
        self.url.setPlaceholderText("Pega la URL del manga aquí...")

        self.buscar = QPushButton(" Buscar")
        self.buscar.setObjectName("searchButton")
        self.buscar.setFixedWidth(170)
        self.buscar.setIcon(
            qta.icon("fa6s.magnifying-glass", color="black")
        )

        self.buscar.clicked.connect(self.buscar_manga)

        buscador.addWidget(self.url)
        buscador.addWidget(self.buscar)

        layout.addLayout(buscador, 1)

        # =======================
        # Menú superior
        # =======================

        menu = QHBoxLayout()
        menu.setSpacing(15)

        ajustes = QToolButton()
        ajustes.setObjectName("topButton")
        ajustes.setText(" Ajustes")
        ajustes.setIcon(qta.icon("fa6s.gear", color="white"))
        ajustes.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        tema = QToolButton()
        tema.setObjectName("topButton")
        tema.setText(" Tema")
        tema.setIcon(qta.icon("fa6s.moon", color="white"))
        tema.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        acerca = QToolButton()
        acerca.setObjectName("topButton")
        acerca.setText(" Acerca de")
        acerca.setIcon(qta.icon("fa6s.circle-info", color="white"))
        acerca.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        menu.addWidget(ajustes)
        menu.addWidget(tema)
        menu.addWidget(acerca)

        layout.addLayout(menu)

    def buscar_manga(self):

        url = self.url.text().strip()

        if not url:
            print("No se ingresó ninguna URL.")
            return

        # Enviar la URL al MainWindow
        self.buscarSolicitado.emit(url)