from .i_display import IDisplay


class GraphicDisplayer(IDisplay):
    def __init__(self, word, api, definitions, sentences):
        self.__word = word 
        self.__api = api 
        self.__definitions = definitions
        self.__sentences = sentences

    def show(self, word):
        self.__word.setText(f"{word.word}({word.word_type.value})")
        self.__api.setText(word.ipa)

        for index, sense in enumerate(word.senses):
            definition = self.__definitions[index]
            sentence = self.__sentences[index]

            definition.setText(sense.definition)
            sentence.setText(sense.example)
            
