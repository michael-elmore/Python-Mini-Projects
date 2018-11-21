# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 17:25:47 2018

@author: Michael
"""

"""
This is a 2D snake game. Run the file to start it.
The output is in the console. This is my first attempt
at making any type of game.
"""
import random, time, sched

posx = random.randint(1,16)
posy = random.randint(1,16)
snake = [[posx, posy]]

print("Make the longest snake you can!")
score = 0
move = ""

def newgoal():
    goalx = random.randint(1,16)
    goaly = random.randint(1,16)
    return [[goalx,goaly]]

def checkloss(nhead, snake):
    if nhead in snake:
        return True
    elif nhead[0] not in range(1,17):
        return True
    elif nhead[1] not in range(1,17):
        return True
    else: 
        return False
    
def printdisplay(goal, snake):
    for i in range(16):
        gline = ""
        for j in range(16):
            if [j+1,i+1] in snake:
                gline = gline + "S "
            elif [j+1,i+1] in goal:
                gline = gline + "# "
            else:
                gline = gline + "- "
        if i == 1:
            print(gline, "\t SCORE:", score)
        else:
            print(gline)

gameover = False

goal = newgoal()
while goal[0] in snake:
    goal = newgoal()

while move != "stop" and gameover == False:
    
    printdisplay(goal, snake)
    move = input('Type "u", "d", "l" or "r": ')
    head = snake[len(snake)-1][:]
    
    if move == "u":
        nhead = [head[0],head[1]-1]
        gameover = checkloss(nhead, snake)
    elif move == "d":
        nhead = [head[0],head[1]+1]
        gameover = checkloss(nhead, snake)
    elif move == "l":
        nhead = [head[0]-1,head[1]]
        gameover = checkloss(nhead, snake)
    elif move == "r":
        nhead = [head[0]+1,head[1]]
        gameover = checkloss(nhead, snake)
    elif move == "stop":
        break
    else: 
        print("You must type u, d, l or r!")
    
    if nhead == goal[0]:
        snake.append(nhead)
        score += 1
        while goal[0] in snake:
            goal = newgoal()
    else:
        snake.append(nhead)
        snake.pop(0)
    
print("GAME OVER")
print("Your score is:", score)