def ReverseArray(arr):
  left = 0
  right = len(arr) - 1

  #increase till left is less then right 
  while left <right:
     #swap
    arr[left],arr[right] = arr[right], arr[left]

    #incease the left pointer
    left +=1

    #decrease the right pointer
    right -=1

arr=[10,20,30,40,50]
ReverseArray(arr)
print(arr)
