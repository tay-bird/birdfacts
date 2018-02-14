import json
import re

import markovify
import wikipedia

from models import NameText
from models import NLTKText
from utils import load_model_from_file


def sub_in_name(name, text):
    return re.sub('@@SPECIES@@', name, text)


def _format_fact(name, start_sentence, final_sentence):
    fact = '{start_sentence} {final_sentence}'.format(
        start_sentence=sub_in_name(name, start_sentence),
        final_sentence=sub_in_name(name, final_sentence)
    )
   
    return fact


def get_fact():
    name_model = load_model_from_file('names_corpus.txt', NameText)
    text_model = load_model_from_file('summaries_corpus.txt', NLTKText)

    name = name_model.make_sentence()
    start_sentence = text_model.make_sentence_with_start('The @@SPECIES@@', tries=100)
    final_sentence = text_model.make_sentence_with_start('It', tries=100)
    
    fact = _format_fact(name, start_sentence, final_sentence)

    return fact

