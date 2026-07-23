# hello.py 파일 내용
print("첫 번째 파이썬 실행 테스트")

for i in range(3):
    print(i + 1, "번째 실행 중...")

print("실행이 끝났습니다!")

# 버전을 변수로 흉내 내어 실행 흐름 제어
version = "3.12"
print("파이썬 버전:", version)

if version.startswith("3"):
    print("최신 파이썬 버전입니다!")
else:
    print("버전을 업데이트하세요!")

print("프로그램 종료")

# 1. 프로그램은 위에서 아래로 한 줄씩 실행됩니다.
print("Hello, Python!") # 첫 출력
name = "학생"
print("반갑습니다,", name) # 문자열 출력
a = 10
b = 20
print("a + b =", a + b) # 연산 결과 출력
print("파이썬 시작 성공!")


name = "한코딩" # 문자열 -> String
a = 10 # 정수 -> Integer
b = 3.14 # 실수 -> float

print("문자열:", type(name))
print("정수:", type(a))
print("실수:", type(b))


# 사용자 입력 → 처리 → 출력
user = input("당신의 이름은 무엇인가요? ")

greet = f"안녕하세요, {user}님!"
print(greet)  # 인사 출력

age = int(input("나이를 입력해 보세요: "))
print("내년에는", age + 1, "살이 되겠군요!")
print("첫 번째 파이썬 코드 완성!")


# f-String을 사용하는 경우
age = int(input("나이를 입력해 보세요:"))

print (f"내년에는 {age + 1}살이 되시는군요")


numbers = [5, 10, 15, 20]
total = 0
for n in numbers:
    total += n
    print("현재 합:", total)  # 디버깅 포인트
avg = total / len(numbers)
print("평균:", avg)
print("계산 완료!")


# 사용자 입력 → 처리 → 출력
user = input("당신의 이름은 무엇인가요? ")

greet = f"안녕하세요, {user}님!"
print(greet)  # 인사 출력

age = int(input("나이를 입력해 보세요: "))
print("내년에는", age + 1, "살이 되겠군요!")
print("첫 번째 파이썬 코드 완성!")


# f-String을 사용하는 경우
age = int(input("나이를 입력해 보세요:"))

print (f"내년에는 {age + 1}살이 되시는군요")


numbers = [5, 10, 15, 20]
total = 0
for n in numbers:
    total += n
    print("현재 합:", total)  # 디버깅 포인트
avg = total / len(numbers)
print("평균:", avg)
print("계산 완료!")


def greet(name):
    msg = f"안녕하세요, {name}님!"
    print(msg)
    return len(msg)

length = greet("파이썬 학습자")
print("메시지 길이:", length)
print("PyCharm에서 단계별 실행(F8)으로 확인해 보세요.")


x = 10        # 정수(int)
print(x, type(x))

x = "hello"   # 문자열(str)
print(x, type(x))

x = 3.14      # 실수(float)
print(x, type(x))

# 같은 변수 x가 상황에 따라 다른 자료형을 가짐


# 변수 선언 및 출력
name = "Alice"
age = 20
height = 165.5

print("이름:", name)
print("나이:", age)
print("키:", height, "cm")

a = 15
b = 4
print("덧셈:", a + b)
print("나눗셈(실수):", a / b)
print("나눗셈(몫):", a // b)
print("나머지:", a % b)
print("거듭제곱:", a ** b)

a = 15
b = 4
print("덧셈:", a + b)
print("나눗셈(실수):", a / b)
print("나눗셈(몫):", a // b)
print("나머지:", a % b)
print("거듭제곱:", a ** b)

num1 = int(input("첫 번째 정수 입력:"))
num2 = int(input("두 번째 정수 입력:"))
num3 = int(input("세 번째 정수 입력:"))

max_num = max(num1, num2, num3)
min_num = min(num1, num2, num3)

print(f"최댓값은 {max_num}입니다.")
print(f"최댓값은 {min_num}입니다.")

name, score = "Kim", 92
print(f"{name}님의 점수는 {score}점입니다.")  # f-string

items = ["사과", "배", "포도"]
joined = ", ".join(items)     # 리스트 → 문자열
print("장바구니:", joined)

print(joined.split(", "))     # 문자열 → 리스트
print("-".join(["2025", "09", "01"]))  # 날짜 포맷

