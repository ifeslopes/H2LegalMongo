class Agenda:
    def __init__(self,
                 quantidade_indicada: float = None,
                 quantidade_consumida: float = None,
                 quantidade_consumida_total: float = None,
                 data_cadastro: float = None,
                 codigo_usuario: int = None
                 ):
        self.set_quantidade_indicada(quantidade_indicada)
        self.set_quantidade_consumida(quantidade_consumida)
        self.set_quantidade_consumida_total(quantidade_consumida_total)
        self.set_data_cadastro(data_cadastro)
        self.set_codigo_usuario(codigo_usuario)

    def set_quantidade_indicada(self, quantidade_indicada: float):
        self.quantidade_indicada = quantidade_indicada

    def get_quantidade_indicada(self) -> float:
        return self.quantidade_indicada

    def set_quantidade_consumida(self, quantidade_consumida: float):
        self.quantidade_consumida = quantidade_consumida

    def get_quantidade_consumida(self) -> float:
        return self.quantidade_consumida

    def set_quantidade_consumida_total(self, quantidade_consumida_total: int):
        self.quantidade_consumida_total = quantidade_consumida_total

    def get_quantidade_consumida_total(self) -> int:
        return self.quantidade_consumida_total

    def set_data_cadastro(self, data_cadastro: float):
        self.data_cadastro = data_cadastro

    def get_data_cadastro(self) -> float:
        return self.data_cadastro

    def set_codigo_usuario(self, codigo_usuario: int):
        self.codigo_usuario = codigo_usuario

    def get_codigo_usuario(self) -> int:
        return self.codigo_usuario

    def to_string(self) -> str:
        return f"Quantidade ndicada: {self.get_quantidade_indicada()} | Quantidade consumida : {self.get_quantidade_consumida()} | Quantidade consumida total: {self.get_quantidade_consumida_total()} | Data cadastro: {self.get_data_cadastro()} | Código de usuario: {self.get_codigo_usuario()}"
