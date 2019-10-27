from os import listdir, getcwd
from os.path import join
import re
import string


def clean_text(_text):
    _text = _text.translate(str.maketrans('', '', string.punctuation))
    _text = re.sub('[0-9]', ' ', _text).lower()
    _text = re.sub(' +', ' ', _text).lower()
    _text = re.sub(' \n', ' ', _text).lower()
    return _text


def get_data():
    relative_test_data_path = "resources\\test_data"
    test_data_path = join(getcwd(), relative_test_data_path)

    labels = open("resources\\labels_train.txt", "r")
    data = []

    # temporary limit
    limit = 100

    for f in listdir(test_data_path):
        text = open(join(relative_test_data_path, f), "r", encoding="utf8").read()
        text = clean_text(text)
        label = labels.readline()
        data.append([text, int(label)])
        limit = limit - 1
        if limit == 0:
            break

    labels.close()
    return data
