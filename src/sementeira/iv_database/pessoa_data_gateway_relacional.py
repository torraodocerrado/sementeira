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
    attributes = ["nome", "endereco", "data_nascimento"]

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

    def cadastrar(self, pessoa: Pessoa):
        data = []
        try:
            cursor = self.get_connection().cursor(cursor_factory=psycopg2.extras.DictCursor)
            cursor.execute(self.config.get('queries', "pessoa_cadastrar"), [pessoa.nome,
                                                                            pessoa.endereco,
                                                                            pessoa.data_nascimento])
            answer = cursor.fetchall()
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

    def cadastrar(self, pessoa: Pessoa):
        data = []
        try:
            cursor = self.get_connection().cursor(cursor_factory=psycopg2.extras.DictCursor)
            cursor.execute(self.config.get('queries', "pessoa_cadastrar"), [pessoa.nome,
                                                                            pessoa.endereco,
                                                                            pessoa.data_nascimento])
            answer = cursor.fetchall()
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
