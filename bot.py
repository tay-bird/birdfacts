import os

import nltk

from lib import facts, tweeter


def run():
    path = os.environ.get('NLTK_DATA')

    if path:
        nltk.download('averaged_perceptron_tagger', download_dir=path)
        facts.postfact()

    else:
        raise KeyError('Could not find environment variable: ')
