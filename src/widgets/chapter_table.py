from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel,
    QTableWidget,
    QHeaderView,
    QTableWidgetItem
)

from PySide6.QtCore import Qt


class ChapterTable(QFrame):

    def __init__(self):
        super().__init__()

        self.setObjectName("chapterTable")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20,20,20,20)
        layout.setSpacing(15)

        titulo = QLabel("Capítulos disponibles")
        titulo.setObjectName("chapterTitle")

        layout.addWidget(titulo)

        self.table = QTableWidget()

        self.table.setColumnCount(2)

        self.table.setHorizontalHeaderLabels([
            "Capítulo",
            "Estado"
        ])

        self.table.horizontalHeader().setStretchLastSection(True)

        self.table.horizontalHeader().setSectionResizeMode(
            0,
            QHeaderView.ResizeToContents
        )

        self.table.verticalHeader().hide()

        self.table.setAlternatingRowColors(True)

        self.table.setSelectionBehavior(
            QTableWidget.SelectRows
        )

        self.table.setEditTriggers(
            QTableWidget.NoEditTriggers
        )

        self.table.setRowCount(20)

        for i in range(20):

            self.table.setItem(
                i,
                0,
                QTableWidgetItem(f"Capítulo {i+1}")
            )

            self.table.setItem(
                i,
                1,
                QTableWidgetItem("Pendiente")
            )

        layout.addWidget(self.table)