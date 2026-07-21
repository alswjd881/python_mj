a = 10 # 대입 연산자

print("감소 전 a:",a)

a -= 1 # 복합 대입 연산자
print("감소 후 a:",a) #a=9

a += 34
print("1 증가 후 a:",a) #a=43

a *= 2
print("2 곱한 후:", a) #a=86

##논리연산자
print(True and True) #and : 둘 다 True 일 때만 True
print(False or True) #or : 둘 중 하나라도 True이면 True
print(not True) # not : 뒤에 오는 모든 결과값을 뒤집어줌

## 예제
db_id = "admin"
db_password="1234"

input_id = input("아이디를 입력해주세요:")
input_password= input("패스워드를 입력해주세요:")

if db_id == input_id and db_password == input_password:
    print("로그인이 완료되었습니다.")
else:
    print("로그인에 실패하였습니다.")


