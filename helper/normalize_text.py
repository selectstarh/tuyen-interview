import string
from nltk.stem.porter import *

def normalize_word(word):
    ps = PorterStemmer()
    word = word.lower()
    word = word.translate(str.maketrans('', '', string.punctuation))
    word = ps.stem(word)

    return word

def normalize_text(text):
    words = text.split('-')
    result = []

    for word in words:
        result.append(normalize_word(word))

    return result
