questions = ("How many elements in their prodic table :",
            "Which animal lays the largest eag :",
            "What is the most abuntdant gas in earth's atomosphare :",
            "How many bones are in their in humen body :",
            "Which planet in the solar system is the hottest :")

options = (("A. 116" ,"B. 117" ,"C. 118" ,"D. 119" ),
           ("A. Whale" ,"B. crocodile" ,"C. Elephant" ,"D. Ostrich" ),
           ("A. Nitrogen" ,"B. oxygen" ,"C. Carbon-duoxied" ,"D. Hydrogen" ),
           ("A. 206" ,"B. 207" ,"C. 208" ,"D. 209" ),
           ("A. Mercury" ,"B. Venus" ,"C. Earth" ,"D. Mars" ))

answers = ("C", "D", "A", "A", "B")
guesses = []
question_num = 0
score = 0

for question in questions:
    print("------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)    
    guess = input("Enter (A ,B ,c ,D):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score +=1
        print("CORRECT !")
    else:
        print("INCORECT !")
        print(f"{answers[question_num]} is corect answer ")

    question_num += 1

print("-----------------------------------")
print("---------------RESULT--------------")
print("-----------------------------------")

print("answer : ",end=" ")

for answer in answers:
    print(answer,end=" ")
print()
 
print("Guesses :",end=" ")
for guess in guesses:
    print(guess,end=" ")
print()

score = int(score/len(questions)*100)
print(f"Your score is {score}%")