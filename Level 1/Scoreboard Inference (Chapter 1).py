from typing import List
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
  # Write your code here
  """
  The solution must consist of 0 to 2 numbers of 1-point problems and other two-point problems.
  
  1. If the maximum score is 5, the solution must be [1,2,2].
  2. If the maximum score is 6,
    2-1. If there is no odd score in scores, the solution is [2,2,2].
    2-2. If there is any odd score in scores, the solution is [1,1,2,2].
  """
  return max(S) // 2 + any(s % 2 for s in S)
