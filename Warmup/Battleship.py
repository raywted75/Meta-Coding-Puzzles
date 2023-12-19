from typing import List
# Write any import statements here

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  # Write your code here
  ships = 0
  
  for i in range(R):
    for j in range(C):
      ships += G[i][j]
  
  hit_prob = ships / (R * C)
      
  return hit_prob
