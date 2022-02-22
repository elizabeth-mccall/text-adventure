sub = ["she", "he", "they"]
obj = ["her", "him", "them"]
pos = ["her", "his", "their"]
ind_pos = ["hers", "his", "theirs"]

is_are = ["is", "is", "are"]
was_were = ["was", "was", "were"]

def get_pronoun():
    global start_pronoun
    start_pronoun = input("What pronouns do you use? (Enter the number): \n1. she/her/hers \n2. he/him/his \n3. they/them/theirs \n4. other (enter your own)\n>>>")
    if start_pronoun in ["1", "2", "3", "4"]:
        global player_pronoun
        player_pronoun = (int(start_pronoun) - 1)
        if player_pronoun in [0, 1, 2]:
            print("Your pronouns are", sub[player_pronoun] + ",", obj[player_pronoun] +",", ind_pos[player_pronoun] + ".")
        elif player_pronoun == 3: 
            print("Enter your 3rd person personal pronouns below in LOWERCASE:\n")
            new_sub = input("Subject pronoun (i.e., she/he/they). Example: <They> went to the store.\n>>>")
            sub.append(new_sub)
            new_obj = input("Object pronoun (i.e. her/him/them). Example: They saw <him>.\n>>>")
            obj.append(new_obj)
            new_pos = input("Possessive pronoun (i.e. her/his/their). Example: That is <her> bag.\n>>>")
            pos.append(new_pos)
            new_ind_pos = input("Independent possessive pronoun (i.e. hers/his/theirs). Example: That bag is <hers>.\n>>>")
            ind_pos.append(new_ind_pos)
            def get_plurality():
                pronoun_plurality = int(input("Are your pronouns grammatically singular (e.g., he/she <is>) or plural (e.g., they/xey <are>)? (Enter the number) \n1. singular\n2. plural\n>>>"))
                if pronoun_plurality == 1:
                    is_are.append("is")
                    was_were.append("was")
                elif pronoun_plurality == 2:
                    is_are.append("are")
                    was_were.append("were")
                else:
                    print("Invalid entry.")
                    get_plurality()
            get_plurality()
            print("Your pronouns are", sub[player_pronoun] + ",", obj[player_pronoun] +",", ind_pos[player_pronoun] + ".")
    else:
        print("Enter a number from 1-4.\n")
        get_pronoun()

while True:
    player_name = input("What is your name?\n>>>")
    get_pronoun()
    print("This is", player_name + ".", (sub[player_pronoun]).capitalize(), is_are[player_pronoun], "very cool. I've known", obj[player_pronoun], "since", pos[player_pronoun], "childhood.")

