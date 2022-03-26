from .i_display import IDisplay
from data import Sound


class GraphicDisplayer(IDisplay):
    def __init__(self, frames_dict):
        self.frames_dict = frames_dict

    def show(self, word):
        for key in word.properties.keys():
            if key == "sound":
                pass
            elif key != "senses":
                frame = self.frames_dict[key]
                frame.setText(word[key])
            else:
                for frames, sense in zip(self.frames_dict["senses"], word["senses"]):
                    for key in sense.keys():
                        frames[key].setText(sense[key])
