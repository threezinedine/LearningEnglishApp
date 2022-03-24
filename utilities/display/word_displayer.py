from .i_display import IDisplay
from data import Sound


class WordDisplayer(IDisplay):
    @classmethod
    def __show_sense(cls, sense):
        print(f"----------------------")
        for key, value in sense.items():
            print(f"\t{key}: {value}")
        print("-----------------------")

    def show(cls, word):
        """
            Show the word information 
            
            Parameters
            ----------
                word: Word object
        """
        word_properties = word.properties

        for key in word_properties.keys():
            if key == "senses":
                print("Senses:")
                for sense in word_properties["senses"]:
                    cls.__show_sense(sense)
            else:
                print(f"{key}: {word_properties[key]}")
