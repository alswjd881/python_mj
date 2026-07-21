##나이 예제
age = int(input("나이를 입력해 주세요:"))

if age>19:
    print("성인입니다.")
else:
    print("미성년자입니다.")


##요일 예제
num = int(input("정수 입력:"))

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
    print("해당 요일은 존재하지 않습니다.")

    ###
print("메뉴를 선택하세요: ")
print("1. 아메리카노")
print("2. 카페라떼")
print("3. 아이스티")

choice = int(input("번호 입력: "))

if choice == 1:
    print("아메리카노를 선택했습니다.")
elif choice == 2:
    print("카페라떼를 선택했습니다.")
elif choice == 3:
    print("아이스티를 선택했습니다.")
else:
    print("잘못된 선택입니다.")

print("주문이 완료되었습니다.")

##연습문제 1
n = int(input("정수 입력:"))

if n<0 :
    print("음수입니다.")
elif n==0:
    print("0입니다.")
else n>0:
    print("양수입니다.")

##연습문제 2
num1 = int(input("1정수입력:"))
num2 = int(input("2정수입력:"))
num3 = int(input("3정수입력:"))

max_num =0

if num1>num2 and num1>num3:
    max_num = num1
elif num2>num3 and num2>num1:
    max_num = num2
else :
    max_num = num3

print(f"최댓값은 {max_num}입니다.")

min_num = 0
if num1 < num2 and num1 < num3:
    min_num = num1
elif num2 < num3 and num2 < num1:
    min_num = num2
else:
    min_num = num3

print(f"최댓값은 {min_num}입니다.")