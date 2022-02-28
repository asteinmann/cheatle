__version__ = '0.1.0'

import re

class WordleSolver():
    def __init__(self,dict_file='/usr/share/dict/words'):
        with open( dict_file) as f:
            self.words = f.read()
        self.cur_set = None
        
    @staticmethod
    def _sanitize_guess(guess):
        assert len(guess)==5, 'Guess must be 5 characters'
        
    def get_list(self,guess,has_letters,used=''):
        # Add used letters
        self._sanitize_guess(guess)
        b = re.compile(f"\\b{guess}\\b")
        cur_set = b.findall(self.words)
        for letter in has_letters:
            cur_set = [x for x in cur_set if letter in x]
        for word in cur_set:
            for letter in word:
                if letter in used:
                    cur_set.remove(word)
                    break
        self.cur_set = cur_set
        return cur_set