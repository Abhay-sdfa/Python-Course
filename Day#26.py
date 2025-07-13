# Exercise 2: Solution
import time
import pyttsx3

print(time.strftime("%H:%M:%S"))

engine = pyttsx3.init()         # Initialize the TTS engine
engine.setProperty('rate',120)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

current_time=time.strftime("%H:%M:%S")

if "00:00:00"<current_time<"12:00:00" :
    engine.say("GOOD MORNING SIR")
    engine.runAndWait()             # Run the speech engine

    print("GOOD MORNING SIR :)") 

elif "12:00:00"<current_time<"18:00:00" :
    engine.say("GOOD AFTERNOON SIR")
    engine.runAndWait()             # Run the speech engine

    print("GOOD AFERNOON SIR :)")

elif "18:00:00"<current_time<"22:00:00" :
     engine.say("GOOD EVENING SIR")
     engine.runAndWait()            # Run the speech engine

     print("GOOD EVENING SIR :)")

elif "22:00:00"<current_time<"00:00:00" :
    engine.say("GOOD NIGHT SIR")
    engine.runAndWait()             # Run the speech engine
    
    print("GOOD NIGHT SIR :)")
'''
'''