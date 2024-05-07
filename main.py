import argparse
from gmn_game import start_game
from rps_game import play_rps
from welcome import print_welcome_msg
# create a argument parser
parser = argparse.ArgumentParser(description="Helps in using player name in the game")

parser.add_argument("-n","--name",help="Stores player name",dest="player_name",required=True)
# parsing arguments from command line
args = parser.parse_args()

print(f"Hello {args.player_name}, Welcome to Amazing Games World")

def start_game_menu(player_name):

    while True:
        game_num = int(input("\n Which game do you want to play ? please enter\n1. for Rock Paper Scissors\n2. for Guess my Number\n3. for exit the game\n"))
        if game_num not in [1,2,3]:
            print("Invalid Number")
            return start_console(player_name)
        if game_num == 1:
            # print welcome message
            print_welcome_msg(player_name,"rock, paper, scissors")
            # start Rock Paper Scissors
            play_rps(player_name)
            continue
        elif game_num == 2:
            # print welcome message
            print_welcome_msg(player_name,"Guess my number")
            # start Guess My Number
            start_game(player_name)
            continue
        else:
            print("Sad to see you go 😢")
            print("Bye Bye")
            break



if __name__ == "__main__":
    start_game_menu(args.player_name)
