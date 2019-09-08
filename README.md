# Transferência Sockets

Sistema simples de transferência de um único arquivo ou uma lista deles via rede usando a biblioteca socket do python.

## Requisitos do sistema:
- Python v3.7+, usando a biblioteca socket do python.
- Somente as extensões JPG, MP4 podem ser enviadas através desse aplicativo.
- Sistema controlado via linha de comando. 
- Testes automatizados. 
- Validação por PyCodestyle (PEP8) e Pylint.

## Preparando o ambiente (Linux - Ubuntu):

### Após baixar ou clonar o projeto abra o Terminal e faça o seguinte:

1. Atualize o apt
```
sudo apt upgrade
```
2. Instale o Python3.7 (caso não o tenha)
```
sudo apt-install python3.7
```
3. Instale o pip:
```
sudo python get-pip.py
```
4. Instale o ambiente virtual do Python
```
sudo apt-get install python3-venv
```
5. Vá até o diretório do projeto
6. Crie uma ambiente virtual
```
python36 -m venv <nome_da_venv>
```
7. Ative o ambiente virtual
```
source <nome_da_venv>/bin/activate
```
8. Instale os requerimentos do sistema
```
pip install -r requirements.txt
```
