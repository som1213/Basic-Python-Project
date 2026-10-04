# using sting indexing e mail slicer program  
mail = input("Enter your E mail :")
index = mail.index("@")
username = mail[:index]
domain = mail[index+1:]
print(f"Your username {username} and the domain is {domain} ")