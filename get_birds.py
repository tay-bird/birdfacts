from __future__ import print_function
import json
import re

import wikipedia

from lib.utils import create_model_from_corpus
from models import NameText
from models import NLTKText


def get_birds():
    birds = wikipedia.page('List_of_birds_by_common_name').links
    
    for bird in birds:
        try:
            summary = wikipedia.summary(bird)
        except:
            next
        
        summary = re.sub(bird, '@@SPECIES@@', summary, flags=re.IGNORECASE)

        with open('names.txt', 'a') as f:
            f.write(bird.encode('ascii','ignore') + '\n')

        with open('summaries.txt', 'a') as f:
            f.write(summary.encode('ascii', 'ignore') + '\n')


def make_corpus():
    name_model = create_model_from_corpus('names.txt', NameText, 5)
    text_model = create_model_from_corpus('summaries.txt', NLTKText, 4)

    with open('names_corpus.txt', 'w') as f:
        json.dump(name_model.to_json(), f)

    with open('summaries_corpus.txt', 'w') as f:
        json.dump(text_model.to_json(), f)


if __name__ == '__main__':
    get_birds()
    make_corpus()
