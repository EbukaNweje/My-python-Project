students = {}
while True:
    username = input("what is student name:")
    score = int(input("what is the score:"))

    students[username] = score


    repeat = input("Would you like to add another student" " (Yes/no):")
    if repeat == "no":
     break
print("RESULT")

for username,score in students.items():
    print(username, "your score is: ", score)

highest = max(students, key=students.get)
lowest = min(students, key=students.get)

print("Highest:", highest)
print("Lowest:", lowest)
