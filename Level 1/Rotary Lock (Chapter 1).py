from typing import List
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  # Write your code here
  pre = 1
  res = 0
  
  for i in range(M):
    cur = C[i]
    res += min(abs(cur - pre), min(pre, cur) + N - max(pre, cur))
    pre = cur
    
  return res
