from conexion.mongo_queries import MongoQueries
import pandas as pd
from pymongo import ASCENDING, DESCENDING

class Relatorio:
    def __init__(self):
        pass

    def get_relatorio_perfils_usado(self):
        # Cria uma nova conexão com o banco
        mongo = MongoQueries()
        mongo.connect()
        # Recupera os dados transformando em um DataFrame
        pipeline = [
        {
            '$lookup': {
                'from': 'usuario',
                'localField': 'codigo_perfil',
                'foreignField': 'codigo_perfil',
                'as': 'usuario_perfil'
            }
        },
        {
            '$unwind': '$usuario_perfil'
        },
        {
            '$group': {
                '_id': '$descricao_perfil',
                'qtd_usos': {
                    '$sum': 1
                }
            }
        },
        {
            '$project': {
                'descricao_perfil': '$_id',
                'qtd_usos': 1,
                '_id': 0
            }
        }
    ]

    # Executar a agregação
        resultado_agregacao = pd.DataFrame(list( mongo.db["perfils"].aggregate(pipeline)))
        print(resultado_agregacao[["qtd_usos", "descricao_perfil"]])
        input("Pressione Enter para Sair do Relatório de Quantidade perfils usados")
       
     
    def get_relator1io_perfil(self):
        # Cria uma nova conexão com o banco
        mongo = MongoQueries()
        mongo.connect()
        # Recupera os dados transformando em um DataFrame
        query_result = mongo.db["perfils"].find({}, 
                                                     {"codigo_perfil": 1, 
                                                      "descricao_perfil": 1, 
                                                      "porcentagem_perfila": 1, 
                                                      "_id": 0
                                                     }).sort("codigo_perfil", ASCENDING)
        df_perfil = pd.DataFrame(list(query_result))
        # Fecha a conexão com o mongo
        mongo.close()
        # Exibe o resultado
        print(df_perfil)        
        input("Pressione Enter para Sair do Relatório de Perfils")
        
 
    def get_relatorio_usuario(self):
        # Cria uma nova conexão com o banco
        mongo = MongoQueries()
        mongo.connect()
           
        pipeline = [
        {
            '$lookup': {
                'from': 'perfils',
                'localField': 'codigo_perfil',
                'foreignField': 'codigo_perfil',
                'as': 'perfil_usuario'
            }
        },
        {
            '$unwind': '$perfil_usuario'
        },
        {
            '$project': {
                '_id': 0,
                'codigo_usuario': 1,
                'nome': 1,
                'email': 1,
                'idade_usuario': 1,
                'altura_usuario': 1,
                'peso_usuario': 1,
                'descricao_perfil': '$perfil_usuario.descricao_perfil'
            }
        }
    ]
    # Executar a agregação
        resultado_agregacao = list(mongo.db["usuario"].aggregate(pipeline))
        df_usuarios = pd.DataFrame(resultado_agregacao)

    # Exibir DataFrame Pandas
        print(df_usuarios)       
        input("Pressione Enter para Sair do Relatório de UsuArio")

    def get_relatorio_agenda(self):
        # Cria uma nova conexão com o banco
        mongo = MongoQueries()
        mongo.connect()
        # Recupera os dados transformando em um DataFrame
        query_result = mongo.db["agenda"].find({}, 
                                                {"codigo_agenda": 1, "qtd_indicada": 1,"_id":0, "qtd_consumida": 1,
                                                    "qtd_total": 1, "data_cadastro": 1, "codigo_usuario": 1}
                                                ).sort("codigo_agenda", ASCENDING)
        

        df_usuario = pd.DataFrame(list(query_result))
        # Fecha a conexão com o mongo
        mongo.close()
        # Exibe o resultado
        print(df_usuario.to_string())        
        input("Pressione Enter para Sair do Relatório de Agenda")
