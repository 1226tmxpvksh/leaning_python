a=int(input("물건값을 입력하시오:")) #거스름돈 만들기
b=int(input("1000원 지폐의 개수:"))
c=int(input("500원 지폐의 개수:"))
d=int(input("100원 동전개수:"))

f=(b*1000+c*500+d*100)-a

print("500원=",f//500)
f=f%500
print("100원=",f//100)
f=f%100
print("10원=",f//10)
f=f%10
print("1원=",f//1) #거스름돈 나오게 하기

a=10
b=20
c=30
d=40

a,b=b,a
a,b,c,d=d,c,b,a

print(a,b,c,d) #40,30,10,20

a=10
b=20
c=30
d=40

if(a>b):
	print("a가 큽니다")
else:
    print("b가 더 큽니다") #if문 쓰기

import turtle
t=turtle.Pen()

while True: #무한반복
	direction=input("왼쪽=left, 오르쪽=right:")
	if direction=="left":
		t.left(60)
		t.forward(50)
	if direction=="right":
		t.right(60)
		t.forward(50)

#홀수 짝수 구별
for i in range(0,10): #다른 반복문으로 while a<10:
	x=int(input("정수를 입력하세요: "))
	if x%2==0:
		print("짝수입니다")
	else:
		print("홀수입니다")

#물건값 계산
a=int(input("구입 금액을 입력하시오:"))
if a>=100000:
	b=a*0.05
	c=a-b
print("지불 금액은",c,"입니다")

#졸업 학점 검사하기
a=int(input("이수한 학점수를 입력하시오:"))
b=float(input("평점을 입력하시오:"))
if a>=140 and b>=2.0:
	print("졸업 가능합니다!")
else:
	print("졸업이 힘듬니다!")

#날짜/시간 출력하기
import datetime

now=datetime.datetime.now()
print(now.year,"년")
print(now.month,"월")
print(now.day,"일")
print(now.hour,"시")
print(now.minute,"분")
print(now.second,"초")

#계절 구분하는 프로그램

import datetime

now=datetime.datetime.now()

if 3<=now.month<=5:
	print("이번달은 {}월로 봄입니다!".format(now.month))
if 6<=now.month<=8:
	print("이번 달은 {}월로 여름입니다!".format(now.minth))
if 9<=now.month<=11:
	print("이번 달은 {}월로 가을입니다!".format(now.month))
if now.month ==12 or 1<=now.month<=2:
	print("이번 달은 {}월로 겨울입니다!".format(now.month))
