from typing import List
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  # Write your code here
  S.sort()
  
  res = 0
  
  l = 0 - K
  for r in S:
    res += (r - l - 1 - K) // (K + 1)
    l = r
  
  res += (N - l) // (K + 1)
  
  return res
