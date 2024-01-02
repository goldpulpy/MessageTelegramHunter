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


    def filt(self, message: str) -> float:
        total_score: float = 0.0
        unique_words_set = set()

        words_in_message: list = message.lower().split() if message else []

        for word, score in words.items():

            for word_from_message in words_in_message:

                if word.lower() in word_from_message and word_from_message not in unique_words_set:

                    total_score += score
                    unique_words_set.add(word_from_message)

        return total_score