# Write any import statements here
from collections import defaultdict

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Write your code here
  
  l, r = defaultdict(int), defaultdict(int)
  
  l[C[0]] += 1
  for i in range(2 * X, X + Y + 1):
    if i < N:
      r[C[i]] += 1
  
  res = 0
  
  for i in range(X, N - X):
    if C[i] == 'A':
      res += l['P'] * r['B']
      res += l['B'] * r['P']
    
    if i - Y >= 0:
      l[C[i - Y]] -= 1
    l[C[i - X + 1]] += 1
    
    r[C[i + X]] -= 1
    if i + Y + 1 < N:
      r[C[i + Y + 1]] += 1
  
  return res
