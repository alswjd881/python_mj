mj = {
    "이름" : "김민정",
    "나이" : 26,
    "주소" : "대전"
}

print(mj["이름"])
print(mj["나이"])
print(mj["주소"])

mj["키"] = "159.6" ##추가하고 싶을때
print(mj)

## 리스트 안에 이게 있나 찾고 싶을때 if문

person = {"name": "Lee", "age": 30, "city": "Seoul"}

person ["email"] = "alswjd881@naver.com"

if "email" in person:
    print(person["email"])

##삭제
person = {"name": "Lee", "age": 30, "city": "Seoul"}

print("name 키 있나요?", "name" in person)
print("gender 키 있나요?", "gender" in person)

del person["city"]
print("삭제 후:", person)

##딕셔너리 순회
scores= {"kim":90, "lee":85, "park":92}

for key in scores:
    print("이름:", key, "점수:", scores[key])

print("키 목록:", list(scores.keys()))
print("값 목록:", list(scores.values()))
print("키 목록:", list(scores.items()))

"""메서드 
- `get(key, default)` : 키가 없으면 기본값 반환
- `keys()` : 모든 키 반환
- `values()` : 모든 값 반환
- `items()` : 모든 키-값 쌍 반환 (튜플 형태로 반환)
- `update()` : 다른 딕셔너리 병합
"""

##get
user = {"id":"admin", "pw":"1234"}
print("loading...")

print(user.get("aaa", "존재하지 않는 키"))

print("loading...")

##update
user = {"id":"admin", "pw":"1234"}
print("추가 전:", user)
user.update({"email":"alswjd881@naver.com", "name":"김민정"})
print("추가 후:", user)

## 다른 메서드
user = {"id":"admin", "pw":"1234"}

for k,v in user.items():
    print(f'{k}: {v}')
print(user.items()) #dict_items([('id', 'admin'), ('pw', '1234')])
print(user.values()) #dict_values(['admin', '1234'])
print(user.keys()) #dict_keys(['id', 'pw'])

##연습문제 1
student = {"name": "홍길동", "age": 20, "major": "CS"}

student.update({"age" : 21}) # student['age'] += 1 이것도 가능
student.update({"grade":"A"})

for k,v in student.items():
    print(k,v)


##연습문제 2

score ={}

for i in range(3):
    name = str(input("이름입력:"))
    grade= int(input("점수 입력:"))
    score.update({name:grade})
print(score)

avg_score = sum(score.values())/len(score)
print(f"평균:{avg_score}점")

##다른 문제풀이

scores = {}

student1 = input("학생 이름:")
score1 = int(input("점수:"))
scores[student1] = score1

student2 = input("학생 이름:")
score2 = int(input("점수:"))
scores[student2] = score2


student3 = input("학생 이름:")
score3 = int(input("점수:"))
scores[student3] = score3

avg_score = sum(score.values())/len(score)
print(f"평균:{avg_score}점")