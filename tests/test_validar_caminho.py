import socket
import pathlib
import sys
import os

extensions = ['.jpg', '.JPG', '.jpeg', '.JPEG', '.mp4', '.MP4']

# insira aqui os diretórios de algumas imagens que estão em seu computador
lista_arquivos = ['/image_sample/cachorro.jpg']

def validar_caminho(caminho_arquivo):

    extensao = pathlib.Path(caminho_arquivo).suffix
    caminho = os.path.isfile(caminho_arquivo)

    if caminho and extensao in extensions:
        return caminho_arquivo
    else:
        print("O caminho ou arquivo não válido(s)!")

# testa se o arquivo está de acordo com as exigências
def test_caminho_valido():
    caminho_arquivo = "/image_sample/cachorro.jpg"
    assert validar_caminho(caminho_arquivo) == caminho_arquivo

# testa se a extensão do arquivo consta na lista de extensões permitidas
def test_caminho_invalido():
    caminho_arquivo = "/image_sample/cachorro.jpgg"
    assert validar_caminho(caminho_arquivo) == print("O caminho ou arquivo não válido(s)!")