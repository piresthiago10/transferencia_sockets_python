'''
TRANSFERENCIA DE SOCKETS COM PYTHON
Desenvolvedor: Thiago Pires
GitHub: https://github.com/piresthiago10
'''

import socket
import pathlib
import sys
import os


class ClientSide():

    ''' Classe responsável por realizar a comunicação no sentido
    cliente - servidor.

    Contém os atributos: host e port os quais precisam estar
    com seus valores em conformidade com os do arquivo server_side.py

    '''

    # extensões permitidas
    extensions = ['.jpg', '.JPG', '.jpeg', '.JPEG', '.mp4', '.MP4']
    lista_arquivos = []

    host = socket.gethostname()
    port = 9000

    def connect_server(self):

        ''' Método responsável por realizar a conexão entre cliente - servidor.

        Parametros:
        Nenhum

        Retorno:
        socket: Serversock

        '''

        try:
            serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serversock.connect((self.host, self.port))
            print(f"Conexão estabelecida com {self.host} na porta {self.port}")
            return serversock
        except ConnectionError:
            print("Não foi possível conectar ao seu cliente.")
            sys.exit()

    def enumerar_lista(self):

        ''' Método responsável por enumerar a lista com os diretórios
        de arquivos para serem enviados ao servidor

        Parametros:
        Nenhum

        Retorno:
        Nenhum

        '''

        print("ID  - Caminho")

        for index, item in enumerate(self.lista_arquivos):
            print(f"[{index}] - {item}")

    def validar_caminho(self, caminho_arquivo):

        ''' Método responsável por validar o arquivo na lista;
        verificar se o arquivo já foi inserido na lista
        e verifica se o caminho e a extensão são válidos.

        Parametros:
        str: caminho_arquivo

        Retorno:
        str: caminho_arquivo

        '''

        extensao = pathlib.Path(caminho_arquivo).suffix
        caminho = os.path.isfile(caminho_arquivo)

        if caminho_arquivo in self.lista_arquivos:
            print("O arquivo já está inserido na lista!")
            return self.menu()
        elif caminho and extensao in self.extensions:
            return caminho_arquivo
        else:
            print("O caminho ou arquivo não válido(s)!")
            return self.menu()

    def inserir_arquivo(self):

        ''' Método responsável por inserir os caminhos dos arquivos na lista

        Parametros:
        Nenhum

        Retorno:
        Nenhum

        '''

        arquivo = input("Insira o caminho para o arquivo:")
        self.validar_caminho(arquivo)
        self.lista_arquivos.append(arquivo)
        self.menu()

    def alterar_lista(self):

        ''' Método responsável por inserir os caminhos dos arquivos na lista

        Parametros:
        Nenhum

        Retorno:
        Nenhum

        '''

        id_arquivo = input("Selecione o ID do arquivo a ser alterado:")
        self.enumerar_lista()

        if id_arquivo.isdigit():
            int_ind_artigo = int(id_arquivo)
        else:
            print("Opção inválida.")
            self.menu()

        # verifica se há o índice na lista
        if len(self.lista_arquivos) > int_ind_artigo:
            if self.lista_arquivos[int_ind_artigo]:
                arquivo = input("Insira o caminho para o arquivo:")
                self.validar_caminho(arquivo)
                self.lista_arquivos[int_ind_artigo] = arquivo
        else:
            print("Não existe o ID na lista.")
            self.menu()

    def excluir_item_lista(self):

        ''' Método responsável por excluir um arquivo da lista de arquivos

        Parametros:
        Nenhum

        Retorno:
        Nenhum

        '''

        id_arquivo = input("Selecione o ID do arquivo a ser excluido:")
        self.enumerar_lista()

        if id_arquivo.isdigit():
            int_ind_artigo = int(id_arquivo)
        else:
            print("Opção inválida.")
            self.menu()

        # verifica se há o índice na lista
        if len(self.lista_arquivos) > int_ind_artigo:
            if self.lista_arquivos[int_ind_artigo]:
                del self.lista_arquivos[int_ind_artigo]
                print("Arquivo excluido!")
                self.menu()
        else:
            print("Não existe o ID na lista.")
            self.menu()

    def excluir_lista(self):

        ''' Método responsável por excluir toda a lista de arquivos

        Parametros:
        Nenhum

        Retorno:
        Método: menu()

        '''

        self.lista_arquivos.clear()

        return self.menu()

    def transferir_arquivos(self, arquivo):

        ''' Método responsável por transferir os arquivos enviados
        pelo cliente para o servidor e emitir mensagens informando
        o andamento do processo de envio de dados e do próprio
        arquivo em si.

        Parametros:
        str: arquivo

        Retorno:
        Nenhum

        '''
        serversock = self.connect_server()

        nome_arquivo = os.path.basename(arquivo)
        serversock.send(nome_arquivo.encode('utf-8'))

        retorno_srv = serversock.recv(128).decode()
        if retorno_srv == nome_arquivo:
            print('SUCESSO: Servidor recebeu o nome do arquivo correto.')
        else:
            print(f'ERRO: Resposta do servidor diferente do nome do arquivo:')
            print(retorno_srv)

        print(f'Enviando o arquivo: {nome_arquivo}')
        with open(arquivo, 'rb') as midia:
            serversock.send(midia.read())
            serversock.close()
        print('Arquivo enviado')

    # metodo principal
    def menu(self):

        ''' Método responsável por exibir um menu para o usuário da
        aplicação

        Parametros:
        Nenhum

        Retorno:
        Nenhum

        '''

        self.enumerar_lista()

        print("Escolha uma opção:")
        print("1 - ADICIONAR ARQUIVO NA LISTA;")
        print("2 - ALTERAR ARQUIVO DA LISTA;")
        print("3 - EXCLUIR ARQUIVO DA LISTA;")
        print("4 - LIMPAR A LISTA;")
        print("5 - TRANSFERIR ARQUIVOS;")
        print("6 - SAIR.")

        option = input("Digite a sua opção:")

        if option == '1':
            self.inserir_arquivo()
        elif option == '2':
            self.alterar_lista()
        elif option == '3':
            self.excluir_item_lista()
        elif option == '4':
            self.excluir_lista()
        elif option == '5':
            while True:
                for arquivo in self.lista_arquivos:
                    self.transferir_arquivos(arquivo)
                break
            self.excluir_lista()
        elif option == '6':
            sys.exit()
        else:
            print("Opção inválida")
            self.menu()


CS = ClientSide()
CS.menu()
