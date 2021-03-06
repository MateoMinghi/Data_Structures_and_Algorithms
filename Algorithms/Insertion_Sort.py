#Insertion Sort Algorithm
#O(n^2)

array_to_sort = [7,8,9,8,7,6,5,6,7,8,9,0]

def InsertionSort(array_to_sort):

  for i in range(1, len(array_to_sort)):

    value_to_sort = array_to_sort[i]

    while value_to_sort < array_to_sort[i-1] and i>0:
      array_to_sort[i], array_to_sort[i-1] = array_to_sort[i-1], array_to_sort[i] 
      i -= 1

  return array_to_sort


if __name__ == "__main__":
  print(InsertionSort(array_to_sort))
