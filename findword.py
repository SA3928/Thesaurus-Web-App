import json
from difflib import get_close_matches



class wordsearch():
    def __init__(self, dataset) :
        self.dataset = json.load(open(r"C:\Users\srija\AppData\Local\Programs\Python\Python38\venv1\Scripts\first_app\thesaurus_data.json"))

    def search(self, word) :
        dataset = json.load(open(r"C:\Users\srija\AppData\Local\Programs\Python\Python38\venv1\Scripts\first_app\thesaurus_data.json"))
        if word in dataset :
            return dataset[word]
        elif word.title() in dataset:
            return dataset[word.title()]
        elif word.upper() in dataset :
            return dataset[word.upper()]
        elif len(get_close_matches(word, dataset.keys()))>0 :
            return dataset[get_close_matches(word, dataset.keys())[0]]
        else :
            return "We did not understand your query. This may not be an English word."