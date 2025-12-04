"""
Pacote de automação para download de certificados SSL.

Autor: Renata Hollanda
Data: Dezembro/2025
"""

__version__ = "1.0.0"
__author__ = "Renata Hollanda"

from .download_certs import download_certificado, ler_arquivo_dicionario, main

__all__ = ["download_certificado", "ler_arquivo_dicionario", "main"]
