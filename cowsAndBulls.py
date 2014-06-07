import os
from random import sample
#GLOBAL VARIABLE
inp_list=[]
word_list=[]
cows=0
bulls=0
game_round=0
game_limit=5
word_length=4
game_end=False
history_stack=[]

def createWord():
    global word_list,cows,bulls,game_round
    game_round=0
    word_list=sample(range(0,9),word_length)
    #print word_list
    history_stack=[]
#Need to remove first 0

def takeInput():
    global inp_list
    print "Please print the 4 numbers to check : "
    user_inp=str(raw_input())
    inp_list=map(int,user_inp)

def checkCowsBulls():
    global cows,bulls,game_end,history_stack
    cows=0
    bulls=0
    matched_list=[]
    #print inp_list,word_list
    matched_list=[i for i in inp_list if i in word_list]
    #print matched_list
    '''for match in matched_list:
        for index in (position for position,item in enumerate(word_list) if item==match):
            print index,match '''
   
    for match in matched_list:
        if word_list.index(match)==inp_list.index(match):
            #print match , word_list.index(match) , inp_list.index(match) ,"cows"
            cows+=1
       
        else:
            #print match , word_list.index(match) , inp_list.index(match) , "bulls"
            bulls+=1

    cur_stack=[inp_list,cows,bulls]
    history_stack+=[cur_stack]
    if cows==len(word_list):
        game_end=True
    else:
        game_end=False

def displayHistory():
    for inp_h,cow_h,bull_h in history_stack:
        print inp_h, "\t| COWS : ", cow_h, " | BULLS : ", bull_h 

def display_word():
    print "\n\tThe actual word is \t" ,word_list

if __name__=='__main__':
    global game_end
    os.system('cls')
    createWord()
    while(not game_end):
        game_round+=1
        takeInput()
        os.system('cls')
        checkCowsBulls()
        if(game_end):
            print "You Won ",word_list
        else:
            displayHistory()
        if(game_round == game_limit and not game_end):
            game_end=True
            display_word()
