from typing import List
from collections import deque
# Write any import statements here

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  # Write your code here
  eaten = deque()
  eaten_type = set()
  res = 0
  
  for i in range(N):
    if D[i] not in eaten_type:
      res += 1
    
      eaten.append(D[i])
      eaten_type.add(D[i])
      
      if len(eaten) > K:
        eaten_type.remove(eaten.popleft())

  return res
