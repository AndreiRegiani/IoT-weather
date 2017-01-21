#!/usr/bin/env python3
import os

import requests
from gtts import gTTS

import settings


def main():
    say_loading()
    speech = get_weather()
    if speech:
        say_weather(speech)


def get_weather():
    url_params = {
        'api': settings.DARKSKY_API,
        'key': settings.DARKSKY_KEY,
        'lat': settings.MY_LATITUDE,
        'long': settings.MY_LONGITUDE,
        'unit': 'si' # metric system instead of imperial unit (default)
    }

    url = "{api}/{key}/{lat},{long}?units={unit}".format(**url_params)
    print("Requesting weather...")
    r = requests.get(url)
    if r.status_code != 200:
        print("Error while requesting weather")
        return False

    data = r.json()
    now_summary = data['currently']['summary']
    now_degrees = data['currently']['temperature']
    later_summary = data['hourly']['summary']

    speech = "Now it's {}, with temperature of {:.0f} degrees.".format(now_summary, now_degrees)
    return speech


def say_loading():
    speech = "Checking weather..."
    print("[SPEECH]", speech)
    filename = 'loading.mp3'
    if not os.path.isfile('./' + filename):
        print("Generating: " + filename)
        tts = gTTS(text=speech, lang='en').save(filename)
    play_sound(filename)


def say_weather(speech):
    filename = 'weather.mp3'
    print("Generating weather speech...")
    tts = gTTS(text=speech, lang='en').save(filename)
    print("[SPEECH]", speech)
    play_sound(filename)


def play_sound(filename):
    """ Helper function to play audio files in Linux """
    play_cmd = "mpg123 {} {} ./{}".format('--quiet --pitch', settings.VOICE_PITCH, filename)
    os.system(play_cmd)


if __name__ == '__main__':
    main()
