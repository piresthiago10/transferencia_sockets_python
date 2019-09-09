# Transferência via Sockets

Sistema simples de transferência de um único arquivo ou uma lista deles via rede usando a biblioteca socket do python.

## Requisitos do sistema:
- Python v3.7+;
- Somente as extensões JPG, MP4 podem ser enviadas através desse aplicativo;
- Os arquivos devem ser informados com seu diretório completo: /home/usuario/imagens/nome_arquivo.jpg;
- Sistema controlado via linha de comando;

## Exemplo de imagem do sistema:
![Exemplo de imagem do sistema](https://piresthiago.com.br/minhas_imagens/socketspython.png)

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
ou
```
sudo apt install python.pip
```
4. Instale o ambiente virtual do Python
```
sudo apt-get install python3-venv
```
5. Vá até o diretório do projeto
6. Crie uma ambiente virtual
```
python3 -m venv <nome_da_venv>
```
7. Ative o ambiente virtual
```
source <nome_da_venv>/bin/activate
```
8. Instale os requerimentos do sistema
```
pip install -r requirements.txt
```
9. Execute o server_side.py
```
python3.7 server_side.py
```
O Server Side irá emitir uma mensagem de espera pelo Client Side.

10. Abra um novo terminal e repita os passos 5 e 7 e Execute o client_side.py
```
python3.7 clint_side.py
```
Irá aparecer um Menu para interagir com o sitema, ele é bem intuitivo!

## Testes e validação do código:

Não há muitos testes desenvolvidos para esse código, mas por motivos didáticos existe um teste automatizado que é executado junto das validações de código pycodestyle e pylint. Para executá-los basta estar no diretório do base do projeto e executar o seginte comando:

```
./automaizado.sh
```
