
#1번
m = int(input("얼마 있어요?"))
def money(m):
    if m > 10000:
        print("고기를 먹는다")
    elif m > 5000:
        print("국밥을 먹는다")
    else:
        print("라면을 먹는다.")
money(m)
#2번
answer = []
for i in range(1,6):
    ans = input('{}번 과일을 입력하세요'.format(i))
    answer.append(ans)

for i in range(len(answer)):
    print(i,"번째 과일은",answer[i],"입니다")

#3번
cookies = {"탱커":"우유맛쿠키","딜러":"칠리맛쿠키","힐러":"천사맛쿠키","서포터":"석류맛쿠키"}
cookies["탱커"] = "다크초코맛쿠키"
cookies["딜러"] = "라떼맛쿠키"
cookies["힐러"] = "허브맛쿠키"
print(cookies)

#4번
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b


while True:
    a = int(input("원하는 숫자를 입력하세요. 1. 더하기 2.빼기 3.곱하기 4.나누기 5.종료"))
    if a != 5:
        n1 = input("숫자1 을 입력하세요")
        n2 = input("숫자2 을 입력하세요")
    if a == 1:
        print(add(n1,n2))
    if a == 2:
        print(sub(n1,n2))
    if a == 3:
        print(mul(n1,n2))
    if a == 4:
        print(div(n1,n2))
    if a == 5:
        break

#5번
class Person:
    def __init__(self,name):
        self.name = name
    def hello(self):
        print("안녕 내 이름은 ",self.name,"이야")
    def walk(self):
        print("나는 걷는 중!")

class Worker(Person):
    def __init__(self,company,mental=50):
        Person.__init__(self,name)
        self.company = company
        self.mental = mental
    def hello(self):
        print("안녕 내 이름은 {0}이고 내가 다니는 회사는 {1}".format(self.name,self.company))
    def work(self):
        self.mental -= 10
        if mental >= 0:
             print("나는 일하는 중, 내 멘탈지수 : {0}".format(self.mental))
        else:
            print("더는 일 못해")
11