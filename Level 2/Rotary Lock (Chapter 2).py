# ref: https://leetcode.com/discuss/interview-question/1368609/Facebook-Rotary-Lock-Practice-Puzzle/1199341

from typing import List
import math
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  # Write your code here
  def cost(pre, cur):
    return min(abs(cur - pre), min(pre, cur) + N - max(pre, cur))
  
  states = [0]
  
  for i in range(M):
    next_states = [0] * i + [math.inf]
    
    for j, time in enumerate(states):
      next_states[j] = time + cost(C[i - 1] if i - 1 >= 0 else 1, C[i])
    
    for j, time in enumerate(states):
      next_states[-1] = min(
        next_states[-1],
        time + cost(C[j - 1] if j - 1 >= 0 else 1, C[i])
      )
    
    states = next_states

  return min(states)
