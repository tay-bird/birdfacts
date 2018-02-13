import re

import markovify
import wikipedia

from lib.nametext import NameText


def _create_model_from_corpus(path, parser, state_size=2):
    with open(path) as f:
        text = f.read()

    text_model = parser(text, state_size=state_size)
    return text_model


def sub_in_name(name, text):
    return re.sub('@@SPECIES@@', name, text)


def _format_fact(name, start_sentence, final_sentence):
    fact = '{name}: {start_sentence} {final_sentence}'.format(
        name=name,
        start_sentence=sub_in_name(name, start_sentence),
        final_sentence=sub_in_name(name, final_sentence)
    )
   
    return fact


def get_fact():
    name_model = _create_model_from_corpus('names.txt', NameText, 5)
    text_model = _create_model_from_corpus('summaries.txt', markovify.Text, 3)

    name = name_model.make_sentence()
    start_sentence = text_model.make_sentence_with_start('The @@SPECIES@@')
    final_sentence = text_model.make_sentence_with_start('It')
    
    fact = _format_fact(name, start_sentence, final_sentence)

    return fact

