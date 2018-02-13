import re
import time

import markovify


class NameText(markovify.Text):

    def sentence_split(self, text):
        return re.split(r"\s*\n\s*", text)

    def sentence_join(self, sentences):
        return '.'.join(sentences)

    def word_split(self, sentence):
        return list(sentence)

    def word_join(self, sentence):
        return ''.join(sentence)
