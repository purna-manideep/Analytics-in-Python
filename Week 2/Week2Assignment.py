# -*- coding: utf-8 -*-
def word_distribution(string):
    # your code here
    result = {}
    word = string.lower()
    temp_word = ""
    for i in word:
        if i == " ":
            temp_word += " "
        elif i == "’":
            temp_word += "’"
        else: 
            if i.isalpha():
                temp_word += i   
    result = {}
    for i in temp_word.split():
        result[i] = result.get(i,0)+1    
    return result
    
#word_distribution("Hello. How are you? Please say hello if you don’t love me!")