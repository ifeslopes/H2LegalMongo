from conexion.oracle_queries import OracleQueries
from reports.relatoriosmogo import Relatorio

class RelatorioMenu:
    def __init__(self):
        self.relatorio = Relatorio()
   

    def get_relatorio_usuario(self):
        # Cria uma nova conexão com o banco que permite alteração
      
        # Recupera os dados transformando em um DataFrame
        self.relatorio.get_relatorio_usuario()
      
        input("Pressione Enter para Sair do Relatório de Usuarios")
    
    def get_relatorio_perfil(self):
        # Cria uma nova conexão com o banco que permite alteração
        self.relatorio.get_relatorio_perfil()
     
        input("Pressione Enter para Sair do Relatório de Perfils")

    def get_relatorio_perfil_usuario(self):
        # Cria uma nova conexão com o banco que permite alteração
        #self.relatorio.get_relatorio_perfils_usado()
        input("AAAUIIOIIIII")
        self.relatorio.get_relatorio_fornecedor()
   
        input("Pressione Enter para Sair do Relatório de  quantidade de Perfils por usuarios")

    def get_relatorio_agenda(self):
        # Cria uma nova conexão com o banco que permite alteração
        self.relatorio.get_relatorio_agenda()
        input("Pressione Enter para Sair do Relatório de Agenda")
