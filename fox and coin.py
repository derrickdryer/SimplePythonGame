#IMPORTS
import pgzrun

from random import randint

#Define variables
#create CONSTANT variables for the screen size
WIDTH = 4000
HEIGHT = 400

score = 90
level = 1
gameOver =False


#Actors
background = Actor("background")
background.pos = (100,100)
hedgehog = Actor("hedgehog")
hedgehog.pos = (200,200)
coin = Actor("coin")
coin.pos = (150,150)
fox = Actor("fox")
fox.pos=(-1200,120)
bonus = Actor("bonus")
bonus.pos = (-1300,130)
background2 = Actor("background2")
background2.pos = (100,100)
wolf = Actor("wolf")
wolf.pos = (-1200,120)

#DEFINE FUNCTONS
def draw():    
    screen.fill(" brown")

    if level == 1:
        background.draw()
    elif level == 2:
        background2.draw()

    hedgehog.draw()
    coin.draw()
    if level == 1:
        fox.draw()
    if level == 2:
        bonus.draw()
        wolf.draw()
    #Display the score on the screen.
    #The screen has a bunch of draw method, including.text()
    screen.draw.text("score: " +str(score), topleft=(10,10), color='black')
    
    if gameOver:
        if score < 400:
            screen.fill('blue')
            screen.draw.text("Final score:" + str(score)+"you lose", topleft=(10,10), fontsize = 60)
        else:
            screen.fill('pink')
            screen.draw.text("Final score:" + str(score)+"you win", topleft=(10,10), fontsize = 60)
        
def placeCoin():
     coin.x = randint(20, WIDTH-20)
     coin.y = randint(20, HEIGHT-20)
     
def placeFox():
     fox.x = randint(20, WIDTH-20)
     fox.y = randint(20, HEIGHT-20)
     

def placeWolf():
         wolf.x = randint(20, WIDTH-20)
         wolf.y = randint(20, HEIGHT-20)
     
def showFox():
    fox.pos = (120,120)
    
def showWolf():
    wolf.pos = (120,120)
    
def showBonus():
    bonus.pos = (130,130)

def timeUp():
   #This sets the gameOver global variable to be True.
    global gameOver
    gameOver = True 

#updates() is a built-in-functon (like draw())
#updates will be called automatically 60 times per second.
def update():
    global score, level
    
    if keyboard.left:
       hedgehog.x = hedgehog.x-2
       hedgehog.image = 'hedgehog2'
    if keyboard.down:
       hedgehog.y = hedgehog.y+2
    if keyboard.up:
        hedgehog.y = hedgehog.y-2
    if keyboard.right:
       hedgehog.x = hedgehog.x+2
       hedgehog.image = 'hedgehog'
    #coinCollected is a LOCAL boolean variable
    #All Actors have a built-in-function called .colliderect()
    #you pass in any other Actor and it returns True and False
    coinCollected = hedgehog.colliderect(coin)
    foxHit = hedgehog.colliderect(fox)
    bonusCollected = hedgehog.colliderect(bonus)
    wolfHit = hedgehog.colliderect(wolf)
    #Did the hedgehog get the coin?
    if coinCollected:
        if level == 1:
            score = score + 10
        elif level == 2:
            score = score + 20
        placeCoin()

    #Did the hedgehog get hit?
    if foxHit:
        score = score - 5
        placeFox()
    elif level == 2:
        if wolfHit:
            score = score -6
            placeWolf()
    #Did yopu get enough points to move to level 2?
    if level == 1 and score >= 100:
        level = 2
    
    #Did the hedgehog get the bonus
    if bonusCollected:
        score  = score + 50
        bonus.pos = (-1000,1000)

#MAIN PROGRAM (TOP-LEVEL CODE)
#Run the timeUp function 15 seconds after the game starts.
#clock is a built-in-function with a .schedule() method
clock.schedule(timeUp, 50)
clock.schedule(showFox, 10)
clock.schedule(showBonus,15)
clock.schedule(showWolf,10)
placeCoin()

pgzrun
