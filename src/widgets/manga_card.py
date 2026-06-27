from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
import qtawesome as qta


class MangaCard(QFrame):

    def __init__(self):
        super().__init__()

        self.setObjectName("mangaCard")

        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(25)

        # ==========================
        # PORTADA
        # ==========================

        self.portada = QLabel()

        pixmap = QPixmap("assets/images/solo_leveling.jpg")

        pixmap = pixmap.scaled(
            210,
            300,
            Qt.KeepAspectRatioByExpanding,
            Qt.SmoothTransformation
        )

        self.portada.setPixmap(pixmap)
        self.portada.setFixedSize(210, 300)
        self.portada.setScaledContents(True)
        self.portada.setObjectName("cover")

        layout.addWidget(self.portada)

        # ==========================
        # INFORMACIÓN
        # ==========================

        info = QVBoxLayout()
        info.setSpacing(12)

        self.titulo = QLabel("Solo Leveling")
        self.titulo.setObjectName("mangaTitle")

        self.rating = QLabel("★★★★★ 9.8")
        self.rating.setObjectName("rating")

        self.autor = QLabel("👤 Autor: Chugong")
        self.autor.setObjectName("infoLabel")

        self.estado = QLabel("📌 Estado: Finalizado")
        self.estado.setObjectName("infoLabel")

        self.capitulos = QLabel("📚 Capítulos: 200")
        self.capitulos.setObjectName("infoLabel")

        self.generos = QLabel(
            "Acción • Fantasía • Aventura • Fantasía Oscura"
        )
        self.generos.setWordWrap(True)
        self.generos.setObjectName("infoLabel")

        self.sinopsis = QLabel(
            "Hace más de una década aparecieron misteriosas mazmorras..."
        )
        self.sinopsis.setWordWrap(True)
        self.sinopsis.setObjectName("synopsis")

        # ==========================
        # BOTONES
        # ==========================

        botones = QHBoxLayout()

        self.descargar = QPushButton(" Agregar a descargas")
        self.descargar.setObjectName("goldButton")
        self.descargar.setIcon(
            qta.icon("fa6s.download", color="black")
        )

        self.biblioteca = QPushButton(" Agregar a biblioteca")
        self.biblioteca.setObjectName("darkButton")
        self.biblioteca.setIcon(
            qta.icon("fa6s.bookmark", color="white")
        )

        botones.addWidget(self.descargar)
        botones.addWidget(self.biblioteca)

        info.addWidget(self.titulo)
        info.addWidget(self.rating)
        info.addSpacing(8)
        info.addWidget(self.autor)
        info.addWidget(self.estado)
        info.addWidget(self.capitulos)
        info.addWidget(self.generos)
        info.addSpacing(12)
        info.addWidget(self.sinopsis)
        info.addSpacing(12)
        info.addLayout(botones)
        info.addStretch()

        layout.addLayout(info)

    # ===================================
    # ACTUALIZAR INFORMACIÓN DEL MANGA
    # ===================================

    def actualizar(self, datos):

        self.titulo.setText(
            datos.get("titulo", "Sin título")
        )

        self.autor.setText(
            f"👤 Autor: {datos.get('autor', 'Desconocido')}"
        )

        self.estado.setText(
            f"📌 Estado: {datos.get('estado', 'Desconocido')}"
        )

        generos = datos.get("generos", [])

        if isinstance(generos, list):
            generos = " • ".join(generos)

        self.generos.setText(
            f"🏷 {generos if generos else 'Sin géneros'}"
        )

        self.capitulos.setText(
            f"📚 Capítulos: {len(datos.get('capitulos', []))}"
        )

        self.sinopsis.setText(
            datos.get("sinopsis", "Sin sinopsis.")
        )