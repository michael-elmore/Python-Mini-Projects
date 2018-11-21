# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 18:09:39 2018

@author: Michael
"""

"""
This simulates playing the EuroMillions lottery!
You can use it to see just how pointless playing the lottery
is. use the function "playlotto(n)", where "n" is the number
of lucky dip tickets you wish to buy, to get output: 
The actual draw, any close-matching draws and a table of 
close-matching draws.
"""

def gendraw():
    # This generates a EuroMillions number set. It can be
    # used to generate draws or to generate "lucky dips".
    import random
    result1 = []
    result2 = []
    while len(result1) < 5:
        ball = random.randint(1,50)
        if ball not in result1:
            result1.append(ball)
    while len(result2) < 2:
        ball = random.randint(1,12)
        if ball not in result2:
            result2.append(ball)
    result1.sort()
    result2.sort()
    return result1, result2

def comparedraws(a, b):
    # This is a function that compares two sets of numbers
    # in order to check if they match. It returns the number
    # of normal balls and lucky stars that have matched.
    mainballs = 0
    luckystars = 0
    for k in range(5):
        if a[0][k] in b[0]:
            mainballs += 1
    for j in range(2):
        if a[1][j] in b[1]:
            luckystars += 1
    return mainballs, luckystars

def playlotto(n):
    # Generate a draw and n lucky dips and compare each lucky
    # dip to the draw to see if there is a match. Return a
    # table with the number of matches.
    winner = gendraw()
    print(winner)
    wins = {0:[0,0,0],1:[0,0,0],2:[0,0,0],3:[0,0,0], 4:[0,0,0], 5:[0,0,0]}
    for k in range(n):
        ld = gendraw()
        com = comparedraws(ld, winner)
        if com[0] >= 3:
            if com[0] == 5:
                print(ld, com)
        wins[com[0]][com[1]] += 1
    print("\nStars:\t0\t1\t2")
    for ln in range(6):
        print(str(ln) + "\t" + str(wins[ln][0]) + "\t" +str(wins[ln][1]) + "\t" +str(wins[ln][2]))
    return None