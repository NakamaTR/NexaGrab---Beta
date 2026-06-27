from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QFrame,
    QLabel
)

from src.widgets.sidebar import Sidebar
from src.widgets.header import Header
from src.widgets.manga_card import MangaCard
from src.widgets.chapter_table import ChapterTable
from src.scraper.manga_scraper import MangaScraper


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("NexaGrab Beta")
        self.resize(1500, 900)

        self.scraper = MangaScraper()

        central = QWidget()
        self.setCentralWidget(central)

        root = QHBoxLayout(central)
        root.setContentsMargins(15, 15, 15, 15)
        root.setSpacing(15)

        self.sidebar = Sidebar()
        root.addWidget(self.sidebar)

        right = QVBoxLayout()
        right.setSpacing(15)

        self.header = Header()
        self.header.buscarSolicitado.connect(self.buscar_manga)
        right.addWidget(self.header)

        top = QHBoxLayout()
        top.setSpacing(15)

        self.manga = MangaCard()
        top.addWidget(self.manga, 2)

        self.detalles = QFrame()
        self.detalles.setObjectName("content")

        detalles_layout = QVBoxLayout(self.detalles)
        detalles_layout.setContentsMargins(20, 20, 20, 20)
        detalles_layout.setSpacing(10)

        self.titulo = QLabel("Detalles del manga")
        self.titulo.setObjectName("title")

        self.autor = QLabel("👤 Autor: ---")
        self.autor.setObjectName("infoLabel")

        self.estado = QLabel("📌 Estado: ---")
        self.estado.setObjectName("infoLabel")

        self.generos = QLabel("🏷 Géneros: ---")
        self.generos.setObjectName("infoLabel")

        self.sinopsis = QLabel(
            "Aquí aparecerá la descripción del manga cuando pulses Buscar."
        )
        self.sinopsis.setWordWrap(True)
        self.sinopsis.setObjectName("infoLabel")

        detalles_layout.addWidget(self.titulo)
        detalles_layout.addSpacing(10)
        detalles_layout.addWidget(self.autor)
        detalles_layout.addWidget(self.estado)
        detalles_layout.addWidget(self.generos)
        detalles_layout.addSpacing(15)
        detalles_layout.addWidget(self.sinopsis)
        detalles_layout.addStretch()

        top.addWidget(self.detalles, 1)
        right.addLayout(top)

        self.tabla = ChapterTable()
        right.addWidget(self.tabla, 2)

        self.barra = QFrame()
        self.barra.setObjectName("content")

        barra_layout = QVBoxLayout(self.barra)
        barra_layout.setContentsMargins(20, 15, 20, 15)

        barra_titulo = QLabel("Barra de descarga")
        barra_titulo.setObjectName("title")
        barra_layout.addWidget(barra_titulo)

        right.addWidget(self.barra)

        root.addLayout(right, 1)

    def buscar_manga(self, url):

        try:
            datos = self.scraper.obtener_info(url)

            self.manga.actualizar(datos)

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
                f"🏷 Géneros: {generos if generos else 'Sin géneros'}"
            )

            self.sinopsis.setText(
                datos.get("sinopsis", "Sin sinopsis.")
            )

            self.tabla.actualizar(
                datos.get("capitulos", [])
            )

            print(datos)

        except Exception as e:
            print("ERROR:", e)
