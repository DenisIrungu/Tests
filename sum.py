#Write a program to find the sum of two numbers.
try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid number. Please enter valid numbers.")

def find_sum ():
   return number1 + number2
   
sum = find_sum ()
print (f"Sum = {sum}")