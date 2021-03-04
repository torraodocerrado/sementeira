import psycopg2
import psycopg2.extras
import json
import datetime
from pprint import pprint

from ..i_entities import Pessoa
from ..iii_controllers import AbstractDataGateway

class PessoaDataGatewayRelacional(AbstractDataGateway):
    conn = None
    config = None

    def __init__(self, config):
        self.config = config

    def get_connection(self):
        if not self.conn:
            self.conn = psycopg2.connect("dbname='"+self.config.get('database', 'database') +
                                         "' user='"+self.config.get('database', 'user') +
                                         "' host='"+self.config.get('database', 'host') +
                                         "' port='"+self.config.get('database', 'port') +
                                         "' password='"+self.config.get('database', 'password') +
                                         "'")
            self.conn.autocommit = True
        return self.conn

    def json(self, o):
        if isinstance(o, (datetime.date, datetime.datetime)):
            return o.isoformat()
        else:
            return o.__dict__

    def to_json(self, data_object):
        data_dump = json.dumps(data_object,
                          sort_keys=True,
                          indent=1,
                          default=self.json)
        response = json.loads(data_dump)
        return response

    def to_dict(self, data_object):
        data = self.to_json(data_object)
        return data
    
    def cadastrar(self, pessoa: Pessoa):
        data = []
        try:
            pessoa = self.to_dict(pessoa)
            cursor = self.get_connection().cursor(cursor_factory=psycopg2.extras.DictCursor)
            cursor.execute(self.config.get('queries', "pessoa_cadastrar"), [pessoa["nome"], pessoa["endereco"], pessoa["data_nascimento"]])
            print("aqui")
            answer = cursor.fetchall()
            print(answer)
            data = []
            for row in answer:
                data.append(dict(row))
        except Exception as e:
            print(e)
            raise e
        finally:
            try:
                cursor.close()
            except:
                pass
        return data
