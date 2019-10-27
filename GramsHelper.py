from nltk import ngrams


def generate_char_k_gram(_k, _text):
    kgrams = list(ngrams(_text, _k))
    result = []
    for k_tuple in kgrams:
        current_kgram = ""
        for letter in k_tuple:
            current_kgram = current_kgram + letter
        result.append(current_kgram)
    return result

