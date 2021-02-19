from flask import Flask, request, jsonify
from flask_cors import cross_origin
from flask_api import status

from ..i_entities import Pessoa
from ..iii_controllers import PessoaController
from ..iv_database import PessoaDataGatewayRelacional
from ..iv_database import PessoaCreatorDataGateway


app = Flask(__name__)

def prepareJsonResult(data):
    return data

def build_return(response, status_code):
    if not response:
        status_code = status.HTTP_204_NO_CONTENT
    response = prepareJsonResult(response)
    return jsonify({"status_code": status_code, "data": response})

def get_tecnologia_persistencia():
    return "relacional"

def get_pessoa_data_gateway():
    creator = PessoaCreatorDataGateway()
    return creator.build(get_tecnologia_persistencia())

@app.route('/pessoa', methods=['POST'])
@cross_origin()
def cadastrar_pessoa():
    result = []
    status_code = status.HTTP_200_OK
    try:
        data = request.json
        pessoa = Pessoa(None, data.nome, data.endereco, data.data_nascimento)
        dataGateway = get_pessoa_data_gateway()
        pessoaController = PessoaController(dataGateway)
        result = pessoaController.cadastrarPessoa(pessoa)
    except Exception as e:
        status_code = status.HTTP_400_BAD_REQUEST
        result = str(e)
        print(e)
    finally:
        return build_return(result, status_code)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9999)
