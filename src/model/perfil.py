class Perfil:
    def __init__(self, 
                 porcentagem:float=None, 
                 nome:str=None
                ):
        self.set_porcentagem(porcentagem)
        self.set_nome(nome)

    def set_porcentagem(self, porcentagem:float):
        self.porcentagem = porcentagem

    def set_nome(self, nome:str):
        self.nome = nome

    def get_porcentagem(self) -> float:
        return self.porcentagem

    def get_nome(self) -> str:
        return self.nome

    def to_string(self) -> str:
        return f"porcentagem: {self.get_porcentagem()} | Nome: {self.get_nome()}"