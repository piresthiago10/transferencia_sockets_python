#!/bin/bash
echo "Olá:" whoami

echo "Executando testes automatizados"
py.test ./tests/test_validar_caminho.py

echo "Executando pycodestyle em client_side.py"
pycodestyle client_side.py

echo "Executando pycodestyle em server_side.py"
pycodestyle server_side.py

echo "Executando pylint em client_side.py"
pylint client_side.py

echo "Executando pylint em server_side.py"
pylint server_side.py
