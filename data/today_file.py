from utilities import date


class TodayFile:
    def __init__(self, properties):
        self.__properties = properties

    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, new_properties):
        if 'review_done' not in new_properties.keys():
            raise ValueError(f"The 'review_done' key must appear in the new_properties.")
        elif 'words' not in new_properties.keys():
            raise ValueError(f"The 'words' key must appear in the new_properties.")
        self.__properties = new_properties

    def __del_word_in_list(self):
        if len(self.__properties['words']) >= 1:
            self.__properties['words'] = self.__properties['words'][:-1]
            if len(self.__properties['words']):
                self.__properties['review_done'] = True

    def get_word(self):
        return self.__properties['words'][-1]

    def has_review_done(self):
        return self.__properties['review_done']
