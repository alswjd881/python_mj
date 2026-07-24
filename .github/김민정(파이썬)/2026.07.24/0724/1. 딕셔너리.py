#복습

dct={}

for i in range(3):
    name = str(input("이름 입력:"))
    score = int(input("점수 입력:"))
    dct[name]=score

print(dct)

##키 검사와 삭제
person = {"name": "Lee", "age": 30, "city": "Seoul"}

print("name 키 있나요?", "name" in person)
print("gender 키 있나요?", "gender" in person)

del person["city"]
print("삭제후:", person)
print("길이", len(person))

##키나 값만 꺼낼 수도 있음
person = {"name": "Lee", "age": 30, "city": "Seoul"}

for key, value in person.items():
    print(person.values())
    print(person.keys())