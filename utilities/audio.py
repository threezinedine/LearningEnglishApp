import urllib
from pydub import AudioSegment
from pydub.playback import play


def play_url(url):
    mp3file = urllib.request.urlopen(url)
    with open('utilities/test.mp3','wb') as output:
      output.write(mp3file.read())

    song = AudioSegment.from_mp3("utilities/test.mp3")
    play(song)
