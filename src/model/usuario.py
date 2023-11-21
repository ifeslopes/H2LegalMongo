class Usuario:
    
    def __init__(self,
                 email: str = None,
                 nome: str = None,
                 idade_usuario: int = None,
                 altura_usuario: float = None,
                 peso_usuario: float = None,
                 codigo_perfil: int = None
                 ):
  
        self.set_email(email)
        self.set_nome(nome)
        self.set_idade_usuario(idade_usuario)
        self.set_altura_usuario(altura_usuario)
        self.set_peso_usuario(peso_usuario)
        self.set_codigo_perfil(codigo_perfil)

    def set_email(self, email: str):
        self.email = email

    def get_email(self) -> str:
        return self.email

    def set_nome(self, nome: str):
        self.nome = nome

    def get_nome(self) -> str:
        return self.nome

    def set_idade_usuario(self, idade_usuario: int):
        self.idade_usuario = idade_usuario

    def get_idade_usuario(self) -> int:
        return self.idade_usuario

    def set_altura_usuario(self, altura_usuario: float):
        self.altura_usuario = altura_usuario

    def get_altura_usuario(self) -> float:
        return self.altura_usuario

    def set_peso_usuario(self, peso_usuario: float):
        self.peso_usuario = peso_usuario

    def get_peso_usuario(self) -> float:
        return self.peso_usuario

    def set_codigo_perfil(self, codigo_perfil: int):
        self.codigo_perfil = codigo_perfil

    def get_codigo_perfil(self) -> int:
        return self.codigo_perfil

    def to_string(self) -> str:
        return f"Email: {self.get_email()} | Nome de Usuário: {self.get_nome()} | Idade: {self.get_idade_usuario()} | Altura: {self.get_altura_usuario()} | Peso: {self.get_peso_usuario()} | Código de Perfil: {self.get_codigo_perfil()}"
