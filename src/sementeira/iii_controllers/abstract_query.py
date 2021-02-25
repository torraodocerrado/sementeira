class AbstractQuery():
    params: dict
    nome: str

    def __init__(self, nome: str, params):
        self.params = params
        self.nome = nome
