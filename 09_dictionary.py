empty_dict = {}  # how to make an empty dictionary
marks = {
"aditi" : 100,
"sunidhi" : 99,

}
print(marks , type(marks))
print(marks['aditi'])

print(marks.items())
print(marks.keys())
print(marks.values())

#Diff btweeen get and [] operator
print(marks.get("aditi")) #it will give the value of the key if it is present in the dictionary otherwise it will return None
print(marks['aditi'])   #it will error if the key is not present in the dictionary


print(marks.pop("sunidhi"))
marks.update({"aditi" : 98,"swastik":100})
print(marks)


#PRACTICE PROBLEMS

#WAP TO DREACTE A DICT OF HINDI WORDS WITH TRANSLATION IN ENGLISH

words = {
"namaste" : "hello",
"shukriya" : "thank you",
"kripya" : "please",

}

word = input("enter a hindi word: ")
print(words[word])

#make an empty dict and take input from 4 friends with unique name , of their fav lang

languages = {}
name1 = input("enter your name: ")
lang1 = input("enter your fav lang: ")

languages.update({name1 : lang1})

name1 = input("enter your name: ")
lang1 = input("enter your fav lang: ")

languages.update({name1 : lang1})

name1 = input("enter your name: ")
lang1 = input("enter your fav lang: ")

languages.update({name1 : lang1})

name1 = input("enter your name: ")
lang1 = input("enter your fav lang: ")

languages.update({name1 : lang1})

print(languages)
