def print_welcome_msg(player_name="Player",game_name="the game"):
    # Welcome message
    print("*"*32)
    print(f"{'*'.ljust(8)}{f'hello {player_name}'.upper().center(16)}{'*'.rjust(8)}")
    print(f"{'*'.ljust(8)}{'welcome'.upper().center(16)}{'*'.rjust(8)}")
    print(f"{'*'.ljust(8)}{'to'.upper().center(16)}{'*'.rjust(8)}")
    print(f"{'*'.ljust(4)}{game_name.upper().center(24)}{'*'.rjust(4)}")
    print("*"*32)