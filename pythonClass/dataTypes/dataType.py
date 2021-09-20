# String is an array of characters
word = "Ubani is an insturctor in CODELAB"
v = 'Miracle'

# string slicing
access = word[5:10]
print(access)
print("agbaya")

subject = "Mathematics"

#string methods are used to format strings
#showing the datatype of the variable
print(type(subject))

#string count
nwss = subject.count("i")
print(nwss)
#positive indexing
newsubject = subject[3:6]
print(newsubject)

#negative indexing
result1 = "positivity"
result2 = result1[-7:-1]
print(result2)

#string as an array
news = subject[5]
print(news)

#string length method
newss = len(subject)
print(newss)

#string cases
#uppercase characters
newsss = subject.upper()
print(newsss)

#lowercase characters
nw = subject.lower()
print(nw)

#capatilize characters
nws = subject.capitalize()
print(nws)