Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> year = int(input("Enter a year: "))

if year <= 1582:
    print("Not within the Gregorian calendar period")
elif year % 4 != 0:
    print("it's a common year")
elif year % 100 != 0:
    print("it's a leap year")
elif year % 400 != 0:
    print("it's a common year")
else:
    print("it's a leap year")