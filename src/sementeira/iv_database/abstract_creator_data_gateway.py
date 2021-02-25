from ..iii_controllers import AbstractDataGateway

class AbstractCreatorDataGateway():
    _data_gateway = {}

    def __init__(self):
        self._data_gateway = {}

    def build(self, tipo: str):
        raise NotImplementedError
        
