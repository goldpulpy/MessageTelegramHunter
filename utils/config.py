import json


class Config:
    def __init__(self, config: str = "config.json") -> None:

        self.config: str = config


        self.API_ID: int = None
        self.API_HASH: str = None
        self.SESSION_NAME: str = None
        self.FORWARD_TO_ID: int = None
        self.MESSAGE_POOL: int = None
        self.WAIT_TIME: int = None


    def load_config(self) -> bool:
        
        try:

            with open(self.config, 'r') as file:

                config: dict = json.load(file)

        except FileNotFoundError:

            return False

        self.API_ID: int = config['API_ID']
        self.API_HASH: str = config['API_HASH']
        self.SESSION_NAME: str = config['SESSION_NAME']
        self.FORWARD_TO_ID: int = config['FORWARD_TO_ID']
        self.MESSAGE_POOL: int = config['MESSAGE_POOL']
        self.WAIT_TIME: int = config['WAIT_TIME']

        return True