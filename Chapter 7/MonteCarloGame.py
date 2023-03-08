import random

switch = False

def get_normal_door(host, player_door):
    door = 0
    while door == host or door == player_door:
        door = (door + 1)
    return door

def switch_door(shown_door, player_door):
    door = 0
    while door == shown_door or door == player_door:
        door = (door + 1)
    return door

def play_game(test_num):

    win_switch_count = 0
    win_stay_count = 0
    lose_switch_count = 0
    lose_stay_count = 0

    doors = [0, 1, 2]

    for number in range(0, test_num):

        prize_door = random.randint(0, 2)
        host = prize_door
        #print(f"This is the prize door: {host}")

        player_door = random.randint(0, 2)
        og_player_door = player_door
        #print(f"The player chose this door: {og_player_door}")

        shown_door = get_normal_door(host, og_player_door)
        #print(f"The shown door is: {shown_door}")

        if switch:
            player_door = switch_door(shown_door, og_player_door)


        if player_door == host and switch == False:
            win_stay_count += 1
            
        elif player_door == host and switch == True:
            win_switch_count += 1
            
        elif player_door != host and switch == False:
            lose_stay_count += 1

        elif player_door != host and switch == True:
            lose_switch_count += 1

    if switch:
        print(f"If the player switched every time...")
        print(f"The player had a {100*(win_switch_count/test_num):.2f}% chance of winning.")
        print(f"The player had a {100*(lose_switch_count/test_num):.2f}% chance of losing.")

    elif switch == False:
        print(f"If the player stayed every time...")
        print(f"The player had a {100*(win_stay_count/test_num):.2f}% chance of winning.")
        print(f"The player had a {100*(lose_stay_count/test_num):.2f}% chance of losing.")



if __name__ == '__main__':

    num_of_simulations = 1000000  #int(input("How many times would you like to run the simulation?\n:"))

    play_game(num_of_simulations)


