import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

def rock_paper_scissors():


    game_count = 0
    player_wins = 0
    computer_wins = 0
    tie_count = 0

    def play_rps_game(player_name='Player'):

        nonlocal game_count
        
        # Collect Player Input  
        player_choice = input(
            f"Hi {player_name} please enter... \n 1 for ROCK \n 2 for PAPER \n 3 for SCISSORS\n\n")

        # Make Sure input is 1,2 or 3
        if player_choice not in ["1","2","3"]:
            print(f"{player_name}, Wrong Option Selected 👎")
            return play_rps_game(player_name) # recurssive call
            
        # casting Player input in integer
        player = int(player_choice)
        # generate a random computer number for computer
        computer_choice = random.choice("123")
        # cast computer_choice to integer
        computer = int(computer_choice)

        print(f"You Chose {str(RPS(player)).replace('RPS.', '')}.")
        print(f"Computer Chose {str(RPS(computer)).replace('RPS.', '')}.\n")

        def game_logic():
            nonlocal player_wins
            nonlocal computer_wins
            nonlocal tie_count
            nonlocal player_name
            # game logic
            if player == 1 and computer == 3:
                player_wins += 1
                return f"{player_name} Wins! 🎉🎉🎉"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"{player_name} Wins! 🎉🎉🎉"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"{player_name} Wins! 🎉🎉🎉"
            elif player == computer:
                tie_count += 1
                return "It's a tie. 😃"
            else:
                computer_wins += 1
                return "💻 Computer wins!"

        game_result = game_logic()
        print(game_result)
        game_count += 1
        print(f"\nGame count = {game_count}")
        print(f"{player_name} Wins : {player_wins}")
        print(f"Computer Wins : {computer_wins}")
        print(f"Tie count : {tie_count}")

        # ask player if they want to play again or quit
        while True:
            play_again = str(input(f"\n\n Hey {player_name}, Do you want to play again ? Enter...\n Y to play again\n Q to quit the game\n"))
            if play_again.lower() not in ['y','q']:
                continue
            else:
                break

        if play_again.lower() == 'y':
            play_rps_game(player_name) 
        else:
            print("\n Thanks for playing... .🙏")
            print(f"Bye Bye! {player_name} 👋👋👋")
            return

    return play_rps_game
        
    
play_rps = rock_paper_scissors()


    
    
