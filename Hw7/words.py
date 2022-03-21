def words(s):
  index=0;
  start=-1;
  while len(s)>index:
    if(" "==s[index]) or index==len(s)-1:
      if(len(s)-1==index):
        yield s[start+1:]
      else:
        yield s[start+1:index]
        start=index
    index=index+1
# TODO implement this generator function


def firstlines(filename):
  f = open(filename, 'r')
  flag=0
  dict={}
  while flag!=-1:
    holder=f.readline()
    if(len(holder)==0):
      flag=-2
    else:
      for i in words(holder):
        if(i=="\n"):
          pass
        else:
          newkey={i:flag}
          dict.update(newkey)
    flag=flag+1
  f.close
  return dict