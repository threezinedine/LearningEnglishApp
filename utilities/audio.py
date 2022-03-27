import requests
from pygame import mixer
import os
from time import sleep


def play_url(url, save_folder):
    response = requests.get(url)
    with open(os.path.join(save_folder, 'sound.mp3'), 'wb') as file:
        file.write(response.content)

    mixer.init() 
    mixer.music.load(os.path.join(save_folder, 'sound.mp3'))
    mixer.music.play()
    sleep(2)
    mixer.quit()
