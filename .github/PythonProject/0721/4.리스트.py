##리스트 생성과 인덱싱

fruits = ["사과", "배", "포도", "귤"]

print("첫 번째 과일:", fruits[0])   # 인덱스 0
print("마지막 과일:", fruits[-1])  # 음수 인덱스 -1은 역순!!!
print("리스트 길이:", len(fruits))

# 리스트 요소 변경
fruits[1] = "바나나"
print("변경 후:", fruits)

##리스트 안에 리스트

data = [10, 3.14, "Python", True, [1, 2, 3]]

print("정수:", data[0])
print("실수:", data[1])
print("문자열:", data[2])
print("참:", data[3])
print("리스트 안의 리스트:", data[4][2])

# 리스트를 생성하는 방법
lst = [1, 3.14, "안녕하세요", True, "파이썬", [1, 2, 3]]

for i in range(0, len(lst)):
    print(f"데이터는 {lst[i]}이고 타입은 {type(lst[i])}입니다.")

#for 문 이용한 리스트
lst = [10, 3.14, "Python", True,"파이썬", [1, 2, 3]]

for data in lst:
    print(f"데이터는 {data}이고 타입은 {type(data)}입니다.")

## 리스트의 연산 (나누기 빼기는 안됨!!)
a = [1, 2, 3]
b = [4, 5]

print("리스트 덧셈:", a + b)    # [1,2,3,4,5]
print("리스트 곱셈:", b * 3)   # [4,5,4,5,4,5]
print("길이:", len(a + b * 2)) #b*2 먼저 -> 4545123 -> 7


#슬라이싱

nums = [10, 20, 30, 40, 50, 60]

print("앞 3개:", nums[:3])   # [10,20,30]
print("뒤 3개:", nums[-3:])  # [40,50,60]
print("인덱스가 짝수 번째:", nums[::2])  # [10,30,50]
print("역순:", nums[::-1])   # [60,50,40,30,20,10]


#메소드
"""
- `append(x)`: 맨 뒤에 요소 추가
- `insert(i, x)`: 원하는 위치에 요소 추가
- `remove(x)`: 값 제거
- `pop()`: 마지막 요소 꺼내기
- `sort()`: 정렬
- `reverse()`: 역순

"""

nums = [3, 1, 4]

nums.append(5)
print("append:", nums)

nums.insert(1, 2) # (a ,b) a에 b를 추가
print("insert:", nums)

nums.remove(4) #4라는 값을 제거.// 4번째 값제거 아님!!
print("remove:", nums)

last = nums.pop()
print("pop:", last, nums)