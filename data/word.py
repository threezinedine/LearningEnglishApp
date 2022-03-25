import json
import os


class Word:
    """
        The class stores all information of the word (include ipa, ...)

        Parameters
        ----------
            properties: Map
                The map stores all information of the word.
    """
    @staticmethod
    def word_from(properties):
        """
            The method initialize the Word object from a certain properties map.

            Parameters
            ----------
                properties: map
                    The properties of the word.
        """
        word = Word({})
        word.properties = properties
        return word

    def __init__(self, properties):
        self.__properties = properties

    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, new_properties):
        self.__properties = new_properties

    def __getitem__(self, item):
        return self.__properties[item]
