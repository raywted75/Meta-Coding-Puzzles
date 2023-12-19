from typing import List
# Write any import statements here

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
  # Write your code here
  stack = list()
  
  for r in R:
    stack.append(r)
    
    i = len(stack) - 1 
    while i > 0 and stack[i - 1] >= stack[i]:
        stack[i - 1] = stack[i] - 1
        if stack[i - 1] == 0:
          return -1
        i -= 1
  
  return sum(x != y for x, y in zip(stack, R))
