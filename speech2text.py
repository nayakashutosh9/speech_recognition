import speech_recognition as sr

r1 = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak anything")
    audio = r1.listen(source)
    try:
        text = r1.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")
