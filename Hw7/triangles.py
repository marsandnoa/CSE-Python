def triangles(n):
  output=[];
  sum=0;
  for i in range(n):
    sum=sum+i
    output.append(sum)
  return output
def ctriangles(n):
  return [sum(range(1,i+1)) for i in range(n)]

def factorial(r):
  output=1;
  for i in range(1,r+1):
    output=output*i;
  if(output==0):
    output=1
  return output
  
def pascal(r):
  output=[];
  amoElements=1;
  row=[]
  checker=[]
  for i in range(r):
    row=[]
    for j in range(amoElements):
      number=factorial((i))/(factorial(j)*factorial((i-j)))
      row.append(number)
    output.append(row)
    amoElements=amoElements+1
  
  return output