import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()
print (sr.Microphone.list_microphone_names())
device = int(input("Please enter the index of the audio device you wish to use: "))

while True:
    with sr.Microphone(device_index=device) as source:
        print('Say something: ')
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print('You said: {}'.format(text))
            f = open("speech.txt", "w")
            f.write(text)
            f.close()

        except:
            print("Sorry, couldn't recognise that..")

end = input()
