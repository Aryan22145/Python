import nltk
from nltk.corpus import words

# Download the word corpus if not already downloaded
nltk.download('words')

# Get the list of words
word_list = words.words()

# Check the total number of words in the list
total_words = len(word_list)
print(f"Total words available: {total_words}")

# If there are fewer than 100,000 words, duplicate the list until you reach 100,000
if total_words < 100000:
    factor = 100000 // total_words + 1
    word_list = (word_list * factor)[:100000]

# Trim the list to exactly 100,000 words
word_list = word_list[:100000]

# Print the first 10 words to verify
print(word_list[:100000])
