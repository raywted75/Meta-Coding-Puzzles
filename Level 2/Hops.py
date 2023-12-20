from typing import List
# Write any import statements here

def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
  # Write your code here
  """
  We will get the optimal sequence of hops if each time we start from the leftmost frog and let it hop to the next empty lily pad. Eventually, frogs will line up before the last lily pad, and it takes 1 hop for each one to hop to the last pad. 
  
  Therefore, # hops = # empty pads bwteen them + # frogs
  
  For example, N = 10, P = [1, 4, 6]
  1. frogs will hop to lily pad [2, 3, 5, 7, 8, 9] in sequence. -> 6
  2. frogs end at [7, 8, 9], and each frog takes 1 hop to the last lily pad. -> 3
  3. The optimal hops = 6 + 3 = 9
  """
  pos = sorted(P)
  pos.append(N)
  
  res = F
  for i in range(1, len(pos)):
    res += pos[i] - pos[i - 1] - 1
  
  return res