from .i_display import IDisplay


class WordDisplayer(IDisplay):
    def show(word):
        print(f"Word: {word.word}")
        print(f"IPA: {word.ipa}")
        print("\n")

        word.sound.play()
        print("\n")

        for sense in word.senses:
            print(f"Definition: {sense.definition}")
            print(f"Example: {sense.example}")
            print(f"My Example: {sense.my_example}")
            print(f"-------------------------------")
