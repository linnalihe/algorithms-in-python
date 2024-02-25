def find_pairs_with_given_difference(arr, k):
  
  output = []
  seen = set()
  for y1 in arr:
    seen.add(y1)
    
  for y2 in arr:
    x = k + y2
    if(x in seen):
      output.append([x, y2])
  
  return output