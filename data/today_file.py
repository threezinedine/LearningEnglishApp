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
        self.__properties = new_properties
