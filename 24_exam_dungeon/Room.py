from code import interact

from Player import Player
from Monster import Monster

class Room():

    def __init__(self, description, monster):
        self.description = description
        self.monster = monster

    def __str__(self):
        return str(self.description)

    def fight_round(self, player):
        print(str(monster))
        print(str(player))
        print(f"The monster hits you with {self.monster.strength} strength.")
        player.take_damage(self.monster.strength)
        print(str(player))
        print(f"You hit the monster with {player.strength} strength.")
        self.monster.take_damage(player.strength)
        print(str(monster))
        if self.monster.health == 0:
            print("The monster is dead")
            player.regain_health(self.monster.lost_health/2)
            print(f"Player {player.name}, you regained health: {player.health}")
        elif player.health == 0:
            print("You lost the fight")

    def interact(self, player):
        print(f"Welcome to the {self.description}")
        print(f"The monster {self.monster.name} appears!")
        if player.health != 0 and self.monster.health != 0:
            player_action = str(input("Would you like to run (r) or fight (f)? "))
            if player_action == "r":
                print("You chose RUN!")
                player.take_damage(10)
                print("You sprint out of the room and take 10 damage!")
            elif player_action == "f":
                print("You chose FIGHT!")
                self.fight_round(player)
                self.interact(player)

player = Player("Hans")
monster = Monster("Goblin")

room = Room("Hall", monster)
room.fight_round(player)
