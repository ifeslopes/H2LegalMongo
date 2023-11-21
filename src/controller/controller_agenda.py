import os
from time import sleep
from model.agenda import Agenda
from model.usuario import Usuario
from conexion.oracle_queries import OracleQueries
from bson import ObjectId
import pandas as pd
from conexion.mongo_queries import MongoQueries
from reports.relatoriosmogo import Relatorio
import datetime




class Controller_Agenda:
    def __init__(self):
        pass
        self.mongo = MongoQueries()
        self.relatorio = Relatorio()

    def inserir_agenda(self) -> Usuario:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        relatorio = Relatorio()
        self.mongo.connect()

        relatorio.get_relatorio_usuario()
        # Solicita o novo email
        codigo = int(input("entre com codigo do usuario: "))

   
        agenda = self.criar_agenda_para_usuario(codigo)
        proximo_agenda = self.mongo.db["agenda"].aggregate([
            {
                '$group': {
                    '_id': '$agenda',
                    'proximo_agenda': {
                        '$max': '$codigo_agenda'
                    }
                }
            }, {
                '$project': {
                    'proximo_agenda': {
                        '$sum': [
                            '$proximo_agenda', 1
                        ]
                    },
                    '_id': 0
                }
            }
        ])

        proximo_agenda = int(list(proximo_agenda)[0]['proximo_agenda'])

            # Insere e persiste o novo usuário
        id_usuario = self.mongo.db["agenda"].insert_one({"codigo_agenda": proximo_agenda, "qtd_indicada": agenda.get_quantidade_indicada(), "qtd_consumida": agenda.get_quantidade_consumida(),
                                                        "qtd_total": agenda.get_quantidade_consumida_total(), "data_cadastro": agenda.get_data_cadastro(), "codigo_usuario": int(agenda.get_codigo_usuario())})
        df_agenda = self.recupera_agenda(id_usuario.inserted_id)

            # Cria um novo objeto Usuario
        nova_agenda = Agenda(
                df_agenda.qtd_indicada.values[0],
                df_agenda.qtd_consumida.values[0],
                df_agenda.qtd_total.values[0],
                df_agenda.data_cadastro.values[0],
                df_agenda.codigo_usuario.values[0]
            )

            # Exibe os atributos do novo usuário
        print(nova_agenda.to_string())

        continue_resgristrando = input(
                "Deseja continuar regristrando? s /SIM - n /NÃO: ")
        if continue_resgristrando == "s":
                self.inserir_agenda()

            # Retorna o objeto novo_usuario para utilização posterior, caso necessário
        return nova_agenda
      

    def atualizar_agenda(self) -> Usuario:

        print(" EM DESEVOLVIMENTO... ")
        sleep(3)
        return None
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        relatorio = Relatorio()

        # Solicita o email do usuário a ser alterado
        email = input("Email do usuário que deseja alterar: ")

        # Verifica se o usuário existe na base de dados
        if not self.verifica_usuario_completou_quantidade_agua(oracle, email):
            # Solicita o novo nome
            novo_nome = input("Nome (Novo): ")
            # Solicita a nova idade
            nova_idade_usuario = int(input("Idade (Nova): "))
            # Solicita a nova altura
            nova_altura_usuario = float(input("Altura (Nova): "))
            # Solicita o novo peso
            novo_peso_usuario = float(input("Peso (Novo): "))

            relatorio.get_relatorio_perfil()
            # Solicita o novo código do perfil
            novo_codigo_perfil = int(input("Código do Perfil (Novo): "))

            # Atualiza os dados do usuário existente
            oracle.write(
                f"update usuario set nome = '{novo_nome}', idade_usuario = {nova_idade_usuario}, altura_usuario = {nova_altura_usuario}, peso_usuario = {novo_peso_usuario}, codigo_perfil = {novo_codigo_perfil} where email = '{email}'")
            # Recupera os dados do usuário atualizado transformando em um DataFrame
            df_agenda = oracle.sqlToDataFrame(
                f"select email, nome, idade_usuario, altura_usuario, peso_usuario, codigo_perfil from usuario where email = '{email}'")
            # Cria um novo objeto usuario_atualizado
            usuario_atualizado = Usuario(
                df_agenda.email.values[0],
                df_agenda.nome.values[0],
                df_agenda.idade_usuario.values[0],
                df_agenda.altura_usuario.values[0],
                df_agenda.peso_usuario.values[0],
                df_agenda.codigo_perfil.values[0]
            )
            # Exibe os atributos do novo usuário
            print(usuario_atualizado.to_string())
            # Retorna o objeto usuario_atualizado para utilização posterior, caso necessário

            continue_resgristrando = input(
                "Deseja continuar regristrando? s /SIM - n /NÃO: ")
            if continue_resgristrando == "s":
                self.atualizar_agenda()

            return usuario_atualizado
        else:
            print(f"O usario não existe.")
            return None

    def excluir_agenda(self):
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()
        self.relatorio.get_relatorio_agenda()

        # Solicita o email do usuário a ser excluído
        id = int(input("Entre com Id da agendamento ou do usuario que irá excluir: "))

        # Verifica se o usuário existe na base de dados
        if not self.recupera_agenda_id(id).empty:

            df_agenda = self.recupera_agenda_id(id)
                
            nome = input(
                f"você deseja excluir  agenda mendo do codigo? {df_agenda.codigo_agenda.values[0]}:  S - Sim / N - não ")

            if nome == "s":
                # Revome o perfil da tabela
                    
                self.mongo.db["agenda"].delete_one({"codigo_agenda": id})
                   
                    # Exibe os atributos do perfil excluído
                print("perfil Removido com Sucesso!")
                print(df_agenda.to_string())

                continue_resgristrando = input(
                    "Deseja continuar excluindo os regristos? s /SIM - n /NÃO: ")
                if continue_resgristrando == "s":
                    self.excluir_agenda()
        else:
            print(f"O agendamentop do código {id} não existe.")

    
    def recupera_agenda(self, _id: ObjectId = None) -> pd.DataFrame:
        # Recupera os dados do novo usuario criado transformando em um DataFrame
        agenda = pd.DataFrame(list(self.mongo.db["agenda"].find({"_id": _id}, {"codigo_agenda":1,"qtd_indicada":1, "qtd_consumida" :1,"qtd_total" :1, "data_cadastro":1, "codigo_usuario":1})))
        return agenda
    def recupera_agenda_id(self, codigo: int = None) -> pd.DataFrame:
        self.mongo.connect()
        # Recupera os dados do novo usuario criado transformando em um DataFrame
        agenda = pd.DataFrame(list(self.mongo.db["agenda"].find({"codigo_agenda": codigo}, {"codigo_agenda":1,"qtd_indicada":1, "qtd_consumida" :1,"qtd_total" :1, "data_cadastro":1, "codigo_usuario":1})))
  
        return agenda

    def verifica_usuario_completou_quantidade_agua(self, oracle: OracleQueries, codigo: str = None) -> bool:
        # Recupera os dados do agenda criado transformando em um DataFrame
        df_agenda = oracle.sqlToDataFrame(
            f"select * from agenda WHERE (QTD_CONSUMIDA < QTD_INDICADA ) AND CODIGO_USUARIO   = '{codigo}'")
        return df_agenda.empty

 
    def criar_agenda_para_usuario(self, codigo:  int = None, external: bool = False) -> pd.DataFrame:
        # Recupera os dados do agenda criado transformando em um DataFrame
        
        self.mongo.connect()
        data_atual = datetime.datetime.today()

        ml_agua_kilo = float(35)
        ml_agua_dia = float(350)

        df_agenda = pd.DataFrame(list(self.mongo.db["usuario"].find({"codigo_usuario": codigo}, {"codigo_usuario": 1, "_id": 0, "email": 1, "nome": 1,"idade_usuario": 1, "altura_usuario": 1, "peso_usuario": 1, "codigo_perfil": 1})))
       
        df_perfil = pd.DataFrame(list(self.mongo.db["perfils"].find({"codigo_perfil": int(df_agenda.codigo_perfil.values[0])}, {
                              "codigo_perfil": 1, "descricao_perfil": 1, "_id": 0, "porcentagem_perfil": 1})))                                                                                                  
        
        qauntidade_agua_indicada = int(float(
            df_agenda.peso_usuario.values[0] * ml_agua_kilo) * float(df_perfil.porcentagem_perfil.values[0])) / 1000

        tempo = str(input(
            "Entre com intervalo de tempo que gostaria de receber os aviso entre com Horas e Minutos Ex:[1:30]: "))

        segundos = float(
            float(tempo.split(":")[0]) * 60*60 + float(tempo.split(":")[1]) * 60)
        qauntidade_consumida = str(
            input("Entre com quantidade de água cunsumida em Ml: "))
        agenda = Agenda(qauntidade_agua_indicada, qauntidade_consumida,
                        qauntidade_consumida, data_atual, df_agenda.codigo_usuario.values[0])
        
            # Fecha a conexão com o Mongo
      
        

        return agenda
