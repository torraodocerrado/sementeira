from .abstract_creator_data_gateway import AbstractCreatorDataGateway
from .pessoa_data_gateway_relacional import PessoaDataGatewayRelacional
from .pessoa_data_gateway_json import PessoaDataGatewayJson

class PessoaCreatorDataGateway(AbstractCreatorDataGateway):

    def build(self, config):
        print(config)
        tipo = config.get("persistencia", "tecnologia")
        if tipo not in self._data_gateway:
            if tipo == 'relacional':
                self._data_gateway[tipo] = PessoaDataGatewayRelacional(config)
            if tipo == 'json':
                self._data_gateway[tipo] = PessoaDataGatewayJson()
        if tipo in self._data_gateway:
            return self._data_gateway[tipo]
        else:
            raise Exception("Tipo {} não encontrado".format(tipo))
