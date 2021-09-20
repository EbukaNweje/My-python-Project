#string is an array of characters
word='Ubani is an instructor in CODELAB'
subject= 'mathematics'

#string methods are used to format strings
#showing the datatype of the variable
print(type(subject))

#string slicing
#positive indexing
newword= word[5:16]
allword = word[:]

#negative indexing
result1= 'positive'
result2= result1[-7:-3]
print(result2)

#string as an array
newsubject= subject[4]
print(newsubject)

#string lenght method
newsubject= len(subject)
print(newsubject)

#string cases
#upper case characters
newsubject1= subject.upper()
print(newsubject1)

#Lower Case Characters
newsubjec=subject.lower()
print(newsubject)

#capitalize Characters
newsubject= subject.capitalize()

#string count
newsubject= subject.count('m')
print(newsubject)

