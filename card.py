odd_digits = 0
even_digits = 0 
tota = 0
# Step 01
cradit_card_number = input("Enter your cradit card number :")
cradit_card_number = cradit_card_number.replace("_","")
cradit_card_number = cradit_card_number.replace(" ","")
cradit_card_number = cradit_card_number[::-1]
# Step 02
for x in cradit_card_number[::2]:
    odd_digits += int(x)
    break
for x in cradit_card_number[1::2]:
    x = int(x)*2
    if x>=10 :
        x = 1+(x%10)
    even_digits += x
# step 03
total = odd_digits + even_digits
if total%10==0:
    print("VALID")
else:
    print("INVALID")