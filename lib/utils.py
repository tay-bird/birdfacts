import json


def create_model_from_corpus(path, parser, state_size=2):
    with open(path) as f:
        text = f.read()

    model = parser(text, state_size=state_size)
    return model


def load_model_from_file(path, parser):
    with open(path) as f:
        corpus = json.load(f)

    model = parser.from_json(corpus)

    return model

