username = input("아이디 입력: ")
password = input("비밀번호 입력: ")

if username == "admin" and password == "1234":
    print("로그인 성공!")
    print("관리자 권한으로 접속했습니다.")
else:
    print("로그인 실패!")
    print("아이디 또는 비밀번호가 잘못되었습니다.")

print("시스템 종료")