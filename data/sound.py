class Sound:
    """
        The class stores link for the sound file.

        Parameters
        ----------
            url: string
                The link of the sound.
    """
    def __init__(self, url):
        self.__url = url

    @property
    def url(self):
        return self.__url

    def play(self):
        """
            Play the sound.
        """
        print(f"Playing sound ({self.__url})...")
