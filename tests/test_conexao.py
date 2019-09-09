import socket


def connect_server_servidor(host, port):

    try:
        serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversock.bind((host, port))
        serversock.listen(5)
        conn, address = serversock.accept()
        print(f"Conexão estabelecida com {address}")
        return conn
    except ConnectionError:
        print("Não foi possível conectar ao seu cliente.")

def connect_server_cliente(host, port):

    try:
        serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversock.connect((host, port))
        print(f"Conexão estabelecida com {host} na porta {port}")
        return serversock
    except ConnectionError:
        print("Não foi possível conectar ao seu cliente.")

def test_conexao_servidor():
    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversock.bind((socket.gethostname(), 9000))
    serversock.listen(5)
    conn, address = serversock.accept()
    assert connect_server_servidor(socket.gethostname(), 9000) == conn

def test_conexao_cliente():
    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversock.connect((socket.gethostname(), 9000))
    return serversock
    assert connect_server_cliente(socket.gethostname(), 9000) == serversock


