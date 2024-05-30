#Slicer
# variable[start:end:step]

#Create string
word = "supercalificacionchida"

#Take "super"
word_sup = word[0:5:1]
print(word_sup)

#Take "super" in another way
word_sup2 = word[:5]
print(word_sup2)

#Take "chida" using index instead of numbers
word_chi = word[word.index("chi"):]
print(word_chi)

#Take "calificacion"
word_cali = word[word.index("cali"):word.index("chi")]
print(word_cali)
