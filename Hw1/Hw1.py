import random
import math
import string

def guessing_game():
    start=1
    stop=101
    goldenNumber=random.choice(range(start, stop))
    count=1
    value=-1
    while value!=goldenNumber:
        value=int(input("What is your guess?\n"))
        if value==goldenNumber:
            print('You got the number! It took you '+str(count)+' times!')
        else:
            if value>goldenNumber:
                print('Your number was too high!')
            else:
                print('Your number was too low!')
        count=count+1

def reversed_guessing_game():
  index=0
  window=100
  value=''
  count=0
  while(value!='C'):
    count=count+1
    print("The computer guesses "+str(index+math.trunc(window/2)))
    value=input("Was it too high or too low?")
    if value=="C":
      print("Wow the machine got it right in "+str(count)+" tries")
    elif value=="H":
      window=window/2
    elif value=="L":
      index=index+window/2
      window=window/2

def revised_reversed_guessing_game(min,max):
  index=min
  window=max
  value=''
  count=0
  while(value!='C'):
    count=count+1
    print("The computer guesses "+str(round(index+window/2)))
    value=input("Was it too high or too low?").upper()
    if value=="C":
      print("Wow the machine got it right in "+str(count)+" tries")

    elif value=="H":
      window=window/2
    elif value=="L":
      index=index+window/2
      window=window/2
    if(count>round(math.log(max-min,2)) and value!='C'):
      print("Stop cheating")
      value='C'
revised_reversed_guessing_game(0,2000)