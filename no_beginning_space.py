#Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.
#Example:
#Input:         Juan Dela Cruz
#Output: Juan Dela Cruz
#Input name
name = input("Please enter your full name: ")
#Print without beginning in spaces
print(name.strip())
