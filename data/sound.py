from utilities import play_url, create_folder_if_not_exist


class Sound:
    """
        The class stores link for the sound file.

        Parameters
        ----------
            url: string
                The link of the sound.
    """
    sound_folder = "sound"
    create_folder_if_not_exist(sound_folder)

    def __init__(self, url):
        self.__url = url

    @property
    def url(self):
        return self.__url

    def play(self):
        """
            Play the sound.
        """
        if self.url is not None:
            play_url(self.url, self.sound_folder)
