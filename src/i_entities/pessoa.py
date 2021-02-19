from datetime import datetime

class Pessoa:
    id: int
    nome: str
    endereco: [str]
    data_nascimento: datetime

    def __init__(self, id:int, nome: str, endereco: [str], data_nascimento: datetime):
        self.id = id
        self.nome = nome
        self.endereco = endereco        
        self.data_nascimento = data_nascimento