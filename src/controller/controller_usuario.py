from model.usuario import Usuario
from conexion.oracle_queries import OracleQueries
from bson import ObjectId
import pandas as pd
from conexion.mongo_queries import MongoQueries
from reports.relatoriosmogo import Relatorio


class Controller_Usuario:
    def __init__(self):
        self.mongo = MongoQueries()
        self.relatorio = Relatorio()

    def inserir_usuario(self) -> Usuario:
        self.mongo.connect()
        email = input("Email (Novo): ")

        # Solicita o nome de usuário
        nome = input("Nome de Usuário (Novo): ")
        # Solicita a idade
        idade_usuario = float(input("Idade (Novo): "))

        # Solicita a altura
        altura_usuario = float(input("Altura (Novo): "))
        # Solicita o peso
        peso_usuario = float(input("Peso (Novo): "))
        # Listar os usuarios
        self.relatorio.get_relatorio_perfil()

        # Solicita o código do usuario
        codigo_perfil = int(input("Código do pefil : "))

        proximo_usuario = self.mongo.db["usuario"].aggregate([
            {
                '$group': {
                    '_id': '$usuario',
                    'proximo_usuario': {
                        '$max': '$codigo_usuario'
                    }
                }
            }, {
                '$project': {
                    'proximo_usuario': {
                        '$sum': [
                            '$proximo_usuario', 1
                        ]
                    },
                    '_id': 0
                }
            }
        ])

        proximo_usuario = int(list(proximo_usuario)[0]['proximo_usuario'])
        # Insere e Recupera o código do novo usuario
        id_usuario = self.mongo.db["usuario"].insert_one({"codigo_usuario": proximo_usuario, "nome": nome, "email": email,
                                                         "idade_usuario": idade_usuario, "altura_usuario": altura_usuario, "peso_usuario": peso_usuario, "codigo_perfil": codigo_perfil})
        # Recupera os dados do novo usuario criado transformando em um DataFrame
        df_usuario = self.recupera_usuario(id_usuario.inserted_id)

        # Cria um novo objeto usuario
        novo_usuario = novo_usuario = Usuario(
            df_usuario.email.values[0],
            df_usuario.nome.values[0],
            df_usuario.idade_usuario.values[0],
            df_usuario.altura_usuario.values[0],
            df_usuario.peso_usuario.values[0],
            df_usuario.codigo_perfil.values[0])

        # Exibe os atributos do novo usuario
        print(novo_usuario.to_string())
        self.mongo.close()
        # Retorna o objeto novo_usuario para utilização posterior, caso necessário
        continue_resgristrando = input(
            "Deseja continuar regristrando? s /SIM - n /NÃo: ")
        if continue_resgristrando == "s":
            self.inserir_usuario()

            # Retorna o objeto novo_usuario para utilização posterior, caso necessário
        self.mongo.close()
        return novo_usuario

    def atualizar_usuario(self) -> Usuario:
        self.mongo.connect()

        self.relatorio.get_relatorio_usuario()

        # Solicita o email do usuário a ser alterado
        codigo_usuario = int(input("Codigo do usuário que deseja alterar: "))

        # Verifica se o usuário existe na base de dados
        if not self.buscar_usuario_codigo(codigo_usuario).empty:
            # Solicita o novo nome
            nome = input("Nome (Novo): ")
            # Solicita a nova idade
            idade_usuario = int(input("Idade (Nova): "))
            # Solicita a nova altura
            altura_usuario = float(input("Altura (Nova): "))
            # Solicita o novo peso
            peso_usuario = float(input("Peso (Novo): "))

            self.relatorio.get_relatorio_perfil()
            # Solicita o novo código do usuario
            codigo_perfil = int(input("Código do perfil (Novo): "))

            # Atualiza os dados do usuário existente
            self.mongo.db["usuario"].update_one({"codigo_usuario": codigo_usuario}, {
                "$set": {"nome": nome, "idade_usuario": idade_usuario, "altura_usuario": altura_usuario, "peso_usuario": peso_usuario, "codigo_perfil": codigo_perfil}})

            # Recupera os dados do usuário atualizado transformando em um DataFrame
            df_usuario = self.buscar_usuario_codigo(codigo_usuario)
            # Cria um novo objeto usuario_atualizado
            usuario_atualizado = Usuario(
                df_usuario.email.values[0],
                df_usuario.nome.values[0],
                df_usuario.idade_usuario.values[0],
                df_usuario.altura_usuario.values[0],
                df_usuario.peso_usuario.values[0],
                df_usuario.codigo_perfil.values[0]
            )
            # Exibe os atributos do novo usuário
            print(usuario_atualizado.to_string())
            # Retorna o objeto usuario_atualizado para utilização posterior, caso necessário
            continue_resgristrando = input(
                "Deseja continuar atualizando os regristos? s /SIM - n /NÃO: ")
            if continue_resgristrando == "s":
                self.atualizar_usuario()
            return usuario_atualizado
        else:
            print(f"O codigo do usuario {codigo_usuario} não existe.")
            return None

    def excluir_usuario(self):
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()
        self.relatorio.get_relatorio_usuario()

        # Solicita o email do usuário a ser excluído
        codigo = int(input("Codigo do Usuário que irá excluir: "))

        # Verifica se o usuário existe na base de dados
        if not self.buscar_usuario_codigo(codigo).empty:
            df_usuario = self.buscar_usuario_codigo(codigo)

            nome = input(
                f"você deseja excluir o  usuário? {df_usuario.nome.values[0]}:  S - Sim / N - não ")
            if nome == "s":
                if  self.recupera_usuario_codigo_relacionado(codigo).empty:

                   
                    # Revome o perfil da tabela
                    self.mongo.db["usuario"].delete_one(
                        {"codigo_usuario": codigo})
                    # Cria um novo objeto perfil para informar que foi removido
                   
                    # Exibe os atributos do perfil excluído
                    print("perfil Removido com Sucesso!")
                    print(df_usuario.to_string()) 
                    self.mongo.close()
                else:
                    print(
                        "Usuário Não pede ser apgado porque esta relaciondo com outra tabela")

        else:
            print(f"O usuario com codigo {codigo} não existe.")

    def recupera_usuario(self, _id: ObjectId = None) -> pd.DataFrame:
        # Recupera os dados do novo usuario criado transformando em um DataFrame
        usuario = pd.DataFrame(list(self.mongo.db["usuario"].find({"_id": _id}, {"codigo_usuario": 1, "_id": 0, "email": 1, "nome": 1,
                               "idade_usuario": 1, "altura_usuario": 1, "peso_usuario": 1, "codigo_perfil": 1})))
        return usuario

    def buscar_usuario_codigo(self, codigo:  int= None, external: bool = False) -> pd.DataFrame:
        if external:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect()

        # Recupera os dados do novo perfil criado transformando em um DataFrame
        usuario = pd.DataFrame(list(self.mongo.db["usuario"].find({"codigo_usuario": codigo}, {"codigo_usuario": 1, "_id": 0, "email": 1, "nome": 1,
                                "idade_usuario": 1, "altura_usuario": 1, "peso_usuario": 1, "codigo_perfil": 1})))


        if external:
            # Fecha a conexão com o Mongo
            self.mongo.close()
        
        return usuario
    def recupera_usuario_codigo_relacionado(self, codigo: int = None, external: bool = False) -> pd.DataFrame:
        if external:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect()

        # Recupera os dados do novo usuario criado transformando em um DataFrame
        usuario = pd.DataFrame(list(self.mongo.db["agenda"].find({"codigo_usuario": codigo}, {
            "codigo_agenda": 1})))

        if external:
            # Fecha a conexão com o Mongo
            self.mongo.close()

        return usuario
