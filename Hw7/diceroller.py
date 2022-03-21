
import random

def diceroller(sides=6, samples=100):
  output={}
  options=[]
  for i in range(1,sides+1):
    options.append(i)
    output[i]=0
  for i in range(samples):
    sampled=random.choice(options)
    output[sampled]=output[sampled]+1
  return output

def print_bar_chart(dict):
  print("GRAPH BELOW-------------------------------------")
  output=""
  for i in range(1,len(dict)+1):
    output=""
    for j in range(dict[i]):
      cap=78-len(str(i))
      if(j<cap):
        output=output+"\u2588"
    print(str(i)+": "+output)

