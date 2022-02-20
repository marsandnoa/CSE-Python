"""Contains a class that represents a Fraction (i.e., a rational number).

Author: Noah
Collaborators: [collaborators' names here]
"""

# Import statements go here
from functools import total_ordering
  
  
@total_ordering
class Fraction:
    """A rational number.

    Fraction should have no public instance variables.
    """

    def __init__(self, num: int, d: int):
        """Produces the fraction n/d in reduced form.

        By "reduced form", we mean that in the produced fraction, the numerator
        and denominator are relatively prime.
        """
        x=2;
        if(num==0):
          num=0
          d=1
        if(d==0):
          #you are a troll and a griefer, 0/0 is not valid
          num=1
          d=1
        else:
          #the init method is poorly developed bc it should determine if num or den is higher before looping, but not worth fix
          while x<num:
            if(num%x==0) and (d%x==0):
              num=num/x
              d=d/x
            else:
              x=x+1
         
        self.num=num
        self.d=d


    def mixed_number(self) -> str:
        """Returns a string representation of self in mixed number form.

        For example, if self is 5/3, mixed_number should return "1 2/3".
        """
        output="";
        mixed=0;
        n=this.num
        while(n-this.d>0):
          mixed=mixed+1;
          n=n-d;
        output=str(mixed)+" "+str(self.num)+"/"+str(self.d)
        return output


    def __repr__(self):
        """Returns a string that is [numerator]'/'[denominator].

        __repr__ is called by the builtin function repr, or by print if
        there is no definition for __str__.
        """

        output=""
        output=str(self.num)+"/"+str(self.d)
        return output

    def __str__(self):
        """Returns a string that is [numerator]'/'[denominator].

        __str__ is called by the builtin print function
        """
        output=""
        if(self.d!=1):
          output=str(self.num)+"/"+str(self.d)
        else:
          output=str(self.num)
        return output

    def __eq__(self, other: 'Fraction') -> bool:
        """Reports whether self is the same number as other.

        __eq__ is called by the equality operator, e.g., frac1 == frac2.
        """
        
        return ((self.num==other.num) and (self.d==other.d))

    def __neg__(self) -> 'Fraction':
        """Returns the negation of self.

        __neg__ is called by the unary minus operator, e.g., -frac.
        """
        return Fraction(-self.num,-self.d)

    def __invert__(self) -> 'Fraction':
        """Returns the reciprocal of self.

        __invert__ is called by the unary tilde operator, e.g., ~frac.
        """
        return Fraction(self.d,self.num)


    def __add__(self, other: 'Fraction') -> 'Fraction':
        """Returns the sum of self and other.

        __add__ is called by the binary plus operator, e.g., frac1 + frac2.
        """
        return Fraction(self.num*other.d+other.num*self.d,self.d*other.d)

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        """Returns the product of self and other.

        __mul__ is called by the binary times operator, e.g., frac1 * frac2.
        """
        return Fraction(self.num*other.num,self.d*other.d)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        """Returns the difference of self and other.

        __sub__ is called by the binary minus operator, e.g., frac1 - frac2.
        """
        return Fraction(self.num*other.d-other.num*self.d,self.d*other.d)

    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        """Returns the quotient of self and other.

        __div__ is called by the binary division operator, e.g., frac1 / frac2.
        """
        return Fraction(self.d*other.num,self.d*other.num)

    def __lt__(self, other: 'Fraction') -> bool:
      return Fraction(self.num*other.d-other.num*self.d,self.d*other.d).num<0
      
if __name__ == "__main__":
  #TESTS
#Initialization
#edge
  print("INPUT -----------------------")
  print(Fraction(0,0))
  print(Fraction(0,1))
  print(Fraction(1,1))
  print(Fraction(3,2))
  print(Fraction(1,0))
#Basic
  print(Fraction(10,4))
  print(Fraction(20,5))
  print(Fraction(100,10))
  print(Fraction(27,5))
#the init method is poorly developed bc it should determine if num or den is higher
  print(Fraction(5000,24))
  print("ADDITION ----------------------")
#Addition
  print(Fraction(20,5)+Fraction(20,5))
  print(Fraction(20,7)+Fraction(20,7))
  print(Fraction(20,6)+Fraction(20,1))
  print(Fraction(20,0)+Fraction(20,0))
  print(Fraction(20,5)+Fraction(40,5))

  print("LT ----------------------")
#MISC
  print(Fraction(50,5)>Fraction(40,5))
  print(Fraction(0,5)>Fraction(40,5))
  print(Fraction(40,5)>Fraction(40,5))

  print(Fraction(50,5)<Fraction(40,5))
  print(Fraction(40,5)<Fraction(40,5))
  print(Fraction(0,5)<Fraction(40,5))

  print(Fraction(50,5)==Fraction(40,5))
  print(Fraction(40,5)==Fraction(40,5))
  print(Fraction(0,5)==Fraction(40,5))

  print(Fraction(50,5)>=Fraction(40,5))
  print(Fraction(40,5)>=Fraction(40,5))
  print(Fraction(0,5)>=Fraction(40,5))

  print(Fraction(50,5)<=Fraction(40,5))
  print(Fraction(40,5)<=Fraction(40,5))
  print(Fraction(0,5)<=Fraction(40,5))


