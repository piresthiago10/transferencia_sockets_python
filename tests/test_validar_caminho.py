import socket
import pathlib
import sys
import os

extensions = ['.jpg', '.JPG', '.jpeg', '.JPEG', '.mp4', '.MP4']

# insira aqui os diretórios de algumas imagens que estão em seu computador
lista_arquivos = ['C:/Users/thiag/OneDrive/Imagens/diagrama.jpg', 'C:/Users/thiag/OneDrive/Imagens/passaro.jpg', "C:/Users/thiag/OneDrive/Imagens/cavaleiro.jpg"]

def validar_caminho(caminho_arquivo):

    extensao = pathlib.Path(caminho_arquivo).suffix
    caminho = os.path.isfile(caminho_arquivo)

    if caminho_arquivo in lista_arquivos:
        print("O arquivo já está inserido na lista!")

    if caminho and extensao in extensions:
        return caminho_arquivo
    else:
        print("O caminho ou arquivo não válido(s)!")

# testa se o arquivo está de acordo com as exigências
def test_caminho_valido():
    caminho_arquivo = "C:/Users/thiag/OneDrive/Imagens/cpf.jpg"
    assert validar_caminho(caminho_arquivo) == caminho_arquivo

# testa se a extensão do arquivo consta na lista de extensões permitidas
def test_caminho_invalido():
    caminho_arquivo = "C:/Users/thiag/OneDrive/Imagens/diagrama.jpgf"
    assert validar_caminho(caminho_arquivo) == print("O caminho ou arquivo não válido(s)!")