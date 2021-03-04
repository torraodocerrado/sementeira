from flask import Flask, request, jsonify
from flask_cors import cross_origin
from flask_api import status
from datetime import datetime
import os
import configparser

from sementeira.i_entities import Pessoa
from sementeira.iii_controllers import PessoaController
from sementeira.iii_controllers import PesquisarPessoa
from sementeira.iv_database import PessoaDataGatewayRelacional
from sementeira.iv_database import PessoaCreatorDataGateway

def test_if_config_file_exists(config_path):
    if not os.path.isfile(config_path):
        print('Config file *'+config_path +
              '* is missing. Execution will be stopped!')
        exit()

def read_system_config(system_config = "system.config"):
    test_if_config_file_exists(system_config)
    config = configparser.RawConfigParser()
    config.read(system_config)
    return config

app = Flask(__name__)

def prepareJsonResult(data):
    return data

def build_return(response, status_code):
    if not response:
        status_code = status.HTTP_204_NO_CONTENT
    response = prepareJsonResult(response)
    return jsonify({"status_code": status_code, "data": response})

def get_pessoa_data_gateway():
    creator = PessoaCreatorDataGateway()
    config = read_system_config()
    return creator.build(config)

@app.route('/pessoa', methods=['POST'])
@cross_origin()
def cadastrar_pessoa():
    result = []
    status_code = status.HTTP_200_OK
    try:
        data = request.json         
        data_nascimento = datetime.strptime(data["data_nascimento"], '%Y-%m-%d')
        pessoa = Pessoa(None, data["nome"], data["endereco"], data_nascimento)
        dataGateway = get_pessoa_data_gateway()
        pessoaController = PessoaController(dataGateway)
        result = pessoaController.cadastrarPessoa(pessoa)
    except Exception as e:
        status_code = status.HTTP_400_BAD_REQUEST
        result = str(e)
        print(e)
    finally:
        return build_return(result, status_code)

@app.route('/pessoa/<string:nome>', methods=['GET'])
@cross_origin()
def get_pessoa_by_nome(nome:str):
    result = []
    status_code = status.HTTP_200_OK
    try:
        dataGateway = get_pessoa_data_gateway()
        pessoaController = PessoaController(dataGateway)
        
        params = {"nome": nome}
        query = PesquisarPessoa("pessoa_por_nome", params)
        
        result = pessoaController.pesquisarPessoa(query)
        
    except Exception as e:
        status_code = status.HTTP_400_BAD_REQUEST
        result = str(e)
        print(e)
    finally:
        return build_return(result, status_code)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9999)
