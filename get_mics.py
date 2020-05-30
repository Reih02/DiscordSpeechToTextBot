import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()
print (sr.Microphone.list_microphone_names())

end = input()
