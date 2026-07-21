
nums = [3, 1, 4]

nums.append(5)
print("append:", nums)

nums.insert(1, 2) # (a ,b) a에 b를 추가
print("insert:", nums)

nums.remove(4)
print("remove:", nums)

last = nums.pop()
print("pop:", last, nums)