# Here is the a concession stand program 
menu = {"chai":10,
        "biskit":10,
        "coffie":20,
        "popcorn":50,
        "samosa":15,
        "jalebi":20}
cart = []
total = 0 
print("------- MANU -------")
for key, value in menu.items():
    print(f"{key:10}:{value:.2f}")
print("--------------------")

while True :
    item = input("SElECT YOUR ITEMS (q to quit):").lower()
    if item == "q":
        break
    elif menu.get(item) is not None:
        cart.append(item)


for item in cart:
    total += menu.get(item)
    print(item,end=" ")

print()
print(f"Your total is :{total:.2f}")