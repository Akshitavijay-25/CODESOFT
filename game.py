import random
print("Welcome to the game")
print("Winning conditions")
print("rock vs paper->paper")
print("paper vs scissor->scissor")
print("scissor vs rock->rock")
print("enter your choice")
while True:
    print(" 1-Rock \n 2-Paper \n 3-Scissor")
    choice=int(input("enter the choice"))
    while choice > 3 or choice < 1:
        choice=int(input("enter the choice"))
    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name ="Paper"
    else:
        choice_name = "Scissors"
    print("users choice is " ,choice_name)               
    print("now its computers turn")
    comp_choice = random.randint(1, 3)
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'
    print("Computer choice is \n", comp_choice_name)
    print(choice_name, 'Vs', comp_choice_name)
    if choice == comp_choice:
        print('Its a Draw')
        result = "DRAW"
    if (choice == 1 and comp_choice == 2):
        print('paper wins =>')
        result = 'Paper'
    elif (choice == 2 and comp_choice == 1):
        print('paper wins =>')
        result = 'Paper'

    if (choice == 1 and comp_choice == 3):
        print('Rock wins =>\n')
        result = 'Rock'
    elif (choice == 3 and comp_choice == 1):
        print('Rock wins =>\n')
        result = 'RocK'

    if (choice == 2 and comp_choice == 3):
        print('Scissors wins =>')
        result = 'Scissors'
    elif (choice == 3 and comp_choice == 2):
        print('Scissors wins =>')
        result = 'Rock'
    if result == 'DRAW':
        print("<== Its a tie ==>")
    if result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break
print("thanks for playing")
