#program to check if user input is a leap year
input_year = int(input("Please Enter a Year of your Choice"))
def is_leap(year):
    #If year is divisible by 400 or divisible by 4 but not 100, it is a leap year
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else: return False

if is_leap(input_year):
    print(input_year, "It is a leap year")
else:
    print(input_year, "It is not a leap year")