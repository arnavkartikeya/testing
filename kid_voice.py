import discord.voice_client
import speech_recognition as sr

def get_text():
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    with mic as source:
        #r.adjust_for_ambient_noise(source, 1)
        audio = r.listen(source)
    try:
        message = str(r.recognize_google(audio))
    except:
        message = ""