from requests import post
from pathlib import Path
import random

class SmartFilter:

    def __init__(self, instructions_file: str = "instructions.txt",
                       words_file: str = "words.txt") -> None:
        
        self.url: str = "https://openchat.team/api/chat"


        self.model: dict ={ "id":"openchat_v3.2_mistral",
                            "name":"OpenChat Aura",
                            "maxLength":24576,
                            "tokenLimit":8192}

        self.PROMTER: str = '''
Your job is to check the message, here is a list of instructions. (the message can be anything)
List of instructions:

%s

If the message matches one of the instructions, you must answer True
If the sentence does not match the instruction completely answer False.
Answer True or False and nothing else.

Message: "%s"
'''



        self.instructions: str = None
        self.instructions_file: str = instructions_file


        self.words: list = None
        self.words_file: list = words_file



    def load(self) -> bool:

        try:

            #ai filter
            with open(Path(self.instructions_file), 'r') as file:
                self.instructions: str = file.read()

            #classic filter
            with open(Path(self.words_file), 'r') as file:
                words_content: str  = file.read()
                self.words: list  = [word.strip() for word in words_content.split(',')]
            


            return True

        except FileNotFoundError:

            return False



    def classic_filter(self, target: str) -> bool:
        lowercase_target = target.lower()

        return any(variation in lowercase_target for variation in self.words)    


    def ai_filter(self, target: str, 
                   temperature: int = 0.5 
            ) -> bool:

        promt: dict = {
            "model": self.model,
            "messages": [

                {"role":"user","content":self.PROMTER % (self.instructions, target)},
            ],
            "key":"",
            "prompt":" ",
            "temperature": temperature

        }

        result: str = post(self.url, json=promt).text

        if "true" in result.lower():
            
            return True

        return False



    def filt(self, target: str, temperature: int = 0.5) -> bool:

        classic_result: bool = self.classic_filter(target)

        ai_result: bool = self.ai_filter(target, temperature)

        if classic_result and ai_result:

            return True

        elif classic_result and not ai_result:

            return random.choice([True, False, True])

        elif ai_result and not classic_result:

            return random.choice([False, True, False])

        else:

            return False