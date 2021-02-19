from ..ii_use_cases import PessoaModule
from ..i_entities import Pessoa
from .abstract_data_gateway import AbstractDataGateway

class PessoaController():
    dataGateway: AbstractDataGateway
    pessoaModule: PessoaModule

    def __init__(self, dataGateway: AbstractDataGateway):
        self.dataGateway = dataGateway
        self.pessoaModule = PessoaModule()
    
    def cadastrarPessoa(self, pessoa: Pessoa):
        if self.pessoaModule.validar_casos_uso(pessoa):
            self.dataGateway.cadastrar(pessoa)

