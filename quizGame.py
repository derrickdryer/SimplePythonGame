WIDTH = 1311
HEIGHT = 825

mainBox = Rect(0,0, 820,240)
timerBox = Rect(0,0, 240,240)
answerBox1 = Rect(0,0, 495, 165)
answerBox2 = Rect(0,0, 495, 165)
answerBox3 = Rect(0,0, 495, 165)
answerBox4 = Rect(0,0, 495, 165)
score = (0,0, 60,60)

science = Actor('science')
science.pos = (200,280)
math = Actor('math')
math.pos = (1100,555)

#Move the boxes
mainBox.move_ip(50,40)
timerBox.move_ip(990,40)
answerBox1.move_ip(50,358)
answerBox2.move_ip(735,358)
answerBox3.move_ip(50,538)
answerBox4.move_ip(735,538)

#Create a list of answer boxes
answerBoxes = [answerBox1, answerBox2, answerBox3, answerBox4]

score = 0
timeLeft = 20

menu = True
gameOver = False

#Questions are stored in  list.
#Each list contain the questions, 4 answer, and a number for the right answer.
q1 = ["which of these is a noble gas?",
      'Carbon dioxide', 'Nitrogen', 'Oxygen', 'Argon', 4]
q2 = ['What organ in the body is responsible for pumping blood in your body?',
      'Heart', 'Lungs', 'Kidney', 'Liver', 1]
q3 = ['What is the procees by which plants convert light energy into food known as ?',
      'Metabolism', 'Evaporation', 'Catabolism', 'Photosynthesis', 4]
q4 = ['Which planet is the closest to the sun?',
      'Saturn', 'Neptune', 'Mercury', 'Venus', 3]
q5 = ['What scientific name is table salt known as ?',
      'Water', 'Sodium chloride', 'Magnesium carbonate', 'Calcium hydroxide', 2]
q6 = ['A bird travel 72 miles in 6 hours trying at a constant speed. At this rate, how many miles did it travel for 5 hours?',
      '12', '30', '60', '14.4', 3]
q7 = ['what line given by its equationbelow contain the point(1,-1)and(3,5)?',
      '-2y -6x = 0', '2y = 6x -8', 'y = 3x -4', 'y = -3x +4', 2]
q8 = ['The number of 3-digit number divisible by 6 is..?',
      '149', '166', '150', '151', 3]
q9 = ['Which of the following number gives 240 when added to its own square ?',
      '15', '16', '18', '20', 1]
q10 = ['The sum of two positive integer is 13. The difference between these numbers is 7. what is their product?',
      '12','22','30','40', 3]

#Create a list of questions.
questions = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]

question = questions.pop(0)

def draw():
    screen.fill('dim gray')
    screen.blit('background', (0,0))

    if menu == True:
        #Draw those pictures
        science.draw()
        math.draw()
        
    else:

        #Draw the main and timer rectangles
        screen.draw.filled_rect(mainBox, 'sky blue')
        screen.draw.filled_rect(timerBox, 'sky blue')
        
        #Draw all the answer boxes in the list.
        for box in answerBoxes:
            screen.draw.filled_rect(box, 'orange')
        
        #Draw all the text.
        screen.draw.textbox(str(timeLeft), timerBox, color='black')
        screen.draw.textbox(question[0], mainBox, color='black')
        
        index = 1
        for box in answerBoxes:
            screen.draw.textbox(question[index], box, color='black')
            index = index + 1
            
        
        #Display the score on the screen.
        #The screen has a bunch of draw method, including.text()
        screen.draw.text("score: " +str(score), fontsize=60, bottomright=(760, 760), color='black')
    
def gameOver():
    global question, timeLeft, gameOver
    #Build a string to show the final score.
    message = "Game over. you got " + str(score) + " point" 
    #The question is no the message and the answers
    #are blank.
    question  = [message, '-', '-','-', '-', 5]
    timeLeft = 0
    gameOver = True
    
#This functon runs when the player gets an correct answer.
def correctAnswer():
    global question, score, timeLeft,menu
    
    score += 10    
    #If there are more questions, getthe next one.
    if len(questions) > 0:
        question = questions.pop(0)
        timeLeft = 20
    else:
        #No more questions left.
        print("End of question")
        gameOver()
        #menu=True

def on_mouse_down(pos):
    global menu, questions, question
    if menu == True:
        if math.collidepoint(pos):
            questions = [q6, q7, q8, q9, q10]
            question = questions.pop(0)
        elif science.collidepoint(pos):
            questions = [q1, q2, q3, q4, q5]
            question = questions.pop(0)
        menu = False
    else:
        #This variable holds a number that represents the
        #position of the answer box in the list.
        index = 1
        #Go through each answerBox looking for a mouse colllision.
        for box in answerBoxes:
            if box.collidepoint(pos):
                print("Clicked on answer" + str(index))
                if index == question[5]:
                    print("You got it correct")
                    correctAnswer()
                    
            index += 1
            
def on_key_down():
    global gameOver,menu
    if gameOver == True:
        gameOver = False
        menu = True

def updatesTimeLeft():
    global timeLeft
    
    if timeLeft > 0:
        timeLeft = timeLeft - 1
    else:
        gameOver()
        
clock.schedule_interval(updatesTimeLeft, 1.0)

#Extensions - 4 pts Each
#1. END THE GAME
#2. Skip question/Hints
#3. Additional.key controls
#4. Point system.
#5. Awesomeness
