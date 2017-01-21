# IoT-weather
Python script that uses Text-To-Speech to say the current weather in specified location. Edit `settings.py` for desired location (lat/long) and use your `Dark Sky API` key (easily create a free account https://darksky.net/dev/). Tested on Raspberry Pi 3 (Raspbian).


## How It Works
1. Raw weather data is pulled from `Dark Sky API` via HTTP request
2. Friendly summary is formated from raw data
2. `gTTS` is used to generate `.MP3` audio file from text
3. `mpg123` plays generated file

Check `output-example/` to hear how it sounds.


## System Requirements
* Linux
* Python 3
* Internet connection
* Audio output


## Setup
System dependency: (Debian/Raspbian/Ubuntu)
```
sudo apt install mpg123
```

Setup a virtual environment:
```
sudo pip3 install virtualenv
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
```


## Run
```
python3 main.py

[SPEECH] Checking weather...
Requesting weather...
Generating weather speech...
[SPEECH] Now it's Partly Cloudy, with temperature of 3 degrees.
```
