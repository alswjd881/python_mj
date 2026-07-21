# 10000개 숫자 작성 필요 없이 출력하는 반복문!!

i = 1

while i < 10001:
    print(i)
    i += 1


##for 문
for i in range(1, 11, 1): #1에서 10전까지 1칸씩 띄워서 출력
    print(i)

# 연습문제 1
total =0
num =1

while num <= 100:
    total += num
    print(num, total)
    num += 1

##구구단 연습문제2
for dan in range(2,10):
    for num in range(1,10):
        print(f"{dan}*{num}={dan*num}")

##
lst=[1, 10, "안녕하세요","파이썬", 3.14]

for data in lst:
    print(data)

#
for i in range(1,6):
    print(i, "번째 출력")

for i in range(0,12,2):
    print("짝수:", i)


# 건너띄기
for i in range (1, 10):
    if i == 5:
        continue

    print(i)

#멈추기
for i in range (1, 10):
    if i == 5:
        break

    print(i)

#
while True:

    print("1, 학생등록")
    print("2, 학생목록출력")
    print("3, 프로그램 종료")
    cmd =int(input("명령어:"))

    if cmd ==1:
        print("학생등록 로직입니다.")
    elif cmd ==2:
        print("학생 목록을 출력합니다.")
    elif cmd ==3:
        print("프로그램을 종료합니다.")
    else:
        print("존재하지 않는 명령어.")
