def find_array_quadruplet(arr, s):
  n = len(arr)
  
  if n < 4:
    return []
  arr.sort()
  
  for i in range(0, n -3):
    for j in range(i+1, n-2):
      target = s - (arr[i] + arr[j])
      
      low = j + 1
      high = n - 1
      
      while low < high:
        if arr[low] + arr[high] < target:
          low += 1
        elif arr[low] + arr[high] > target:
          high -= 1
        else:
          return [arr[i], arr[j], arr[low], arr[high]]
  return []
