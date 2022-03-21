
"""Homework 3 Template
This is the template for HW3 in CSE 4256 at The Ohio State University.
"""
# TODO
# Besides the syntax used to create them, what are three fundamental differences
# between a Python \lstinline{set} and a Python \lstinline{list}?
# 1. Sets are unordered while lists are ordered
# 2. Lists are immutable while sets are mutable
# 3. Sets cant have duplicate elements while lists can
def all_unique(ls: list) -> bool:
  """Reports whether the list contains all unique elements.
  Positional Arguments:
  ls -- A list of hashable items, such as ints.
  """
  return [True if ls.count(ls[i])==1 else False for i in range(len(ls))].count(False)<1

def maybe_apply_all(s: set, f=lambda x: x + 5):
  """Applies function f to each element of s, updating s in place."""
  for x in s:
    x = f(x)
# TODO
# Is this function correct according to the docstring? If not, what's wrong?
# Answer:No its not correct. The value X is immutable



def apply_all(s: set, f=lambda x: x + 5):
  """Applies function f to each element of s, updating s in place."""
  holder={}
  while len(s)!=0:
    holder.add(f(s.pop))
  s=holder
# TODO
# Does your solution to apply_all(s, f) work for all f?
# Answer: No because the elements of s may not be within f's domain, so the element cant be updated.
def subset_sum(s: set, t: int) -> bool:
  """Solves the Subset Sum problem.
  Returns True iff there is a subset of s whose sum is equal to t.
  Positional arguments:
  s -- A set of integers.
  t -- The target sum.  
  """
  output=False
  #assume that there is no subset
  if(len(s)<2):
    #base case, a single integer is equal to t or there are no other subsets
    if (t in s):
      output=True
    else:
      output=False
  else:
    sum=0
    for i in s:
      sum=sum+i
      #sum the current set
    
    if(sum==t):
      output= True
      #the set sums to t
    if output!=True:
      #the set didnt sum to t and needs to be split into subsets
      for i in s:
        #creates the next smallest subsets, with the total amount of elements being one less than the current set. The method is called on these smaller subsets. This will lead to each method call being applied to sets that are one element smaller than the parent until the base case is reached.
        test=subset_sum(s.difference({i}),t)
        if(test):
        #if one child is true, then output is true:
          output=True
  return output
  # TODO
def is_subset_sum(sub: set, s: set, t: int) -> bool:
  """Checks a proposed solution to the Subset Sum Problem.
  Returns True iff sub is a subset of s and the sum of the elements of s is
  equal to t.
  Positional arguments:
  sub -- A set of integers; the proposed subset.
  s -- A set of integers.
  t -- The target sum.
  """
  sum=0
  if(sub.issubset(s)):
    for i in sub:
      sum=sum+i
  return sum==t
# **********************
#  Challenge Activities
# **********************
def subset_sum_approx(s: set, t: int) -> bool:
  """Approximates the Subset Sum problem.
  
  Returns True iff there is a subset of s whose sum is approximately t.
  Positional arguments:
  s -- A set of integers.
  t -- The target sum.  
  """
  # TODO
  pass
def subset_sum_dyn(s: set, t: int) -> bool:
  """Solves the Subset Sum problem using dynamic programming.
  
  Returns True iff there is a subset of s whose sum is approximately t.
  Implemented using Dynamic Programming.
  Positional arguments:
  s -- A set of integers.
  t -- The target sum.  
  """
  # TODO
  pass
def subset_sum_h_s(s: set, t: int) -> bool:
  """Solves the Subset Sum problem using the Horowitz-Sahni algorithm.
  
  Returns True iff there is a subset of s whose sum is approximately t.
  Implemented using the Horowitz-Sahni algoritm. 
  Positional arguments:
  s -- A set of integers.
  t -- The target sum.  
  """
  #TODO
  pass
