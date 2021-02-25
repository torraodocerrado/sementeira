from ..i_entities import Pessoa
from ..iii_controllers import AbstractDataGateway

class PessoaDataGatewayRelacional(AbstractDataGateway):

    def cadastrarPessoa(self, pessoa: Pessoa):
        raise NotImplementedError
