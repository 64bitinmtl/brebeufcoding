#####################################################
#   PLEASE NOTE!!!
#   THIS GAME IS STILL INCOMPLETE
#   THERE IS NO WAY OF WINING (THERE ISN'T THE CODE TO CATCH JACK OF MOLAY), YET..
#   FEEL FREE TO ADD TO MY CODE
#   JUST ADD A COMMENT NEXT TO THE CODE YOU ADDED
#   THANKS!
#   LAURENCE -- December 24, 2016
#####################################################

"""
                        THE ROI MAUDIT GAME

Version Python 2.7.12
Created by Laurence Liang in the December of 2016

***

GAMEPLAY:

You, KING PHILLIP 4 THE BEAUTIFUL, are the KING of FRANCE in 1314.

KING PHILLIP 4 THE BEAUTIFUL is very disturbed, because the prisonner, JACK OF
MOLAY, escaped from prison earlier today, the day of his execution.

Your advisor, GUY OF NOGARETT, advises you to hunt down JACK OF MOLAY, before
he reaches the shores of ENGLAND where he will surely receive political asylum.

You can do 4 things at every turn:
    1. Assault the person in front of you
    2. Dispatch imperial soldiers in your region
    3. Ask the person if he knows where JACK OF MOLAY is
    4. Give up

The game ends either if you have captured JACK OF MOLAY or if he arrives safely in ENGLAND.

GOOD LUCK!
"""


#IMPORT MODULES
#Random module for unpredicatability
import random
#Time module for keeping track of time
import time

#DECLARE VARIABLES

class userClass:        #Class encorporating numeric variables
#Health points
    healthPoints=100.0  #User's health points
    enemyHealth=100.0   #Ennemy's health points
#Probability of attacking the king
    attackProbability=0.0
#Damage done
    damageDone=0.0          #Ennemy's attack
    attackDamage=0.0        #User's attack

#Is Jack in England
    jackSafe=0.0
    

#Combat mode
    combatMode=False        #If user is engaged in a fight
jackFound=False      #If Jack is found

#Character list
charList=["Pierre", "Luc", "Mario", "Harambe", "Burt", "Deez Nutz",
          "Philippe", "Louis", "Charles", "Guillaume", "Blanche",
          "Marie", "Marguerite", "Jeanne", "Gautier", "Sylvie", "PewDiePie",
          "Jack of Molay", "Cyprien", "Gary", "Shan Gao", "Laurence THE PCS PERSON",
          "Andrei Lupu", "Phil Radu the Student", "Arian", "Stephen LU!", "Andrew Yao"]

#To break decisionFork loop:
breakLoop=False
#The user's name
name=""
strangerName=""         #The stranger's name
changeName=False        #Wether the stranger changes

#CREATE FUNCTIONS
#Display rules
def displayRules():
    print "Just press ENTER"
    raw_input()
    print "You, KING PHILLIP 4 THE BEAUTIFUL, are the KING of FRANCE in 1314."
    raw_input()
    print """KING PHILLIP 4 THE BEAUTIFUL is very disturbed, because the prisonner, JACK OF
MOLAY, escaped from prison earlier today, the day of his execution."""
    raw_input()
    print """Your advisor, GUY OF NOGARETT, advises you to hunt down JACK OF MOLAY, before
he reaches the shores of ENGLAND where he will surely receive political asylum."""
    raw_input()
    print"""You can do 4 things at every turn (enter the word in CAPITALS):
    1. ASSAULT - Assault the person in front of you
    2. MOVE    - Go to a different place
    3. ASK     - Ask the person if he knows where JACK OF MOLAY is
    4. GIVE UP - Give up"""
    raw_input()
    print "The game ends either if you have captured JACK OF MOLAY or if he is in ENGLAND."
    raw_input()
    print "GOOD LUCK!"
    print
    print "THE GAME BEGINS NOW..."


#Format input
def formatInput(userInput):
    userInput.lower()   #Lowercase letters for simplicity
    return userInput;
    
#Decision fork
def decisionFork(decision):
    initVar()                       #Initializes damage and attack probability
    if decision == "assault":
        if userClass.attackProbability>0.6:
            print strangerName, "attacked you!"
            userClass.combatMode=True
            userClass.healthPoints=userClass.healthPoints-userClass.damageDone  #Recalculates user's health points
        changeName=False
        return changeName
        userClass.enemyHealth=userClass.enemyHealth-userClass.attackDamage      #Ennemy health damage
        if userClass.enemyHealth<0:     #If enemy has finally died
            print strangerName, "is dead."
            combatMode=False
            changeName=True
            return userClass.healthPoints, changeName, userClass.enemyHealth, combatMode
        
    if strangerName=="Jack of Molay":
        print "You've found Jack of Molay!!!"
        
    elif decision == "search":
        print "They couldn't find jack"
        changeName=True
        return changeName
    
    elif decision == "ask":
        changeName=True
        return changeName
        print strangerName, "says that Jack isn't here"
        
    elif decision == "give up":
        userClass.healthPoints=0
        
    else:
        print "You did not enter a valid command."
        print "Please try again."
    
#Initialize variables:
def initVar():
    #Damage done
    userClass.damageDone=random.uniform(0,30)
    userClass.attackDamage=random.uniform(0,50)
    #Probability of attacking the king:
    userClass.attackProbability=random.random()
    #Is Nogaret in England?
    userClass.jackSafe=userClass.jackSafe+random.uniform(0,0.05)
    #Stranger name
    if changeName==True:
        strangerName=random.choice(charList)
        return strangerName
    return userClass.damageDone, userClass.attackProbability

#Displays current user situation
def displayCurrent():
    print "Health:", userClass.healthPoints , "%"
    print "Ennemy:", userClass.enemyHealth, "%"
    print

#Display game over
def gameOver():
    print "GAME OVER."
    print

    
#GAMEPLAY
print " \t \t \t THE ROI MAUDIT GAME"
print
print

#Display rules
displayRules()    #Display rules
print "What's your name?"
name=raw_input("My name is: ")

#While loop
while userClass.healthPoints > 0 and (userClass.jackSafe < 1.0 or jackFound==True) :
    userInput=raw_input(name + ": ")
    #Decision fork
    decisionFork(userInput)
    #Calls function
    #Displays current health
    displayCurrent()


    
#Display game over
gameOver()
