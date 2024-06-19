#Write a program to find the given number is positive or negative.
while True:
    try:
        number = int(input ("Enter a number: "))
        break
    except ValueError:
        print ("Invalid input. Please enter a valid number.")

if number > 0:
    print ("This number is a positive number")

elif number < 0:
    print ("This number is a negative number")

else:
    print ("This number is 0")