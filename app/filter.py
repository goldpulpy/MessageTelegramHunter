from requests import post
from pathlib import Path
import json



class Filter:

    def __init__(self, words_file: str = "words.json",
                       memory_limit: int = 100) -> None:
        

        self.words: list = None
        self.words_file: list = words_file

        self.memory: list = []
        self.memory_limit: int = memory_limit

    def load(self) -> bool:

        try:

            with open(Path(self.words_file), 'r') as file:
                self.words: list  = json.load(file)

            return True

        except FileNotFoundError:

            return False


    def filt(self, message: str) -> float:

        total_score: float = 0.0

        if not message:
            return total_score

       
        lower_message = message.lower()

        if lower_message in set(self.memory):

            return total_score

        unique_words_set = set()

        words_in_message: list = lower_message.split()

        for word, score in self.words.items():

            if word.lower() in words_in_message and word.lower() not in unique_words_set:

                total_score += score
                
                unique_words_set.add(word.lower())

        self.memory = [lower_message] + [m for m in self.memory if m != lower_message][:self.memory_limit - 1]

        return total_score