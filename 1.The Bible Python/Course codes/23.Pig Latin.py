#####################################
########### Pig Latin ###############
#####################################

#Get sentence from user
original = raw_input("Please enter a sentence: ").strip().lower()

#Split sentence into words
words = original.split()

#loop throught works and convert to pig latin
new_words = []

for word in words:
    #If starts with vowel,just add "yay"
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        #Otherwise, move the first consonant cluser to end, and add "ay"
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)
        
#Stick words back together

output =" ".join(new_words)

#output the final string

print(output)
