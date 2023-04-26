"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    ###
    #filename is the name of the words.txt
    def __init__(self, filename):
        self.filename = filename
        self.words = self.read_words()
    #opens the file
    def read_words(self):
        with open(self.filename, 'r') as file: #opens file 'r' read, and creates variable file with the opened object
            words = [line.strip() for line in file] #strip()  removes white space before and after
        return words

    def random_word(self):
        return random.choice(self.words)

wf = WordFinder("words.txt")
print(wf.random_word())

 # $ python3 wordfinder.py

class SpecialWordFinder(WordFinder):
    """A subclass of WordFinder that ignores blank lines and comments."""

    def __init__(self, filename):
        super().__init__(filename)
        self.words = [word for word in self.words if word and not word.startswith('#')]

swf = SpecialWordFinder("words_special.txt")
print(swf.random_word())

 # $ python3 wordfinder.py
