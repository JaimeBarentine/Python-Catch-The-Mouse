

d = {'holdingCheese' : 0, 'lightsOn' : 1, 'cheeseOnTable' : 0, 'mouseOut' : 0, 'youWin' : 0, 'turns' : 0, 'currentRoom' : 'middle'}

def startAdv():
    
    
    if d['currentRoom'] == "middle":
        if d['lightsOn'] == 1:
            print("There's a 'mouse hole' in the wall, and a 'light switch' above it. Only exits are 'left' and 'right'.")
        else:
            print("It's dark in here! There's a 'light switch' on the wall. Only exits are 'left' and 'right'.")

    elif d['currentRoom'] == "right":
        print("A 'cheese dispenser' sits against the wall. Only door is 'left'.")
        d['mouseOut'] = 0
    elif d['currentRoom'] == "left":
        d['mouseOut'] = 0
        if d['cheeseOnTable'] == 1:
            print("Cheese sits on a 'table' in the corner of the room. Only door is 'right'.")
            
        else:
            print("A 'table' sits in the corner of the room. Only door is 'right'")
    
        
    
    chooseText = input("What will you interact with?")
    
    if chooseText == "left" and d['currentRoom'] != "left":
        if d['currentRoom']  == "middle":
            print("You go through the left door into the left room.")
            leftDoor()
        elif d['currentRoom'] == "right":
            print("You go through the left door into the middle room.")
            middleDoor()
    elif chooseText == "right" and d['currentRoom'] != "right":
        if d['currentRoom'] == "left":
            print("You go through the right door into the middle room.")
            middleDoor()
        elif d['currentRoom'] == "middle":
            print("You go through the right door into the right room.")
            rightDoor()
    elif chooseText == "cheese dispenser":
        if d['currentRoom'] == "right" and d['holdingCheese'] == 0:
            d['holdingCheese'] = 1
            print("You got some cheese from the cheese dispenser.")
        elif d['currentRoom'] == "right" and d['holdingCheese'] == 1:
            print("You already have cheese.")
    elif chooseText == "table":
        if d['cheeseOnTable'] == 1 and d['holdingCheese'] == 1:
            print("You're already holding cheese!")
        elif d['cheeseOnTable'] == 1 and d['holdingCheese'] == 0:
            print("You grabbed the cheese off of the table.")
            d['holdingCheese'] = 1
        elif d['cheeseOnTable'] == 0 and d['holdingCheese'] == 1:
            print("You set the cheese on the table.")
            d['holdingCheese'] = 0
            d['cheeseOnTable'] = 1
        else:
            print("You slap your hand on the table... nothing happens.")
            
    elif chooseText == "light switch":
        if d['lightsOn'] == 1:
            if d['cheeseOnTable'] == 1:
                print("You turn off the lights, after a moment you hear squeaks coming from the 'left' room.")
                d['cheeseOnTable'] = 0
                d['mouseOut'] = 1
            else:
                print("You turn the light switch off.")
            d['lightsOn'] = 0
        elif d['lightsOn'] == 0:
            if d['mouseOut'] == 1:
                print("You switch the lights on, as you do the mouse comes walking back in with the cheese in his mouth. You quickly grab him as he's stunned with shock, you've caught the mouse. You win!")
                d['youWin'] = 1
            else:
                print("You turn the light switch back on again.")
                d['lightsOn'] = 1
    elif chooseText == "mouse hole" and d['lightsOn'] == 1:
        if d['holdingCheese'] == 1:
            print("You put the cheese by the mouse hole, the mouse grabs it and hides in its hole again too quickly for you to grab him.")
            d['holdingCheese'] = 0
        else:
            print("You can hear squeaks coming from the other side of the wall. You don't know why, but you really want to catch that mouse!")
    else:
        print("Command not recognized, type something within the room (words that have 'these' around them) that you want to interact with.")
            



def leftDoor():
    d['currentRoom'] = "left"
    ##print("I'm in the left room.")

def middleDoor():
    d['currentRoom'] = "middle"
    ##print("I'm in the middle room.")

def rightDoor():
    d['currentRoom'] = "right"
    ##print("I'm in the right room.")



while d['youWin'] == 0:
    startAdv()
    d['turns'] += 1


endText = input("You beat it in " + str(d['turns']) + " moves! Type anything to end the script.")
extraEndText = input("Except " + endText + ", that's wrong. Don't type that... unless you want to.")
