from utils import config


class SplashScreen:

    def __init__(self):
        # Nome(s) do(s) criador(es)
        self.created_by = "DIEGO MOREIRA, JACÓ LEOPOLDINO"
        self.created_by1 = "KAMILA GALANDE,LEONARDO LOPES"
        self.created_by2 = "MARCIEL COUTINHO,VICTOR FERREIRA"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2023/2"

    def get_documents_count(self, collection_name):
        # Retorna o total de registros computado pela query
        df = config.query_count(collection_name=collection_name)
        return df[f"total_{collection_name}"].values[0]

    def get_updated_screen(self):
        return f"""
        ########################################################
        #                   SISTEMA DE VENDAS                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - USUÁRIO:         {str(self.get_documents_count(collection_name="usuario")).rjust(5)}
        #      2 - PERFIL:          {str(self.get_documents_count(collection_name="perfils")).rjust(5)}
        #      3 - AGENDA:          {str(self.get_documents_count(collection_name="agenda")).rjust(5)}
        #   
        #
        #  CRIADO POR: {self.created_by}
        #              {self.created_by1}
        #              {self.created_by2}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """
