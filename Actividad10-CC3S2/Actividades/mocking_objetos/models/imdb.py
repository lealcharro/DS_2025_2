"""
Acceso a la base de datos de películas de Internet Movie Database
Implementa las APIs SearchTitle, Reviews y Ratings
"""

import logging
from typing import Any, Dict

import requests

import os, urllib.parse
ALLOWED_HOSTS = {"imdb-api.com"}
TIMEOUT = float(os.getenv("HTTP_TIMEOUT", "2.0"))

logger = logging.getLogger(__name__)


def _enforce_policies(url: str):
    host = urllib.parse.urlparse(url).hostname
    if host not in ALLOWED_HOSTS:
        raise ValueError(f"Host no permitido: {host}")
    if not url.startswith("https://"):
        raise ValueError("Se requiere HTTPS")


class IMDb:
    """Acceso a la base de datos de películas de Internet Movie Database"""

    def __init__(self, apikey: str, http_client=None):
        self.apikey = apikey
        self.http = http_client or requests

    def search_titles(self, title: str) -> Dict[str, Any]:
        """Busca una película por título"""
        url = f"https://imdb-api.com/API/SearchTitle/{self.apikey}/{title}"
        logger.info("Buscando en IMDb el título: %s", title)
        r = self.http.get(url, timeout=TIMEOUT)
        return r.json() if r.status_code == 200 else {}

    def movie_reviews(self, imdb_id: str) -> Dict[str, Any]:
        """Obtiene reseñas para una película"""
        url = f"https://imdb-api.com/API/Reviews/{self.apikey}/{imdb_id}"
        logger.info("Buscando en IMDb las reseñas: %s", imdb_id)
        r = self.http.get(url, timeout=TIMEOUT)
        return r.json() if r.status_code == 200 else {}

    def movie_ratings(self, imdb_id: str) -> Dict[str, Any]:
        """Obtiene calificaciones para una película"""
        url = f"https://imdb-api.com/API/Ratings/{self.apikey}/{imdb_id}"
        _enforce_policies(url)
        r = self.http.get(url, timeout=TIMEOUT)
        return r.json() if r.status_code == 200 else {}
