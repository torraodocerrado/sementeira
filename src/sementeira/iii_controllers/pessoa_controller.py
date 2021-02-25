from ..ii_use_cases import PessoaModule
from ..i_entities import Pessoa
from .abstract_data_gateway import AbstractDataGateway

class PessoaController():
    dataGateway: AbstractDataGateway
    pessoaModule: PessoaModule

    def __init__(self, dataGateway: AbstractDataGateway):
        self.dataGateway = dataGateway
        self.pessoaModule = PessoaModule()
    
    def cadastrarPessoa(self, pessoa: Pessoa)->Pessoa:
        response = None
        if self.pessoaModule.validar_casos_uso(pessoa):
            response = self.dataGateway.cadastrar(pessoa)
        return response

    def pesquisarPessoa(self, params)-> list:
        response = self.dataGateway.pesquisar(params)
        return response

