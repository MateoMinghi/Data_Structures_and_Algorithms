#Selection sort
#O(n^2)

array_to_sort = [7,8,9,8,7,6,5,6,7,8,9,0]

def selection_sort(array_to_sort):

  for i in range(0, len(array_to_sort)):
    min_value = i

    for j in range(i+1, len(array_to_sort)):
      if array_to_sort[j] < array_to_sort[min_value]:
        min_value = j
    
    if min_value != i: 
      array_to_sort[min_value], array_to_sort[i] = array_to_sort[i], array_to_sort[min_value]
  
  return array_to_sort

if __name__ == "__main__":
  print(selection_sort(array_to_sort)) #prints the sorted list
