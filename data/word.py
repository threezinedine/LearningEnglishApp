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
    def __init__(self, properties):
        self.__properties = properties

    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, new_properties):
        self.__properties = new_properties

    def save(self, database):
        """
            The save method that will store the database (inherited from IDatabase class)

            Parameters
                database: IDatabase
                    The database in which that word is stored. 
        """
        folder = database.folder
        
        with open(os.path.join(folder, self.__properties['word']), 'w', encoding='utf-8') as file:
            file.write(json.dumps(self.__properties))
