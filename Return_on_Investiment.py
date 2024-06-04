total_cost = input("\nEnter the Total Cost: ")
total_sales = input ("\nEnter the Total Sales: ")
x = int(total_cost)
y = int (total_sales)
def calculate_profit_loss ():
    profit_loss = y - x
    if x >y:
        print (f"\nYou made a loss of: {profit_loss*-1}")
    else:
        print (f"\nYou made a profit of: {profit_loss}")

    return_on_investment = (profit_loss/x)* 100
    r_o_i = int(return_on_investment)
    if r_o_i == -(-r_o_i):
        print (f"\nYour R.I.O is: {r_o_i*-1}% loss")
    else:
        print (f"\nYour R.I.O is: {r_o_i}% profit")

calculate_profit_loss()
