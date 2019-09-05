
'''
Criar a lista para armazenar o caminho dos arquivos; ok


Verificar se o arquivo tem o caminho válido; ok

Exibir a lista de arquivos:
    -> Adicionar arquivo na lista;
    -> Alterar elemento da lista;
    -> Excluir arquivo da lista;
    -> Limpar lista.
    -> Trasnferir arquivo(s)

Criar uma nova pasta e mover os arquivos;
'''

import socket
import pathlib
import os

class ClientServerSide():

    #extensões permitidas
    extensions = ['.jpg', '.JPG', '.jpeg', '.JPEG', '.mp4', '.MP4']
    lista_arquivos = []

    def connect_server(self):
        host = socket.gethostname()
        port = 57000
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        return print(f"Conexão com o {host} foi estabelecida!")

    # listagem dos caminhos dos arquivos
    def enumerar_lista(self):

        print("ID  - Caminho")

        for index, item in enumerate(self.lista_arquivos):
            print(f"[{index}] - {item}")

    # validação do arquivo na lista
    def validar_caminho(self, caminho_arquivo):

        # verifica o arquivo já foi inserido na lista
        if caminho_arquivo in self.lista_arquivos:
            print("O arquivo já está inserido na lista!")
            return self.menu()
        # verifica se o caminho e a extensão são válidos
        elif os.path.isfile(caminho_arquivo) and pathlib.Path(caminho_arquivo).suffix in self.extensions:
            return caminho_arquivo
        else:
            print("O caminho ou arquivo não válido(s)!")
            return self.menu()

    # inserir caminhos de arquivos na lista
    def inserir_arquivo(self):

        arquivo = input("Insira o caminho para o arquivo:")

        self.validar_caminho(arquivo)

        #insere o arquivo na lista
        self.lista_arquivos.append(arquivo)  
   

        return self.menu()     

    def alterar_lista(self):

        id_arquivo = int(input("Selecione o ID do arquivo a ser alterado:"))
        self.enumerar_lista

        # verifica se há o índice na lista
        try:
            if self.lista_arquivos[id_arquivo]:
                arquivo = input("Insira o caminho para o arquivo:")
                self.validar_caminho(arquivo)
                self.lista_arquivos[id_arquivo] = arquivo
        except:
            print("Não existe o ID na lista.")
            self.menu()

    def excluir_item_lista(self):
        pass

    def delete_list(self):
        pass

    def transfer_files(self):
        pass

    def menu(self): # metodo principal

        self.enumerar_lista()
        
        print("Escolha uma opção: \n 1 - ADICIONAR ARQUIVO NA LISTA; \n 2 - ALTERAR ARQUIVO DA LISTA; \n 3 - EXCLUIR ARQUIVO DA LISTA; \n 4 - LIMPAR A LISTA; \n 5 - TRANSFERIR ARQUIVOS; \n 6 - SAIR")
        option = input("Digite a sua opção:")

        if option == '1':
            self.inserir_arquivo()
        elif option == '2':
            self.alterar_lista()
        else:
            print("Opção inválida")
            self.menu()


CS = ClientServerSide()
CS.connect_server()
CS.menu()