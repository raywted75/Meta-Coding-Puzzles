from typing import List
# Write any import statements here

def getSecondsElapsed(C: int, N: int, A: List[int], B: List[int], K: int) -> int:
  # Write your code here
  A.sort()
  B.sort()

  one_round_tunnel_time = sum(b - a for a, b in zip(A, B))
  rounds = K // one_round_tunnel_time
  remainder = K % one_round_tunnel_time

  if remainder == 0:
    return B[-1] + (rounds - 1) * C

  for a, b in zip(A, B):
    remainder -= b - a
    if remainder <= 0:
      return rounds * C + b + remainder
