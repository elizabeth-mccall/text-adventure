from vocab import *
from items import *
from playerchar import * 

###############
### PARSING ###
###############

item_dict = {
    "key": key,
    "rug": rug,
    "sword": sword,
    "branch": branch,
    "basket": basket,
    "jar": jar,
    "bottle": bottle,
    "bread": bread}

#ALL
all_words = [verb_go, directions, directions_short, verb_inventory, verb_look, verb_examine, word_self, cmd_quit, cmd_help, verb_take, verb_drop, verb_eat, verb_break, verb_move, verb_unlock, word_door, prep_from, prep_of, prep_with, articles, item_dict, word_all]

#Checks whether all words are in vocabulary
def check(command):
    if len(command) == 0:
        print("I beg your pardon?")
        return False
    else:
        for command_word in command:
            checker = False
            for word_list in all_words:
                if command_word in word_list:
                    # for debugging: print("I understand", command_word)
                    checker = True
                else:
                    pass
            if checker == False:
                print(f'''I don't know the word "{command_word}".''')
                return False
        if checker == True:
            return True

def parse(command):
    #REMOVE ARTICLES
    command = [word for word in command if word not in articles]
    #print(command) #for debugging
    if command == []:
        print("I'm sorry, I don't understand.")
    #MOVEMENT
    elif any(word in directions for word in command) or any(word in directions_short for word in command) or any(word in verb_go for word in command):
        if command[0] in directions:
            if len(command) == 1:
                player.move_direction(command[0])
            else:
                print(f"I understand you as far as wanting to move {command[0]}.")
        elif command[0] in directions_short:
            command_direction = None
            for direction in directions:
                if command[0] == direction[0]:
                    command_direction = direction
                else:
                    pass
            player.move_direction(command_direction)
        elif command[0] in verb_go:
            if len(command) == 1:
                print(f"Where do you want to {command[0]}?")
            elif len(command) == 2:
                if command[1] in directions or command[1] in directions_short:
                    player.move_direction(command[1])
                else:
                    print(f'"{command[1].capitalize()}" is not a direction.')
            else:
                print(f"I don't understand where you want to {command[0]}.")
        else:
            def is_movement(word):
                return word in directions or word in directions_short or word in verb_go
            desired_direction = [word for index, word in enumerate(command) if is_movement(word)]
            print(f'''I don't understand how you used the word "{desired_direction[0]}".''')
    #INVENTORY
    elif command[0] in verb_inventory:
        if len(command) == 1: 
            player.inventory()
        else:
            print("I understood you as far as wanting to take inventory.")
    #LOOK
    elif command[0] in verb_look:
        if len(command) == 1:
            print(get_room(player.x, player.y))
            get_room(player.x, player.y).describe()
        else:
            print("I understood you as far as wanting to look.")
    #EXAMINE
    elif command[0] in verb_examine:
        if len(command) == 1:
            print("What do you want to", str(command[0]) + "?")
        else: 
            try:
                if command[1] in word_all:
                    print("It's not clear what you're referring to.")
                elif command[1] in word_self:
                    player.describe()
                elif item_dict[command[1]] in get_room(player.x, player.y).contents or item_dict[command[1]] in player.contents:
                    item_dict[command[1]].describe()
                elif hasattr(get_room(player.x, player.y), "furniture"):
                    if item_dict[command[1]] in get_room(player.x, player.y).furniture: 
                        item_dict[command[1]].describe()
                    else:
                        print(f"You can't see a {command[1]} here.")
                else:
                    print(f"You can't see a {command[1]} here!")
            except KeyError:
                print("I understood you as far as wanting to examine something.")
    #TAKE
    elif command[0] in verb_take:
        def take_out_of(item, container):
            try:
                item_dict[container].take_out(item_dict[item], player.contents)
                print("You take the {} from the {}.".format(item, container))
            except ValueError:
                print("There is no {} in the {}.".format(item, container))
            except AttributeError:
                print("The {} is not a container.".format(container))
            except KeyError:
                print("I understood you as far as wanting to take something.")
        def take(item):
            try:
                get_room(player.x, player.y).take(item_dict[item], player.contents)
                print("Taken.")
            except AttributeError:
                print("That's much too heavy to carry.")
            except ValueError:
                print(f"You don't see a {item} in here.")
            except KeyError:
                print("I understood you as far as wanting to take something.")
        def take_all():
            try:
                for item in get_room(player.x, player.y).take_all(player.contents):
                    print("Taken: {}".format(item))
            except ValueError:
                print("There's nothing here to take.")
            except KeyError:
                print("I understood you as far as wanting to take something.")
        if len(command) == 1:
            print("What do you want to {}?".format(str(command[0])))
        elif len(command) == 2:
            if command[1] in word_all:
                take_all()
            else:
                take(command[1])
        elif len(command) == 3:
            take_out_of(command[1], command[2])
        elif len(command) == 4:
            if command[2] in prep_from:
              take_out_of(command[1], command[3])
            else:
                pass
        elif len(command) == 5:
            if command[2] in prep_from and command[3] in prep_of:
                take_out_of(command[1], command[4])
            else:
                pass
        else:
            print("I understood as far as you wanting to take something.")
    #DROP
    elif command[0] in verb_drop:
        def drop(item):
            try:
                player.drop(item_dict[item], get_room(player.x, player.y).contents)
                print("Dropped.")
            except ValueError:
                print("You don't have that.")
        def drop_all():
            try:
                for item in player.drop_all(get_room(player.x, player.y).contents):
                    print("Dropped: {}".format(item))
            except ValueError:
                print("You aren't carrying anything.")
        if len(command) == 1:
            print("What do you want to", str(command[0] + "?"))
        elif len(command) == 2:
            if command[1] in word_all:
                drop_all()
            else:
                drop(command[1])
        else:
            print("I understood as far as you wanting to drop something.")
    #EAT
    elif command[0] in verb_eat:
        def eat(item):
            try:
                player.eat(item_dict[item])
                print("You eat the {}. Yum!".format(item_dict[item]))
            except AttributeError:
                print("You can't eat that!!")
            except ValueError:
                print("You don't have that.")
            except KeyError:
                print("I don't understand what you want to eat.")
        if len(command) == 1:
            print("What do you want to eat?)")
        elif len(command) == 2:
            eat(command[1])
    #BREAK
    elif command[0] in verb_break:
        def breakit(item):
            try: 
                item_dict[item].breakit(get_room(player.x, player.y).contents)
                print(f"You smash the {item} as hard as you can, and it breaks!")
            except AttributeError:
                print("You hit it as hard as you can, but it doesn't break.")
        if len(command) == 1:
            print(f"What do you want to {command[0]}?")
        elif len(command) == 2:
            breakit(command[1])
        else:
            print(f"I understood you as far as wanting to {command[0]} something.")
    #MOVE-ITEM
    elif command[0] in verb_move:
        if len(command) == 1:
            print(f"What do you want to {command[0]}?")
        elif len(command) == 2:
            get_room(player.x, player.y).push(item_dict[command[1]])
        else:
            print(f"I understood you as far as wanting to {command[0]} something.")
    #UNLOCK
    elif command[0] in verb_unlock:
        def unlock():
            try:
                if key in player.contents:
                    get_room(player.x, player.y).unlock_adjacents()
                else:
                    print("You don't have the key for that door.")
            except:
                print("You don't see a lock nearby.")
        if len(command) == 1:
            unlock()
        elif len(command) == 2:
            if command[1] in word_door:
                unlock()
        elif len(command) == 4:
            if command[1] in word_door and command[2] in prep_with:
                if command[3] == "key":
                    unlock()
                else:
                    print(f"You can't unlock a door with a {command[3]}.")
            else:
                print("I don't understand what you want to unlock.")
        else:
            print("I understood you as far as wanting to unlock something.")
    #HELP
    elif command[0] in cmd_help:
        if len(command) == 1:
            print('''
Commands:
    'north'/'n' = go north
    'south'/'s' = go south
    'east'/'e' = go east
    'west'/'w' = go west
    'look'/'l' = look around the room
    'inventory'/'i' = check your inventory
    'examine'/'x' = examine (something)
    'help'/'h' = open help menu
    'quit'/'q' = quit the game
    + and more (but you'll have to figure those out yourself!)''')
        else:
            print("Type 'help' if you need help.")
    #QUIT
    elif command[0] in cmd_quit:
        if len(command) == 1:
            quit_y_n = input("Are you sure you want to quit? Y/N \n \n>")
            if quit_y_n == "y":
                print("Quitting game.")
                raise SystemExit
            else:
                print("Okay, then.")
        else:
            print("Type 'quit' if you want to quit.")
    else:
        print("Sorry, but you stumped me with that one.")



