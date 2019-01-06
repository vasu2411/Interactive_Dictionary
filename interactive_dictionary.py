import json

#load JSON data
data = json.load(open("data.json"))

#take word from user
word = input('Enter word: ')

#function to return meaning of the word from data
def getMeaning(w):
    #for case sensitivity
    w = w.lower()
    #if-else to check word exist in our data or not
    if w in data:
        return data[w]
    else:
        return "The word doesn't exist. Please double check it."

#function call to get meaning of the word entered by user
meaning = getMeaning(word)

#printing meaning of the word in console
print(meaning)