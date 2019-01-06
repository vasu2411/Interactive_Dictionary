import json

#load JSON data
data = json.load(open("data.json"))

#take word from user
word = input('Enter word: ')

#function to return meaning of the word from data
def getMeaning(w):
    return data[w]

#function call to get meaning of the word entered by user
meaning = getMeaning(word)

#printing meaning of the word in console
print("Meaning :" ,meaning)