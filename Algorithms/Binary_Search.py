#binary search is a divide and conquer algorithm
#0(log n)
sequence = [2,4,5,6,7,8,9,10,12,13,14]
item = 5

def Binary_Search(sequence, item):
  begin_index = 0
  end_index = len(sequence) - 1

  while begin_index <= end_index:
    midpoint = begin_index + (end_index - begin_index) // 2
    midpoint_value = sequence[midpoint]
    
    if midpoint_value == item:
      return midpoint
    elif item < midpoint_value:
      end_index = midpoint - 1
    else:
      begin_index = midpoint + 1
  return None


print(Binary_Search(sequence, item)) #this returns the index value of the item we are looking for
