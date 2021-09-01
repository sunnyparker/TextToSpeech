#import library
import  pyttsx3
#open file
file=open("myfile.txt")
#reading file
read=file.read()
#initializing speaker
speaker=pyttsx3.init()
#speech
speaker.say(read)
#runAndWait
speaker.runAndWait()