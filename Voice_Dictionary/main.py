import pyttsx3
import wikipedia

# Create a variable to initialize pyttsx3 engine
engine = pyttsx3.init()

# Change the voice using setProperty method (0 - for Male, 1 - for female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

user_input = input("Enter the word you want to search: ")
engine.say(f"you chose to search the word{user_input} and the definition for the word is...")
searched_word = wikipedia.summary(user_input)
print(searched_word)
engine.say(searched_word)

# Execute the engine and wait
engine.runAndWait()

