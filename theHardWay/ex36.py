""" A selection game. """
from sys import argv, exit
import random

def hut():
    print "Please select the next action:"
    print """
    \t1. go ahead
    \t2. knock the door
    \t3. get in
    """
    response = False

    while True:
        next = raw_input("> ")

        if next == "go ahead":
            dead("You'll lost in the forest.")
        elif next == "knock the door":
            print "There is someone in the hut and open the door."
            response = True
        elif next == "get in" and response:
            print "Talk to the master and get the map."
            print "Find a right way to get out of the forest."
            print "You win!"
            exit(0)
        else:
            print "Please select the reasonable action."

def questions(x=random.randint(1, 100), y=random.randint(1, 100)):
    """ Give the right answer with random input data."""
    print "Please answer: %d * %d = ?" % (x, y)
    answer = raw_input("> ")
    return answer == (x * y)

def sphinx_room():
    print "Now you are meeting Sphinx!"
    print "You have to answer 3 questions, if answers are all right, you win!"

    for i in range(3):
        result = questions()
        if not result:
            dead("You gave the wrong answer! Sphinx will kill you! ")

    print "You are right! You win!"
    return


def gold_room():
    print "This room is full of gold. How much do you take?"

    next = raw_input(">Please input a number: ")
    try:
        int(next)
        how_much = int(next)
    except ValueError:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        # Exit the interpreter by raising SystemExit(0)
        exit(0)
    else:
        dead("You greedy bastard!")


def medusa_room():
    print "You are now in front of a beauty."
    print "She is Medusa, whose hair if full of snakes!"
    print "She, it, whatever stares at you and you become a stone."
    print "Do you flee for your life or stay with her?"

    next = raw_input("> ")

    if next == "flee":
        print "You ran out of the room and returned to the hall."
        palace()
    else:
        dead("You became a statues.")

def palace():
    print "There are 3 doors in the palace hall, please select one!"

    while True:
        door = raw_input("> Please select left or middle or right door:")

        if door == "left":
            sphinx_room()
        elif door == "middle":
            gold_room()
        elif door == "right":
            medusa_room()
        else:
            print "Please select a door."


def dead(why):
    print why, "You lose!"
    exit(0)


def start():
    print "You are now in a forest. You are lost."
    print "Now, in your front, there are two different road ahead."
    print "Please pick one:"
    next = raw_input("> Please select left or right:")

    if next == 'left':
        print "You find a hut in the end of the road."
        hut()
    elif next == 'right':
        print "You see a beautiful palace ahead!"
        palace()
    else:
        dead("You are lost in the forest until you are starve and thirsty!")

start()
