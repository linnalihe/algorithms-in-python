# https://www.pramp.com/challenge/9PNnW3nbyZHlovqAvxXW
# passed all tests
def moveZerosToEnd(arr):

  # brute force is to bubble the zero to the right
  # O(n^2)
  # form new array get all zeros, get non-zeros
  # time O(n), space O(n)
  # [1, 0, 2]
  # [0, 0, 1, 2]
  # [1, 10, 2, 8, 3, 6, 0, 0, 0, 4, 0, 5, 7, 0]
  # keep a counter of 0s and using this to find the index
  # of the first 0 and swap
  
  # [1, 10, 2, 8, 3, 6, 4, 5, 7, 0, 0, 0, 0, 0]
  counter = 0
  for idx in range(len(arr)):
    if arr[idx] == 0:
      counter+=1
      
    else:
      arr[idx], arr[idx-counter] = arr[idx-counter], arr[idx]
      
  
  return arr