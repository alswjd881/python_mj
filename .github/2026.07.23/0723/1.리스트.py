##리스트의 메소드

lst = [1, 2]

print("추가 전:", lst) # [1, 2]

lst.append(100)

print("추가 후:", lst) # [1, 2, 100]

lst.insert(2,"안녕하세요")

print("insert로 추가 후:", lst) # [1, 2, '안녕하세요', 100]

lst.remove(2)

print("remove(2)를 이용하여 제거한 후:", lst) #[1, '안녕하세요', 100]

nums = [3, 1, 3, 4]

# 추가 (마지막에 추가)
nums.append(5)
print("추가 후:", nums)

# 추가 (특정 위치에 추가)
nums.insert(0, 100)
print("특정 위치 추가 후:", nums)

# 제거 -> 매개변수로 들어가는 건 제거할 인덱스가 아니라 제거할 값
# 이 메소드는 인덱스 0에 가장 가까운 값 하나만 제거해 준다
nums.remove(3)
print("3 제거 후:", nums)

# 제일 마지막 요소 꺼내오기
last = nums.pop()
print("마지막 요소:", last)



""" 
정렬과 뒤집기
"""

scores = [88, 95, 70, 100, 99]

scores. sort(reverse=True)
print("내림차순:", scores) #내림차순

scores. sort(reverse=False)
print("오름차순:", scores)

scores.reverse()
print("역순으로 변환", scores)

print("길이:", len(scores))
print("최댓갑:", max(scores))
print("최솟값:", min(scores))

##연습문제 1
nums = [1, 2, 3, 4, 5]

nums.append(6)
nums.remove(3)
print(nums)

#연습문제 2

num1 = int(input("정수를 입력하세요:"))
num2 = int(input("정수를 입력하세요:"))
num3 = int(input("정수를 입력하세요:"))
num4 = int(input("정수를 입력하세요:"))
num5 = int(input("정수를 입력하세요:"))

lst = []
lst.append(num1)
lst.append(num2)
lst.append(num3)
lst.append(num4)
lst.append(num5)

print(lst)
print("최댓값은", max(lst))
print("최솟값은", min(lst))

##연습문제 for문 사용하면?

lst =[]

for i in range(0, 5):
    num = int(input("정수입력:"))
    lst.append(num)

print("리스트", lst)
print("최댓값은", max(lst))
print("최솟값은", min(lst))
