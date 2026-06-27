from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QPushButton,
    QVBoxLayout
)

from PySide6.QtCore import Qt
import qtawesome as qta


class Sidebar(QFrame):

    def __init__(self):
        super().__init__()

        self.setObjectName("sidebar")
        self.setFixedWidth(250)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

        # ==========================
        # LOGO
        # ==========================

        icono = QLabel()
        icono.setPixmap(
            qta.icon(
                "fa6s.book-open",
                color="#E39700"
            ).pixmap(70, 70)
        )
        icono.setAlignment(Qt.AlignCenter)

        layout.addWidget(icono)

        logo = QLabel("NEXAGRAB")
        logo.setObjectName("logo")
        logo.setAlignment(Qt.AlignCenter)

        layout.addWidget(logo)

        version = QLabel("BETA")
        version.setAlignment(Qt.AlignCenter)
        version.setObjectName("version")

        layout.addWidget(version)

        layout.addSpacing(30)

        # ==========================
        # BOTONES
        # ==========================

        botones = [

            ("fa6s.house", "Inicio"),

            ("fa6s.book-open", "Biblioteca"),

            ("fa6s.download", "Descargas"),

            ("fa6s.clock-rotate-left", "Historial"),

            ("fa6s.gear", "Configuración")

        ]

        for i, (icono_nombre, texto) in enumerate(botones):

            boton = QPushButton(texto)

            boton.setObjectName("menuButton")

            boton.setIcon(
                qta.icon(
                    icono_nombre,
                    color="#EAEAEA"
                )
            )

            boton.setCursor(Qt.PointingHandCursor)

            boton.setMinimumHeight(50)

            if i == 0:
                boton.setProperty("active", True)

            layout.addWidget(boton)

        layout.addStretch()

        # ==========================
        # ESTADO
        # ==========================

        estado = QLabel()

        estado.setObjectName("status")

        estado.setAlignment(Qt.AlignCenter)

        estado.setText(
            "🟢 Conectado\n\nv0.1 Beta"
        )

        layout.addWidget(estado)