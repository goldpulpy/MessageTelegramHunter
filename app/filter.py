from requests import post
from pathlib import Path
import json



class Filter:

    def __init__(self, words_file: str = "words.json") -> None:
        

        self.words: list = None
        self.words_file: list = words_file

    def load(self) -> bool:

        try:

            with open(Path(self.words_file), 'r') as file:
                self.words: list  = json.load(file)

            return True

        except FileNotFoundError:

            return False



    def filt(self, message: str, temperature: int = 0.5 ) -> float:

        total_score: float = 0.0

        for word, score in self.words.items():

            if word in message:

                score += score

        return total_score