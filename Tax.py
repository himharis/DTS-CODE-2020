Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> income = float(input("Enter the annual income: "))

#first schema
if income < 0:
    tax = float(0)
elif income < 85528:
    tax = ((18 * income / 100) - 556.2)
else:
   tax = 14839.2 + 32 * (income - 85528) / 100

tax = round(tax, 0)
print("The tax is:", tax, "thalers")