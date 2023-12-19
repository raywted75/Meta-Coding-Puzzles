# Write any import statements here

def getWrongAnswers(N: int, C: str) -> str:
  # Write your code here
  wrong = list()
  
  for correct in C:
    if correct == 'A':
      wrong.append('B')
    else:
      wrong.append('A')
    
  return ''.join(wrong)
