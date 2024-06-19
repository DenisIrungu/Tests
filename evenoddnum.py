#Write a program to print the given number is odd or even.
while True:
    try:
        number = int(input ("Enter a number "))
        break
    except ValueError:
        print ("Invalid number. Please enter a valid number")
    
if number % 2 == 0:
    print (" The number is an Even number")
else:
    print ("The number is an Odd number")

