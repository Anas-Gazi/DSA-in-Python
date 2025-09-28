def MajorityElement(nums):
  count = 0
  cand = 0
  for x in nums:
    if count == 0:
      cand = x
    count+=1 if x == cand else -1
  return cand
nums =[1,2,2,2,2,1,1,1,1,2,2,1]
result = MajorityElement(nums)
print(result)