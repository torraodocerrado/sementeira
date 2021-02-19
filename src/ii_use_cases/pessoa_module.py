from ..i_entities import Pessoa

class PessoaModule:
    idade_minima = 14

    def get_idade(self, pessoa: Pessoa):
        raise NotImplementedError

    def validar_casos_uso(self, pessoa: Pessoa):
        if self.get_idade(pessoa) < self.idade_minima:
            e = Exception("Pessoa não possui idade mínima de "+str(self.idade_minima))
            print(e)
            return False
        else:
            return True