#튜플 생성과 인덱싱

fruits = ("사과", "배", "포도", "귤") #이게 튜플 (소괄호로 표현 가능)

print("첫 번째 과일:", fruits[0])
print("마지막 과일:", fruits[-1])
print("길이:", len(fruits))

"""
fruits[0]= 'apple' #변경 불가한 거 알 수 있음!!!
print(fruits)
"""
### 3가지 프린트 방법
fruits = ("사과", "배", "포도", "귤")

"""
1번째
for f in fruits:  # for문 이용
    print(f)
"""

"""
2번째
for i in range(0, len(fruits)):  #길이 출력
print(fruits[i])
"""

"""
3번째 
print(fruits[0])           #인덱싱 이용
"""

#다중대입
a=10
b=20

temp =a
a=b
b=temp

print("a:", a)
print("b:", b)

#언패킹(다중대입)
person = ("Alice", 25, "Seoul")

name, age, city = person #갯수가 같아야 함!
print("name:", name)
print("age:", age)
print("city:", city)

##cound , index
nums = (1,2,3,2,4,2,4)

print(nums.count(4)) # 해당 값이 개수 반환
print(nums.index(4)) #해당 값의 인덱스 반환

##여러 자료형 포함
data = (3.14, "김민정", 1, True)

for item in data:
    print("요소:", item, "->타입:", type(item))
print("총 개수:",len(data))

#세트
dct = {"name": "Lee", "age": 30} #키와 값을 가지는 딕셔너리

s = {1,2,3,4, 1, 1} # 중복 허용 x, 순서 없는 세트

print(s) # 중복 허용 않기에 1 하나만 나옴

#add, remove
s = {1,2,3,4, 1, 1} # 중복 허용 x, 순서 없는 세트

s.add(1000) # 값 추가
s.remove(3) # 값 제거 (인덱스 제거 ㄴㄴ)

print(s)

##빈 딕셔너리 vs 빈 세트
dct ={} #빈 딕셔너리
dct['name'] = 'Lee'

s=set() #빈 세트
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
print(s)

text = "hello"

letters = set(text) #l이 하나만 나옴 (중복 허용 x) #input 값 입력받아도 똑같..
print(letters) #세트는 순서 보관 안하기에 출력시 뒤죽박죽

##세트의 연산
a={1,2,3,4}
b={3,4,5,6}
#합집합
print("합집합")
print(a|b)
print(a.union(b))
#교집합
print("교집합")
print(a&b)
print(a.intersection(b))
#차집합
print("차집합")
print(a-b)
print(a.difference(b))

##discard, set
s = {1, 2, 3}

s.add(4)
print("add:", s)

s.remove(2)
print("remove:", s)

s.discard(10)  # 오류 발생하지 않음
print("discard 후:", s)

s.clear()
print("clear:", s)
##연습문제 1
t = (10, 20, 30, 40, 50)

print(t[2])
print(t.count(20))
print(t.index(30))

##연습문제 2
a_subjects = set()
b_subjects = set()

print("A학급의 수강 과목을 입력해주세요.")
for i in range(3):
    subject = (input("과목입력:"))
    a_subjects.add(subject)

print("B학급의 수강 과목을 입력해주세요.")
for i in range(3):
    subject = (input("과목입력:"))
    b_subjects.add(subject)

print(f"a,b 동시에 수강하는 과목은 : {a_subjects.intersection(b_subjects)}")