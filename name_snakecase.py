#Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.
#Example:
#Input: jUAn DEla CrUZ
#Output: juan_dela_cruz
#Input name
name = input("Please enter your full name: ")
#Print name in snake casing
print(name.lower().replace(" ", "_"))
