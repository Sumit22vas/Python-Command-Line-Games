import random

# function to print message
def welcome_msg():
    print("*"*30)
    print(f"{'*'.ljust(5)}{'welcome'.upper().center(20)}{'*'.rjust(5)}")
    print(f"{'*'.ljust(5)}{'to'.upper().center(20)}{'*'.rjust(5)}")
    print(f"{'*'.ljust(5)}{'guess my number'.upper().center(20)}{'*'.rjust(5)}")
    print("*"*30)

def play_guess_my_number():

    game_count = 0
    player_wins = 0
    computer_wins = 0

    def start_game(player_name = 'Player'):
        nonlocal game_count
        nonlocal player_wins
        nonlocal computer_wins

        player_input = input(f"\n Hey {player_name}, Please guess and enter a number between 1 to 3\n")
        player = int(player_input)

        if player not in [1,2,3]:
            print(f"Oops, this is not a nvalid number {player_name}")
            return start_game()
        
        computer_choice = random.choice("123")
        computer = int(computer_choice)
        # main game logic
        def game_logic(player,computer):
            nonlocal player_wins
            nonlocal computer_wins
            nonlocal player_name
            if player == computer:
                player_wins += 1
                return f"{player_name} Wins! 🎉"
               
            else:
                computer_wins += 1
                return "Computer Wins! 🎉"
                
        game_result = game_logic(player,computer)
        game_count += 1
        print(f"\n{game_result}")
        print(f"Game Count : {game_count}")
        print(f"{player_name} Wins : {player_wins}")
        print(f"Computer Wins : {computer_wins}")

        def play_again():
            nonlocal player_name
            play_game = input(f"\n Hey {player_name}, Do you wanna play again ? \n Y for yes \n Q for quit\n")
            if play_game.lower() not in ['y','q']:
                return play_again()
            if play_game.lower() == 'y':
                return start_game(player_name)
            else:
                print(f"Thanks for playing")
                print(f"Bye Bye! {player_name}")

        play_again()

    return start_game

start_game = play_guess_my_number()
