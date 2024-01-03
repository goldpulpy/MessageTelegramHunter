import json


class Config:
    def __init__(self, config: str = "config.json") -> None:
        # Initialize the Config object with a default configuration file "config.json"
        self.config: str = config
        self.API_ID: int = None
        self.API_HASH: str = None
        self.SESSION_NAME: str = None
        self.FORWARD_TO_ID: int = None
        self.MESSAGE_POOL: int = None
        self.WAIT_TIME: int = None
        self.REPORT_SCORE: float = None
        self.MEMORY_LIMIT: int = None

    def load_config(self) -> bool:
        # Attempt to load configuration from the specified file
        try:
            with open(self.config, 'r') as file:
                config: dict = json.load(file)

        except FileNotFoundError:
            # Return False if the file is not found
            return False

        # Assign values from the loaded configuration to the class attributes
        self.API_ID: int = config['API_ID']
        self.API_HASH: str = config['API_HASH']
        self.SESSION_NAME: str = config['SESSION_NAME']
        self.FORWARD_TO_ID: int = config['FORWARD_TO_ID']
        self.MESSAGE_POOL: int = config['MESSAGE_POOL']
        self.WAIT_TIME: int = config['WAIT_TIME']
        self.REPORT_SCORE: float = config['REPORT_SCORE']
        self.MEMORY_LIMIT: int = config['MEMORY_LIMIT']

        # Return True to indicate successful loading of the configuration
        return True