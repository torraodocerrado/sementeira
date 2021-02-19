from .abstract_creator_data_gateway import AbstractCreatorDataGateway
from .pessoa_data_gateway_relacional import PessoaDataGatewayRelacional

class PessoaCreatorDataGateway(AbstractCreatorDataGateway):

    def build(self, tipo: str):
        if not self._data_gateway:
            if tipo == 'relacional':
                self._data_gateway = PessoaDataGatewayRelacional()
        return self._data_gateway
