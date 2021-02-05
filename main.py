from room import Room
from item import Item
from character import Enemy, Friend
from rpginfo import RPGinfo

backpack = []

spooky_castle = RPGinfo("Spooky Castle")
spooky_castle.welcome()
RPGinfo.info()

kitchen = Room("Kitchen")
dining_hall = Room("dining hall")
ballroom = Room("ballroom")

print("There are", Room.number_of_rooms, "Rooms to explore!")

kitchen.set_description("A dank and dirty room buzzing with flies")
kitchen.link_room(dining_hall, "south")

dining_hall.set_description("A large room with ornate golden decorations on each wall")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")

ballroom.set_description("A vast room with shiny wooden floor; huge candlesticks guard the entrance")
ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "A smelly zombie!")
dave.set_conversation("Hi, I am Dave. I like to move it move it!")
dave.weakness = 'cheese'
dave.set_sleep_spell('Kacamora')

juan = Enemy("Juan", "A clever skeleton!")
juan.set_conversation("Hello, there! Would you like to sit and read with me?")
juan.weakness = "book"
juan.set_sleep_spell('chuwawa')

print("There are", Enemy.enemies_count, "enemies that you have to defeat!")

catrina = Friend('catrina', "A friendly pumpkin alien")
catrina.set_conversation("Why hello there!")
kitchen.set_character(catrina)

dining_hall.set_character(dave)
ballroom.set_character(juan)

cheese = Item("cheese")
cheese.set_description("Smelly Cheese to ward off Zombies!")
cheese.set_skill_level(1)
kitchen.set_item(cheese)

book = Item("book")
book.set_description("Romantic store to bore clever Skeletons!")
book.set_skill_level(1)
dining_hall.set_item(book)

current_room = kitchen
continueGame = True

while continueGame:
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    else:
        print('No one here!')
    command = input(">>>")
    if command in ['north', 'east', 'south', 'west']:
        current_room = current_room.move(command)
    elif command == 'talk':
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print('No one here!')
    elif command == 'fight':
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print('Pick an item to fight with:')
            item = input('>>>')
            if item in backpack:
                continueGame = inhabitant.fight(item)
            else:
                print("You do not have this item")
        elif inhabitant is not None and isinstance(inhabitant, Friend):
            print(inhabitant.name, "Is Friendly, more love less fight!")
        else:
            print('No one to fight with here!')
    elif command == "send to sleep":
        if inhabitant is not None:
            print('Cast a spell:')
            spell = input('>>>')
            continueGame = inhabitant.send_to_sleep(spell)
        else:
            print('No one here!')
    elif command == 'hug':
        if inhabitant is not None:
            if isinstance(inhabitant, Friend):
                inhabitant.hug()
            else:
                print("I wouldn't do that if I were you!")
        else:
            print("No one to hug here!")
    elif command == 'take':
        if current_room.item is not None:
            backpack.append(current_room.get_item().get_name())
            print(backpack)
            current_room.set_item(None)
        else:
            print("Nothing here!")

    if Enemy.enemies_count == 0:
        print("You are the winner of", spooky_castle.game_name, "\n Well done!")
        continueGame = False

RPGinfo.author = "Israel Goitom"
RPGinfo.credits()
