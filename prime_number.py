#Write a program to find if the given number is prime or not.
def is_prime (number):
    if number <= 1:
        return False
    
    for x in range(2, int(number**0.5+1)):
        if number % x == 0:
            return False
    return True

while True:
    user_input = input("Enter a number or press 'q' to exit: ")

    if user_input.lower() == "q":
        break

    try:
        number = int(user_input) 
        if is_prime(number):
            print (f"{number} is a prime number")
        else:
            print(f"{number} is not a prime number")
        
    except ValueError:
        print( "Invalid input. Please enter a valid number or press 'q' to exit")

