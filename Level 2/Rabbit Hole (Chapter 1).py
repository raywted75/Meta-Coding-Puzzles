from typing import List
# Write any import statements here

def getMaxVisitableWebpages(N: int, L: List[int]) -> int:
  # Write your code here
  for i in range(N):
    L[i] -= 1

  dp = [0] * N
  
  for i in range(N):
    if not dp[i]:
      j = i
      position = dict()
      while not dp[j] and j not in position:
        position[j] = len(position)
        j = L[j]
      
      if dp[j]:  # page j is a calculated circle
        for k, pos in position.items():
          dp[k] = dp[j] + len(position) - pos
      else:
        for k, pos in position.items():
          if pos < position[j]:  # page k is not part of the circle
            dp[k] = len(position) - position[k]
          else:  # # page k is part of the circle
            dp[k] = len(position) - position[j]
  
  return max(dp)
