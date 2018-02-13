import markovify
import wikipedia

from nametext import NameText


def create_model_from_corpus(path, parser, state_size=2):
    with open(path) as f:
        text = f.read()

    text_model = parser(text, state_size=state_size)
    return text_model


def sub_in_name(name, text):
    re.sub('@@SPECIES@@', name, text)


if __name__ == '__main__':
    name_model = create_model_from_corpus('names.txt', NameText, 5)
    name = name_model.make_sentence()

    text_model = create_model_from_corpus('summaries.txt', markovify.Text, 3)
    start_sentence = text_model.make_sentence_with_start('The')
    final_sentence = text_model.make_sentence()
    
    print name
    print sub_in_name(start_sentence)
    print sub_in_name(final_sentence)
