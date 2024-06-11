print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+      The Ice Cream Shop       +")
print("+            Welcome            +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")

container = input("What type of ice cream container would you like: cup or cone? ")
while container!="cup" and container!="cone":
  print("Invalid answer please try again!")
  container = input("What type of ice cream container would you like: cup or cone? ")

scoops = input ("How many scoops would you like, 1-4? ")
while scoops not in ["1","2","3","4"]:
  print ("Invalid choice, please try again")
  scoops = input ("How many scoops would you like, 1-4? ")

toppings = input ("Which topping would you like? ")
while True:
    if toppings == "Flake":
        print ("Flake added")
        break
    elif toppings == "Chocholate Sprinkle":
       print ("chocolate Sprinkle")
       break
    elif toppings == "Strawberry Coulis":
       print ("strawberry coulis added")
       break
    else:
       print("Invalid topping, please try again")
       toppings = input ("Which topping would you like? ")
scoops = int(scoops)
def calculate_total_price ():
   cost = 0.0
   cost += 1.0
   cost += scoops * 1.0
   
   if toppings == "Flake":
      cost += 0.5
   elif toppings == "Chocholate Sprinkle":
      cost += 0.3
   elif toppings == "Strawberry Coulis":
      cost += 0.8
   return cost
total_cost = calculate_total_price()
print (f"The total cost is: {total_cost}")