word = 'hello world' #문자열
w = 'h' #문자

print(word)
print(w)

"""
문자열 주석 처리 
다른 언어에선 문자열과 문자 표기 다름 
파이썬은 똑같음
"""

text = "  Hello, Python!  "

print(text)
print(text.strip())           # 양쪽 공백 제거
print(text.lower())           # 소문자
print(text.upper())           # 대문자
print(text.strip()[0:5])      # 슬라이싱 ("Hello")
# hello, python -> h는 0번임.
print(text.replace("Python", "hello"))  # 문자열 치환

#       012345 0 h 1 e 2 l 3 l 4 o 5
#  0~4면 h~l 까지 (4이전에서 끊기)
text = "hello, world"
print(text.strip()[0:4])      # 슬라이싱 ("Hello")

name, score = "kim", 92
print("이름은", name, "이고 점수는", score, "점입니다.")
print(f"{name}님의 점수는 {score}점 입니다.")

items = ["사과", "배", "포도"]
joined = ",".join(items)
print("장바구니:", joined)

#       0     1   2    3      4
fruits = "사과, 배, 포도, 바나나"
fff = fruits.split(",")
print(fff[0:2]) #단어 하나하나가 자리 하나임

s = input("문장 입력: ")
words = s.split(" ")
print(words)
print(f"단어의 갯수는 {len(words)}입니다.")

# 종합 연습문제1
a = int(input("숫자를 입력해주세요"))
b = int(input("숫자를 입력해주세요"))

print("a + b", a + b) #합
print("a - b", a - b) #차
print("a * b", a * b) #곱
print("a // b", a // b) #나누기 몫
print("a % b", a % b) #나머지

# 종합 연습문제2

word = "Python is fun"

#fun 을 awesome으로 변경
replace_word = word.replace("fun", "awesome") #+.upper[]
print("fun을 awesome으로 변경한 후:", replace_word)

replace_word = word.replace("fun", "awesome").upper() #이건 대문자까지 한번에
print("fun을 awesome으로 변경한 후:", replace_word)


##

first_name = "minjeong " #여기서 띄어쓰기 넣어야 프린트에 띄어쓰기 들감
last_name = "kim"
full_name = first_name + last_name
print(full_name)

hello = "안녕하세요"
print(hello*3)

hello = "안녕하세요안녕하세요안녕하세요"
print(hello/3) #이거는 불가