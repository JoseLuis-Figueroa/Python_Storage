####################################
############## For #################
####################################
vowels=0
consonants=0

word = input("Write a word to get vowels and consonants ").strip().capitalize()

for letter in word:
    if letter.lower() in "aeiou":
        vowels+=1
    elif letter == "":
        pass
    else:
        consonants+=1

print("There are {} vowels.".format(vowels))
print("There are {} consonants.".format(consonants))


