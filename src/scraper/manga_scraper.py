import requests
from bs4 import BeautifulSoup


class MangaScraper:

    def obtener_info(self, url):

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/137.0 Safari/537.36"
            )
        }

        respuesta = requests.get(
            url,
            headers=headers,
            timeout=20
        )

        respuesta.raise_for_status()

        soup = BeautifulSoup(respuesta.text, "lxml")

        # ==========================
        # TÍTULO
        # ==========================

        titulo = ""

        titulo_tag = soup.select_one("h1")

        if titulo_tag:
            titulo = titulo_tag.get_text(strip=True)

        # ==========================
        # PORTADA
        # ==========================

        portada = ""

        portada_tag = soup.select_one(".summary_image img")

        if portada_tag:
            portada = (
                portada_tag.get("data-src")
                or portada_tag.get("src")
                or ""
            )

        # ==========================
        # CAPÍTULOS
        # ==========================

        capitulos = []

        for cap in soup.select("li.wp-manga-chapter"):

            enlace = cap.find("a")

            if enlace:

                capitulos.append({

                    "nombre": enlace.get_text(strip=True),

                    "url": enlace.get("href", "")

                })

        # ==========================
        # DATOS
        # ==========================

        datos = {

            "titulo": titulo,

            "autor": "Desconocido",

            "estado": "Desconocido",

            "generos": [],

            "sinopsis": "",

            "portada": portada,

            "capitulos": capitulos

        }

        return datos