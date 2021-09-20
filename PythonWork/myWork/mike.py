students = {}
def Average(lst):
    return sum(lst)/len(lst)
while True:
    name = input("enter your name:")
    score = int(input("enter your score:"))

    students[name] = score

    repeat = input("would you like to add another student?" "(yes/no)")
    if repeat == 'no':
     break

print("-------RESULT-------")

for name,score in students.items():
    print(name, "your score is: ", score)

avg = Average(students.values())
highest = max(students, key=students.get)
lowest = min(students, key=students.get)

print('avg:', avg)
print('highest:', highest)
print('lowest:', lowest)