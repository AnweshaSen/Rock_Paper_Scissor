import random

user_choice = 0
comp_choice = 0

def user_choose():
    print("")
    choice = input("Choose any one from Rock[r/R], Paper[p/P], Scissor[s/S]:  ")
    if choice in ["Rock", "r", "rock", "ROCK", "R"]:
        choice = "r"

    elif choice in ["Paper", "p", "paper", "PAPER", "P"]:
        choice = "p"

    elif choice in ["Scissor", "s", "scissor", "SCISSOR", "S"]:
        choice = "s"

    else:
        print("Please enter from the given.....")
        user_choose()

    return choice

def comp_choose():
    print("")
    choice = random.randint(1,3)
    if choice == 1:
        choice = "r"

    if choice == 2:
        choice = "p"

    if choice == 3:
        choice = "s"

    return choice

while True:
    print("")
    choice1 = user_choose()
    choice2 = comp_choose()
    print("")

    if choice1 == "r":
        if choice2 == "r":
            print("Your choice is: Rock\nComputer's choice is: Rock\nSo no points for this round ;)") 
        elif choice2 == "p":
            print("Your choice is: Rock\nComputer's choice is: Paper\nSo you loose :(")
            comp_choice +=1
        elif choice2 == "s":
            print("Your choice is: Rock\nCompuetr's choice is: Scissor\nSo you win :)")
            user_choice +=1        

    if choice1 == "p":
        if choice2 == "p":
            print("Your choice is: Paper\nComputer's choice is: Paper\nSo no points for this round ;)")
        elif choice2 == "r":
            print("Your choice is: Paper\nComputer's choice is: Rock\nSo you win :)")
            user_choice +=1
        elif choice2 == "s":
            print("Your choice is: Paper\nComputer's choice is: Scissor\nSo you loose :(")  
            comp_choice +=1

    if choice1 == "s":
        if choice2 == "s":
            print("Your choice is: Scissor\nComputer's choice is: Scissor\nSo no points for this round ;)")
        elif choice2 == "r":
            print("Your choice is: Scissor\nComputer's choice is: Rock\nSo you loose :(")
            comp_choice +=1
        elif choice2 == "p":
            print("Your choice is: Scissor\nComputer's choice is: Paper\nSo you win :)")
            user_choice +=1

    print("")
    print("Score=========>>>>>>>>\nUser -> {0}\nComputer -> {1}".format(str(user_choice),str(comp_choice)))
    choice3 = input("Continue[y/n]?")  
    if choice3 == "y":
        pass
    elif choice3 == "n":
        print('Final score:\n  User: {0}\n  Computer: {1}'.format(str(user_choice), str(comp_choice)))
        if (user_choice > comp_choice):
            print('Conrats, you won!')
        else:
            print('Better luck next time.')
        break
    else:
        print('Final score:\n  User: {0}\n  Computer: {1}'.format(str(user_choice), str(comp_choice)))
        if (user_choice > comp_choice):
            print('Conrats, you won!')
        else:
            print('Better luck next time.')
        break                                         
