from typing import List
# Write any import statements here

def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
  # Write your code here
  """
  Example:
  - V = [10, 2, 8, 6, 4]
  - C = 3
  - S = 0.15
  1. The optimal solution is entering the mail room on days 1 and 5. 
  2. On day 1, we collect 10 - 3 = 7
  3. On day 5, packages in the mail room are [2, 8, 6, 4], so the expected value = (2 * 0.85^3 + 8 * 0.85^2 + 6 * 0.85^1 + 4) - 3 = 13.10825
  4. The maximum expected profit is 7 + 13.10825 = 20.10825
  
  - Let dp[i] be the maximum expected profit we can achieve if we enter the mail room on day i, assuming we make optimal decisions on all days before i.
  - To find dp[i], we need to find dp[j] (the previous day we entered the mail room) that maximizes our profit. If j = 0, we did't enter the mail room before.
  """
  dp = [0] * (1 + N)
  res = 0
  
  for i in range(1, N + 1):
    values = 0
    prob = 1
    
    for j in range(i - 1, -1, -1):
      values += V[j] * prob
      dp[i] = max(dp[i], dp[j] + values)
      prob *= 1 - S
    
    dp[i] -= C
    res = max(res, dp[i])
  
  return res
