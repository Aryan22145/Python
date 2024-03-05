import pyttsx3
import wikipedia

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

user_input = input("Enter the word you want to search: ")
engine.say(f"you chose to search the word{user_input} and the definition for the word is...")
searched_word = wikipedia.summary(user_input)
print(searched_word)
engine.say(searched_word)

engine.runAndWait()

