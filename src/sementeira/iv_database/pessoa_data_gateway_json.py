import json
import datetime
from os import listdir
from os.path import isfile, join

from ..i_entities import Pessoa
from ..iii_controllers import AbstractDataGateway
from ..iii_controllers import AbstractQuery


class PessoaDataGatewayJson(AbstractDataGateway):

    def get_output_file_name(self, pessoa: Pessoa):
        return "pessoa_1_"+pessoa.nome+".json"

    def save_to_file(self, pessoa, output_file_name):
        f = open(output_file_name, "w")
        f.write(pessoa)
        f.close()

    def json(self, o):
        if isinstance(o, (datetime.date, datetime.datetime)):
            return o.isoformat()
        else:
            return o.__dict__

    def parsePessoaJson(self, pessoa: Pessoa):
        return json.dumps(pessoa, sort_keys=True,
                          indent=1, default=self.json)

    def cadastrar(self, pessoa: Pessoa):
        pessoa_json = self.parsePessoaJson(pessoa)
        output_file_name = self.get_output_file_name(pessoa)
        self.save_to_file(pessoa_json, output_file_name)

    def getJsonFiles(self):
        mypath = "."
        return [f for f in listdir() if isfile(join(mypath, f)) and '.json' in f]

    def pesquisar_pessoa_por_nome(self, query):
        params = query.params
        files = self.getJsonFiles()
        response = []
        print("aqui", files)
        for item in files:
            with open(item) as json_file:
                data = json.load(json_file)
                if params["nome"].lower() in data["nome"].lower():
                    response.append(data)
        return response


    def pesquisar(self, query: AbstractQuery):
        if "pessoa_por_nome" in query.nome:
            return self.pesquisar_pessoa_por_nome(query)
