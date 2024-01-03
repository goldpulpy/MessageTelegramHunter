from requests import post
from pathlib import Path
import json



class Filter:

    def __init__(self, words_file: str = "words.json") -> None:
        # Initialize the WordFilter object with a default words file "words.json"
        self.words: list = None
        self.words_file: list = words_file

    def load(self) -> bool:
        # Load words from the specified file
        try:
            with open(Path(self.words_file), 'r') as file:
                self.words: list  = json.load(file)
            return True
        except FileNotFoundError:
            # Return False if the file is not found
            return False

    def filt(self, message: str) -> float:
        # Initialize the total_score to 0.0
        total_score: float = 0.0

        # Return 0.0 if the message is empty
        if not message:
            return total_score

        # Convert the message to lowercase
        lower_message = message.lower()

        # Create a set to track unique words in the message
        unique_words_set = set()

        # Split the lowercased message into a list of words
        words_in_message: list = lower_message.split()

        # Iterate through the loaded words and their associated scores
        for word, score in self.words.items():
            # Check if the lowercase version of the word is present in the message
            # and if it has not already been counted (to avoid double counting)
            if word.lower() in words_in_message and word.lower() not in unique_words_set:
                # Add the score to the total_score and add the word to the unique set
                total_score += score
                unique_words_set.add(word.lower())

        # Return the calculated total_score
        return total_score