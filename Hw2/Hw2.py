s="PYTHON"

#a
print(s[5])
print(s[-1])
#b
#PYTHON
print(s[0:6])
#c
#PYT
print(s[:3])
#d
#PTO
print(s[::2])
#e
print(s[0:4])
#f
print(s[3:6:2])
#g
print(s[6:0:-2])

#2
def fiblist(n):
  output=[0,1]
  while len(output)<n:
    output.append(output[len(output)-1]+output[len(output)-2])
  return output
#3
def ispartitionable(s):
  output=False
  i=0
  while i<len(s):
    if(sum(s[0:i])==sum(s[i:len(s)])):
      output=True
    i=i+1
  return output

#4
n=5
[[1 if i==j else 0 for i in range(n)] for j in range(n)]

#5
m=[[1,2],[3,4]]
sums=[sum(m[i]) for i in range(len(m))]
print(sums)
#6
def vowelcount(s):
  s=s.upper()
  sum=0
  vowels="AEIOU"
  for j in range(len(vowels)-1):
      sum=sum+s.count(vowels[j])
  return sum

#7
def listfromcsv(s):
  return [s.split("\n")[i].split(",") for i in range(len(s.split("\n")))]

print(listfromcsv("5,8,hello,2\n9,14,world,1344"))