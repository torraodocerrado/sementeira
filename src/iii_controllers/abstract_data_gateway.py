from ..i_entities import Pessoa
from .abstract_query import AbstractQuery

class AbstractDataGateway():

    def cadastrar(self, obj):
        raise NotImplementedError

    def editar(self, obj):
        raise NotImplementedError

    def deletar(self, obj):
        raise NotImplementedError

    def pesquisar(self, query: AbstractQuery):
        raise NotImplementedError

