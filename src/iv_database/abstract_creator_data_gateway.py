from ..iii_controllers import AbstractDataGateway

class AbstractCreatorDataGateway():
    _data_gateway = AbstractDataGateway

    def __init__(self):
        self._data_gateway = None

    def build(self, tipo: str):
        raise NotImplementedError
        
