import requests
import pygame


class TranslateTTS:

    TTS_API = "https://translate.google.com/translate_tts"

    def __init__(self):
        pass

    def speak(self, msg, lang_code='th-TH'):
        r = requests.get(self.TTS_API, params={
            'q': msg,
            'tl': lang_code,
            'ie': 'UTF-8',
            'client': 'tw-ob',
        })
        return r

    def save_mp3(self, msg, lang_code='en', out_mp3='out.mp3'):
        r = self.speak(msg, lang_code)
        with open(out_mp3, 'wb') as f:
            f.write(r.content)


if __name__ == "__main__":

    msg = "Hello, this is a navigation robot. may i help you?"

    tts = TranslateTTS()
    tts.save_mp3(msg)

    clock = pygame.time.Clock()
    pygame.mixer.init()
    pygame.mixer.music.load('out.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        # print("Playing...")
        clock.tick(1000)
