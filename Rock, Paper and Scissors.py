import random  
def main(): 
    win = int(0) 
    lose = int(0) 
    tie = int(0) 
    play_again = 'y' 
    while play_again == 'y': 
        print('Prepare to battle in a game of paper, rock, scissors!') 
        print('Please input the correct number according') 
        print('to the object you want to choose.') 
        computer_choice = get_computer_choice() 
        player_choice = get_player_choice() 
        print('Computer chose', computer_choice, '.') 
        print('You chose', player_choice, '.') 
        winner_result(computer_choice, player_choice) 
        play_again = input("Play again? Enter 'y' for yes or 'n' for no. ") 
    print(f"Your total wins are, {win},.") 
    print(f"Your total losses are,{lose},.") 
    print(f"Your total ties are,{tie}.") 
def get_computer_choice(): 
    choice = random.randint(1,3) 
    if choice == 1: 
        choice = 'ROCK' 
    elif choice == 2: 
        choice = 'PAPER' 
    else: 
        choice = 'SCISSORS' 
    return choice  
def get_player_choice(): 
    choice = int(input("Select rock(1), paper(2), or scissors(3): ")) 
    #Detect invalid entry
    while choice != 1 and choice != 2 and choice != 3: 
        print('The valid numbers are rock(type in 1), paper(type in 2),') 
        print('or scissors(type in 3).') 
        choice = int(input('Enter a valid number please: ')) 
    if choice == 1: 
        choice = 'ROCK' 
    elif choice == 2: 
        choice = 'PAPER' 
    else: 
        choice = 'SCISSORS' 
    return choice  
def winner_result(computer_choice, player_choice): 
    if computer_choice == player_choice:
        result = 'tie'
        print("It's a tie!")
    elif computer_choice == 'SCISSORS' and player_choice == 'ROCK':
        result = 'win'
        print('ROCK crushes SCISSORS! You win!')
    elif computer_choice == 'PAPER' and player_choice == 'SCISSORS': 
        result = 'win'
        print('SCISSORS cut PAPER! You win!')
    elif computer_choice == 'ROCK' and player_choice == 'PAPER': 
        result = 'win'
        print('PAPER covers ROCK! You win!')
    else: 
        result = 'lose'
        print('You lose!')
def result(winner_result):
    # For Result
    if result == 'win':
        win += 1
    elif result == 'lose':
        lose += 1
    else:
        tie += 1
main()
