from requests import post
from pathlib import Path
import json



class SmartFilter:

    def __init__(self, words_file: str = "words.json") -> None:
        

        self.words: list = None
        self.words_file: list = words_file


        self.url: str = "https://openchat.team/api/chat"


        self.model: dict ={ "id":"openchat_v3.2_mistral",
                            "name":"OpenChat Aura",
                            "maxLength":24576,
                            "tokenLimit":8192}


        self.PROMTER: str = '''
your task is to determine whether these words are on any box in the sentence 
I give you a list of words and its points.

%s

your answer should be the total number of points without text for example: 0.5 no need to explain.
message: "%s"
'''


    def load(self) -> bool:

        try:

            with open(Path(self.words_file), 'r') as file:
                self.words: list  = json.load(file)

            return True

        except FileNotFoundError:

            return False



    def filt(self, message: str, temperature: int = 0.5 ) -> float:

        promt: dict = {
            "model": self.model,
            "messages": [

                {"role":"user","content":self.PROMTER % (self.words, message)},
            ],
            "key":"",
            "prompt":" ",
            "temperature": temperature

        }

        result: str = post(self.url, json=promt).text

        try:

            total_score: float = float(result)

        
            return total_score

        except:

            return 0