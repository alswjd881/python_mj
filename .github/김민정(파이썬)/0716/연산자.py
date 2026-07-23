#산술, 비교, 논리 연산자
a=7
b=3

#산술 연산
print(a+b)
print(a//b)
print(a**b)

#비교연산
print(a>b)
print(a==b)
print(a!=b) #같지 않나요
print(a>=b)

#논리연산
print("조건1 and 조건2:", (a>5) and (b>5))
#and 연산은 연결되어 있는 거 전부 true일때 true
print("조건 1 or 조건2:", (a<5) or (b<5))
#or은 연결되어 있는 것중 하나라도 true면 true

#로그인할때
db_id = "admin123"
db_password = "1234"

input_id = input("id를 입력해주세요")
input_password = input("비밀번호를 입력해주세요")

if input_id == db_id and input_password == db_password:
    print("로그인 완료")
else:
    print("아이디 혹은 비번 일치하지 않습니다.")


#not 연산자
age = int(input("age:"))

flag =age >= 19
print(flag)

if not flag :
    print("해당나이는 미성년자입니다")

#리스트 -> []

nums = [1,2,3,4]

print(2 in nums)
print(10 not in nums)
print(3 not in nums)

x = [1,2]
y = [1,2]
z = x

print("x==y ?", x==y)
print("x is y?", x is y) # x가 y랑 같지만 x가 y는 아니다. is not -> true
print("x is z?", x is z)

#대입연산자

num1 =77
num2 =23
num3 = num1 + num2

num1 += num2 #num1에 num2를 더하여 새로운 값을 할당 -> 이제 num1은 100
num3 -= num1 #num3에서 num1 빼 새로운 값 할당 -> num1이 100이 됬으니 num3은 0



#연습문제1
a = int(input("숫자 입력:"))
b = int(input("숫자 입력:"))

print("(a+b) * (a-b)=", (a+b) * (a-b))
print("(a>b) and ((a+b)%2 == 0)는", (a>b) and ((a+b)%2 == 0))


#연습문제2
fruits = ["사과", "배", "포도", "바나나"]
need = input("과일 이름:")

if need in fruits:
    print("리스트 안에 포함되어있습니다.")

else:
    print("포함되지 않은 과일입니다.")