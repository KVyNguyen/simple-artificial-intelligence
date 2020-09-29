from __future__ import print_function
import speech_recognition
import pyttsx3
from datetime import date, datetime


robotEar = speech_recognition.Recognizer()
robotMouth = pyttsx3.init()
robotBrain = ""

while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robotEar.listen(mic)
    try:
        you = robotEar.recognize_google(audio)
    except Exception as e:
        you = ""
        print("Exception: " + str(e))
    print("User: " + you)

    if you == "":
        robotBrain = "I can't hear you, try again"
    elif "hello" in you:
        robotBrain = "Hello V"
    elif "today" in you:
        today = date.today()
        robotBrain = today.strftime("Today is %B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robotBrain = now.strftime("%H hours %M minutes %S seconds")
    elif "bye" in you:
        robotBrain = "Bye V"
        print("Robot: " + robotBrain)
        voices = robotMouth.getProperty('voice')
        voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        robotMouth.setProperty('voice', voice_id)
        robotMouth.say(robotBrain)
        robotMouth.runAndWait()
        break
    else:
        robotBrain = "I don't understand what you say, try again"

    print("Robot: " + robotBrain)
    voices = robotMouth.getProperty('voice')
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    robotMouth.setProperty('voice', voice_id)
    robotMouth.say(robotBrain)
    robotMouth.runAndWait()