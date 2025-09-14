import math
def isPrime(n):

  #check if n is 1 0r 0
  if n<=1:
    return False

  #check if n is 2 or 3
  if n==2 or n==3:
    return True

  #check if n is divisiable by 2 or 3
  if n%2 ==0 or n%3 ==0:
    return False
  
   # Check from 5 to square root of n
    # Iterate i by (i+6)

  i= 5
  while (i<=math.sqrt(n)):
    if n%i ==0 or n% (i+2) ==0:
      return False
    i+=6

  return True
  
if __name__ =="__main__":
  n=47
  if(isPrime(n)):
    print("true")
  else:
    print("false")
  