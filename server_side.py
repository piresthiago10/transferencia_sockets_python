'''
TRANSFERENCIA DE SOCKETS COM PYTHON
Desenvolvedor: Thiago Pires
GitHub: https://github.com/piresthiago10
'''

import socket
import sys


class ServerSide():

    ''' Classe responsável por realizar a comunicação no sentido
    servidor - cliente.

    Contém os atributos: host e port os quais precisam estar com
    seus valores em conformidade com os do arquivo client_side.py

    '''

    host = socket.gethostname()
    port = 9000

    def connect_server(self):

        ''' Método responsável por realizar a conexão entre servidor - cliente.
        Imprime no terminal uma mensagem informando se a conexão foi bem
        sucedida ou não.

        Parametros:
        Nenhum

        Retorno:
        socket: Serversock

        '''

        try:
            serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serversock.bind((self.host, self.port))
            serversock.listen(5)
            conn, address = serversock.accept()
            print(f"Conexão estabelecida com {address}")
            return conn
        except ConnectionError:
            print("Não foi possível conectar ao seu cliente.")
            sys.exit()

    def recebe_arquivos(self):

        ''' Método responsável por receber os arquivos enviados
        pelo cliente para o servidor e emitir mensagens informando
        o andamento do processo do recebimento de dados e do próprio
        arquivo em si.

        Parametros:
        Nenhum

        Retorno:
        Nenhum

        '''

        print("Aguardando ação do cliente...")

        while True:
            try:
                conn = self.connect_server()
                print("Recebendo dados...")
                dados = conn.recv(128)
                nome_arquivo = dados.decode('utf-8')
                conn.send(dados)
                with open(nome_arquivo, 'wb') as midia:
                    print("Mídia aberta")
                    print('Recebendo arquivo...')
                    data = conn.recv(40000000)
                    midia.write(data)
                    print(data)
                    print("Mídia enviada")
                    midia.close()
                    print("Transferência Completa!")
                    conn.close()
                    print("Conexão encerrada.")
            except ConnectionError:
                print('Conexão com o servidor foi encerrada.')
                break


SS = ServerSide()
SS.recebe_arquivos()
