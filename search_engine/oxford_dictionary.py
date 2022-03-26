from .i_dictionary import IDictionary
from data import Word, WordType
import requests
import jsons


class OxfordDictionary(IDictionary):
    """
        Class uses the API, that provided by OxfordDictionary, to return the word.
    """
    @classmethod
    def get_json_result(cls, word):
        """
            The method to get raw json result from OxfordDictionary's API.

            Paramters
            ---------
                word: string
                    The word that you wanna search.

            Returns
            -------
                result: json 
                    The json data object from the OxfordDictionary
        """
        app_id = "be5f29eb"
        app_key = "2939a69beb531e9f226addd8161cbdeb"
        language = "en-gb"

        url = 'https://od-api.oxforddictionaries.com/api/v2/entries/'  + language + '/'  + word.lower()
        result = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})

        return result.json()

    def search_word(cls, word_str):
        """
            The main functionality that return the word the you searched.

            Paramters
            ---------
                word_str: string
                    The word that you wanna search.

            Returns
            -------
                words: Word[*]
                    The list of Word objects that store information about this word.
        """
        result = cls.get_json_result(word_str)
        words = []

        if 'error' in result.keys():
            return None

        
        for entries in result['results'][0]['lexicalEntries']:
            properties = {}
            data = entries['entries'][0]
            pronunciation= data['pronunciations'][0]

            properties["word"] = word_str
            properties["sound"] = pronunciation['audioFile']
            properties["ipa"] = pronunciation['phoneticSpelling']
            properties["word_type"] = WordType.return_type(entries['lexicalCategory']['text']).value

            data_senses = data['senses']
            senses = []
            for data_sense in data_senses:
                keys = data_sense.keys()
                if "definitions" in keys and "examples" in keys:
                    sense = {"definition": data_sense['definitions'][0],
                            "example":data_sense['examples'][0]['text'], 
                            "my_example":""}
                    senses.append(sense)

            properties["senses"] = senses

            word = Word(properties)
            words.append(word)

        return words
