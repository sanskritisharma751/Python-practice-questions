from traceback import print_tb

MENU={
    'espresso':{'ingredients': {'water': 50, 'milk':0,'coffee': 18}, 'cost':50 },
    'latte':{'ingredients':{'water':200, 'milk':150, 'coffee':24 }, 'cost':100},
    'cappuccino':{'ingredients': {'water': 250, 'milk': 100, 'coffee': 24 }, 'cost': 150}
}
water_stock=0
milk_stock=0
coffee_stock=0
c=MENU['cappuccino']['ingredients']['coffee']
e=MENU['espresso']['ingredients']['coffee']
l=MENU['latte']['ingredients']['coffee']

wc=MENU['cappuccino']['ingredients']['water']
we=MENU['espresso']['ingredients']['water']
wl=MENU['latte']['ingredients']['water']

mc=MENU['cappuccino']['ingredients']['milk']
me=MENU['espresso']['ingredients']['milk']
ml=MENU['latte']['ingredients']['milk']

for inner_key,inner_value in MENU.items():
#      print(inner_key)
#      print(inner_value)
      water_stock+=inner_value['ingredients']['water']
      milk_stock += inner_value['ingredients']['milk']
      coffee_stock += inner_value['ingredients']['coffee']

print(f"Water Stock: {water_stock}ml")
print(f"Milk Stock: {milk_stock}ml")
print(f"coffee Stock: {coffee_stock}g")
def espresso():
    global water_stock,milk_stock,coffee_stock,coffee_machine_on
    water_used=MENU['espresso']['ingredients']['water']
    milk_used = MENU['espresso']['ingredients']['milk']
    coffee_used=MENU['espresso']['ingredients']['coffee']
    water_stock-=water_used
    milk_stock -= milk_used
    coffee_stock-=coffee_used
#    print("Your total is: ",water_stock)
#    print("Your total is: ",coffee_stock)
    coffee_machine_on = False
    return water_stock,milk_stock,coffee_stock

def latte():
    global water_stock,milk_stock,coffee_stock,coffee_machine_on
    water_used=MENU['latte']['ingredients']['water']
    milk_used=MENU['latte']['ingredients']['milk']
    coffee_used=MENU['latte']['ingredients']['coffee']
    water_stock-=water_used
    coffee_stock-=coffee_used
    milk_stock-=milk_used
    coffee_machine_on=False
    return water_stock,milk_stock,coffee_stock

def cappuccino():
    global water_stock,milk_stock,coffee_stock,coffee_machine_on
    water_used=MENU['cappuccino']['ingredients']['water']
    milk_used=MENU['cappuccino']['ingredients']['milk']
    coffee_used=MENU['cappuccino']['ingredients']['coffee']
    water_stock-=water_used
    coffee_stock-=coffee_used
    milk_stock-=milk_used
    coffee_machine_on=False
    return water_stock,milk_stock,coffee_stock

def report():
    global water_left,milk_left,coffee_left,coffee_machine_on
    water_left=water_stock
    milk_left=milk_stock
    coffee_left=coffee_stock
    return water_left,milk_left,coffee_left

def coins_return(n,m):
    change=m-n
    print(f"here is your change:{change}")


def check():
    global water_left,milk_left,coffee_left,coffee_machine_on
    if water_left < 0 or milk_left < 0  or coffee_left < 0:
        coffee_machine_on=False

coffee_machine_on=True
coins = 0
money=0
print(f"money ₹: {money}")
while coffee_machine_on:
    user = input('What would you like? (espresso/latte/cappuccino):')
    if user != 'report':
         coins = int(input("Enter the coins: "))
    if user == 'espresso' and coins >= MENU['espresso']['cost']:
        water_left,milk_left,coffee_left=espresso()
        coffee_machine_on = True
        check()
        if coins > MENU['espresso']['cost'] and coffee_machine_on:
            print("Here is your espresso ☕ Enjoy!")
            n=MENU['espresso']['cost']
            m=coins
            coins_return(n,m)
            money+=MENU['espresso']['cost']
        else:
            print(f"Sorry, we are out of stock, Money returned: {coins}")
    elif user == 'latte' and coins >= MENU['latte']['cost']:
        water_left,milk_left,coffee_left=latte()
        coffee_machine_on = True
        check()
        if coins > MENU['latte']['cost'] and coffee_machine_on:
            print("Here is your latte ☕ Enjoy!")
            n=MENU['latte']['cost']
            m=coins
            coins_return(n,m)
            money += MENU['latte']['cost']
        else:
            print(f"Sorry, we are out of stock, Money returned: {coins}")
    elif user == 'cappuccino' and coins >= MENU['cappuccino']['cost']:
        water_left,milk_left,coffee_left= cappuccino()
        coffee_machine_on = True
        check()
        if coins > MENU['cappuccino']['cost'] and coffee_machine_on:
            print("Here is your cappuccino ☕ Enjoy!")
            n=MENU['cappuccino']['cost']
            m=coins
            coins_return(n,m)
            money += MENU['cappuccino']['cost']
        else:
            print(f"Sorry, we are out of stock, Money returned: {coins}")
    elif user == 'report':
        water,milk,coffee=report()
        print(f"water left: {water}ml \nmilk left:{milk}ml \ncoffee left:{coffee}g \nmoney left ₹:{money}")
    else:
        coffee_machine_on=False

