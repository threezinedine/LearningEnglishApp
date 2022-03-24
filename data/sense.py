class Sense:
    """
        Class stores a common sense of a word

        Parameters
        ----------
            definition: string
                The definition of the word.

            example: string
                A basic example of the word
            
            my_example: string
                The example that user can set.
    """
    def __init__(self, definition, example):
        self.__definition = definition
        self.__example = example
        self.__my_example = ""

    @property
    def definition(self):
        return self.__definition

    @property
    def example(self):
        return self.__example

    @property
    def my_example(self):
        return self.__my_example

    def add_new_example(self, added_example):
        """
            Add example for this sense.

            Parameters
            ----------
                added_example: string
                    The sentence that user take for this word.
        """
        self.__my_example = added_example
