#!/usr/bin/env python3

def return_evens(num_list):
   return [list for list in num_list if list % 2 == 0]

result_evens = return_evens([0, 1, 3, 5, 7, 8, 9])
print(result_evens)

def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list]

exclamation = make_exclamation(["Hello", "I'm doing great", "Python is fun"])
print(exclamation)