# Install an external module and use it to perform an operation of your interest.

import pyttsx3  # this is an external module

engine = pyttsx3.init()

engine.say("hello everyone my name is raul")
engine.runAndWait()

# run the code and listen whatever you write in this engine.say portion.