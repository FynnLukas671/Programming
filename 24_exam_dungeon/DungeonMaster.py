from Player import Player
from Monster import Monster
from Room import Room
from random import randint

def __main__():
    nr_of_rooms = 2
    run_game(nr_of_rooms)

def initialize_player(player):
    return Player(player, randint(40, 80))

def initialize_rooms(rooms):
    room_list = []

    for key,value in rooms.items():
        room_monster = Monster(value["monster"])
        room_description = Room(rooms[key]["desc"], room_monster)

        room_list.append(room_description)

    return room_list

def print_results(player):
    print("The game is over!")
    print(str(player))
    print("Thank you for playing Dungeon Master!")
    print("Good Bye!")

def run_game(nr_of_rooms):
    rooms_config = {}
    print("Welcome to the Dungeon")
    player = initialize_player(str(input("What is the name of your player? ")))
    for i in range(nr_of_rooms):
        rooms_config.update({i: {"desc": str(input("What is the description of your room? ")), "monster": str(input("What is the name of the monster? "))}})
    room_objects = initialize_rooms(rooms_config)
    for i in range(nr_of_rooms):
        room_objects[i].interact(player)
    if player.health == 0:
        print("Sorry - you died!")
        print_results(player)

__main__()