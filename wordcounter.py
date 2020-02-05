#!/usr/bin/python

print("Welcome to word counter!")
fileInput = input("Enter a file name: ")

numWords = 0

with open(fileInput,"r") as doc:
    for words in doc:
        wordList = words.split()
        numWords += len(wordList)
        

    
print("Number of words: %i"  % numWords)