from typing import List
from collections import defaultdict
from heapq import heappush, heappop
# Write any import statements here

def getSecondsRequired(R: int, C: int, G: List[List[str]]) -> int:
  # Write your code here
  pq = list()
  visited = set()
  portals = defaultdict(list)
  
  for i in range(R):
    for j in range(C):
      if G[i][j] == 'S':
        heappush(pq, (0, i, j))
        visited.add((i, j))
      elif G[i][j] not in 'E.#':
        portals[G[i][j]].append((i, j))
  
  while pq:
    s, i, j = heappop(pq)
    
    if G[i][j] == 'E':
      return s
    
    for x, y in (0, 1), (1, 0), (0, -1), (-1, 0):
      if 0 <= i + x < R and 0 <= j + y < C:
        if (i + x, j + y) not in visited:
          if G[i + x][j + y] != '#':
            heappush(pq, (s + 1, i + x, j + y))
            visited.add((i + x, j + y))
    
    if G[i][j] not in 'SE.#':
      if G[i][j] in portals:
        for x, y in portals[G[i][j]]:
          if x != i or y != j:
            heappush(pq, (s + 1, x, y))
            visited.add((x, y))
        portals.pop(G[i][j])
        
  return -1
