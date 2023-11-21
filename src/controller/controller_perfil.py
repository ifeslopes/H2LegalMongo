from model.perfil import Perfil
from conexion.oracle_queries import OracleQueries
from bson import ObjectId
import pandas as pd
from conexion.mongo_queries import MongoQueries
from reports.relatoriosmogo import Relatorio


class Controller_Perfil:
    def __init__(self):
        self.mongo = MongoQueries()
        self.relatorio = Relatorio()
    
    # def __init__(self):
    #     pass

    def inserir_perfil(self) -> Perfil:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''

        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        self.mongo.connect()
       
        # Solicita ao usuario o novo porcentagem
        descricao_novo_perfil = str(input("Perfil (Novo): "))
        porcentagem = input("Porcetagem (Novo): ")
        proximo_perfil = self.mongo.db["perfils"].aggregate([
                                                    {
                                                        '$group': {
                                                            '_id': '$perfils', 
                                                            'proximo_perfil': {
                                                                '$max': '$codigo_perfil'
                                                            }
                                                        }
                                                    }, {
                                                        '$project': {
                                                            'proximo_perfil': {
                                                                '$sum': [
                                                                    '$proximo_perfil', 1
                                                                ]
                                                            }, 
                                                            '_id': 0
                                                        }
                                                    }
                                                ])
        
        proximo_perfil = int(list(proximo_perfil)[0]['proximo_perfil'])
        # Insere e Recupera o código do novo perfil
        id_perfil = self.mongo.db["perfils"].insert_one(
            {"codigo_perfil": proximo_perfil, "descricao_perfil": descricao_novo_perfil, "porcentagem_perfil": porcentagem})
        # Recupera os dados do novo perfil criado transformando em um DataFrame
        df_perfil = self.recupera_perfil(id_perfil.inserted_id)
      
        # Cria um novo objeto perfil
        novo_perfil = Perfil(df_perfil.porcentagem_perfil.values[0], df_perfil.descricao_perfil.values[0])
       
        # Exibe os atributos do novo perfil
        print(novo_perfil.to_string())
        self.mongo.close()
        # Retorna o objeto novo_perfil para utilização posterior, caso necessário
        continue_resgristrando = input(
                "Deseja continuar regristrando? s /SIM - n /NÃo: ")
        if continue_resgristrando == "s":
                self.inserir_perfil()

        # Retorna o objeto novo_perfil para utilização posterior, caso necessário
        return novo_perfil
    
       
        

    def atualizar_perfil(self) -> Perfil:
        
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        self.relatorio.get_relatorio_perfil()

        # Solicita ao usuário o código do perfil a ser alterado
        codigo_perfil = int(input("Código do perfil que irá alterar: "))

        # Verifica se o perfil existe na base de dados
        if   not self.recupera_perfil_codigo(codigo_perfil).empty:
            # Solicita a nova descrição do perfil
            nova_descricao_perfil = input("Descrição (Novo): ")
            # Atualiza a descrição do perfil existente
            self.mongo.db["perfils"].update_one({"codigo_perfil": codigo_perfil}, {
                                                 "$set": {"descricao_perfil": nova_descricao_perfil}})
            # Recupera os dados do novo perfil criado transformando em um DataFrame
            df_perfil = self.recupera_perfil_codigo(codigo_perfil)
            # Cria um novo objeto perfil
            perfil_atualizado = Perfil(
                df_perfil.porcentagem_perfil.values[0], df_perfil.descricao_perfil.values[0])
            # Exibe os atributos do novo perfil
            print(perfil_atualizado.to_string())
            # Retorna o objeto perfil_atualizado para utilização posterior, caso necessário
            continue_resgristrando = input(
                "Deseja continuar atualizando regristrando? s /SIM - n /NÃO: ")
            if continue_resgristrando == "s":
                self.atualizar_perfil()

            self.mongo.close()
            return perfil_atualizado
            
        else:
            self.mongo.close()
            print(f"O código {codigo_perfil} não existe.")
            return None



    def excluir_perfil(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        self.mongo.connect()
        self.relatorio.get_relatorio_perfil()

        # Solicita ao usuário o código do perfil a ser alterado
        codigo_perfil = int(input("Código do perfil que irá excluir: "))        

        # Verifica se o perfil existe na base de dados
        if  not self.recupera_perfil_codigo(codigo_perfil).empty:  
           
            if self.recupera_perfil_codigo_relacionado(codigo_perfil).empty:          
            # Recupera os dados do novo perfil criado transformando em um DataFrame
                df_perfil = self.recupera_perfil_codigo(codigo_perfil)
                # Revome o perfil da tabela
                self.mongo.db["perfils"].delete_one({"codigo_perfil": codigo_perfil})
                # Cria um novo objeto perfil para informar que foi removido
                perfil_excluido = Perfil(df_perfil.codigo_perfil.values[0], df_perfil.descricao_perfil.values[0])
                # Exibe os atributos do perfil excluído
                print("perfil Removido com Sucesso!")
                print(perfil_excluido.to_string())
                self.mongo.close()
            else:
                print("perfil não pode ser Removido esta  usado em outra tabela!")
                self.mongo.close()
                

        else:
            self.mongo.close()
            print(f"O código {codigo_perfil} não existe.")

    

    def recupera_perfil(self, _id:ObjectId=None) -> pd.DataFrame:
        # Recupera os dados do novo perfil criado transformando em um DataFrame
        perfil = pd.DataFrame(list(self.mongo.db["perfils"].find({"_id":_id}, {"codigo_perfil": 1, "descricao_perfil": 1, "_id": 0,"porcentagem_perfil":1},)))
        return perfil

    def recupera_perfil_codigo(self, codigo:int=None, external: bool = False) -> pd.DataFrame:
        if external:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect()

        # Recupera os dados do novo perfil criado transformando em um DataFrame
        perfil = pd.DataFrame(list(self.mongo.db["perfils"].find({"codigo_perfil": codigo}, {
                              "codigo_perfil": 1, "descricao_perfil": 1, "_id": 0, "porcentagem_perfil": 1})))

        if external:
            # Fecha a conexão com o Mongo
            self.mongo.close()

        return perfil
    
    def recupera_perfil_codigo_relacionado(self, codigo:int=None, external: bool = False) -> pd.DataFrame:
        if external:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect()

        # Recupera os dados do novo perfil criado transformando em um DataFrame
        perfil = pd.DataFrame(list(self.mongo.db["usuario"].find({"codigo_perfil": codigo}, {
                              "nome": 1})))

        if external:
            # Fecha a conexão com o Mongo
            self.mongo.close()

        return perfil
