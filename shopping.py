foods = []
prices = []
total = 0
while True:
    food = input("EMter your food (q to quit) :")
    if food == "q":
        break
    else:
        price = float(input(f"Enter prices of {food} :"))
        foods.append(food)
        prices.append(price) 

print("----- Shopping cart -----")
for food in foods:
    print(food,end=" ")
for price in prices:
    total += price

print()
print(f"your total is :{total}")