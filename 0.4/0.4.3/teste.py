
"""
from tts_watson.TtsWatson import TtsWatson

ttsWatson = TtsWatson('watson_user', 'watson_password', 'en-US_AllisonVoice') 
ttsWatson.play("Hello World")


curl -X POST -u "apikey:idnf9yiSebU-xfW8YqVW6MStSoDgIVjzVHg9OwvybYFd" \
--header "Content-Type: application/json" \
--header "Accept: audio/wav" \
--data "{\"text\":\"hi, how are you today?\"}" \
--output teste.wav \
"https://gateway.watsonplatform.net/natural-language-understanding/api/v1/synthesize"

"""
"""
import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
	if (voice.gender != 'male'):

		print("Voice:")
		print(" - ID: %s" % voice.id)
		print(" - Name: %s" % voice.name)
		print(" - Languages: %s" % voice.languages)
		print(" - Gender: %s" % voice.gender)
		print(" - Age: %s" % voice.age)
"""
from playsound import playsound
playsound('audios/hello.mp3')
