######제어문 - 조건문(if, elife, else), 반복문(for, while)
#elife = else if 줄인거

score = int(input("점수를 입력해주세요:"))

if score >= 90:
    print("합격입니다.")
else:
    print("불합격입니다.")


######홀수, 짝수 구별하기

a=int(input("숫자를 입력하세요: "))

if a %2 == 0:
    print(a, "는 짝수입니다.")
else:
    print(a, "는 홀수입니다.")


####### elif문
num = int(input("숫자를 입력하세여: "))

if num == 1:
    print("월요일")
elif num == 2:
    print("화요일")
elif num == 3:
    print("수요일")
elif num == 4:
    print("목요일")
elif num == 5:
    print("금요일")
elif num == 6:
    print("토요일")
elif num == 7:
    print("일요일")
else:
    print("해당요일은 존재하지 않습니다.")

####성적등급 분류
score = int(input("점수를 입력하세요:"))

if score>=90:
    print("A학점")
elif score>=80:
    print("B학점")
elif score>=70:
    print("C학점")
else:
    print("F학점")

print("등급 판별 완료")

##로그인
username = input("아이디 입력: ")
password = input("비밀번호 입력: ")

if username == "admin" and password == "1234":
    print("로그인 성공!")
    print("관리자 권한으로 접속했습니다.")
else:
    print("로그인 실패!")
    print("아이디 또는 비밀번호가 잘못되었습니다.")

print("시스템 종료")