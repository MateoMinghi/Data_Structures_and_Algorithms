#Merge sort is a divide and conquer algorithm
#O(n log n)
def merge_sort(arr):
  if len(arr) > 1:
    half = len(arr) // 2

    L = arr[:half]
    R = arr[half:]

    merge_sort(L)
    merge_sort(R)

    i = 0
    j = 0
    k = 0

    while i < len(L) and j < len(R): 
      if L[i] < R[j]: 
        arr[k] = L[i] 
        i+= 1
      else: 
        arr[k] = R[j] 
        j+= 1
      k+= 1
          
        # Checking if any element was left 
    while i < len(L): 
      arr[k] = L[i] 
      i+= 1
      k+= 1
          
    while j < len(R): 
      arr[k] = R[j] 
      j+= 1
      k+= 1
  return arr

if __name__ == "__main__":
  arr = [9,8,4,1,2,5,6,2,4,7,5]
  print(merge_sort(arr))
