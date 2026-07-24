"""
1. 리스트 활용
2. 이름과 점수, 나이를 보관
3. while문 이용해 무한 루프 만들고
4. if문 이용해서 명령어 제어
5. 학생은 3명까지 등록 가능
6. 학생 삭제 기능(삭제할 학생 번호 입력:1 ->0)
ㄴㄴ 학생이 없을 수도 있음(고려사항)
"""
from itertools import count
lst = ["names", "scores", "ages"]
names =[]
scores=[]
ages=[]

count = 0

while True:
    print("1. 학생등록")
    print("2. 학생목록")
    print("3. 학생삭제")
    print("4. 학생 검색")
    print("0. 프로그램 종료") #break
    cmd =int(input("명령어 입력:"))

    if cmd ==1:
        if count ==3:
            print("더 이상 등록할 수 없습니다.")
            continue
        name = input("학생이름:")
        names.append(name)
        score = input("학생점수:")
        scores.append(score)
        age = input("학생나이:")
        ages.append(age)

        count += 1

        print(names)
        print(scores)
        print(ages)

    elif cmd ==2:
        if count ==0:
            print("등록된 정보가 없습니다.")
            continue

        print()
        print("===학생 목록 리스트===")

        for i in range(len(names)):
            print(f"{i+1}번째 학생 이름: {names[i]}/ 점수: {scores[i]}/ 나이: {ages[i]}")
        print()
    elif cmd ==3:
        if count ==0:
            print("등록된 학생이 없습니다.")
            continue
        delete_num = int(input("삭제할 학생 번호:")) #index방식으로 지워줘야 함
        delete_index = delete_num-1 #삭제할 학생의 데이터가 들어가 있는 인덱스

        if delete_index <0 or delete_index >= len(names):
            print("삭제할 수 없는 학생입니다.")
            continue
        else:
            names.pop(delete_index)
            scores.pop(delete_index)
            ages.pop(delete_index)

        count -= 1

    elif cmd ==4:

    elif cmd ==0:
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 명령어입니다.")
