a=input("첫번째 정수를 입력하시오:") #두수 중 큰수 출력
b=input("두번째 정수를 입력하시오:")
if a>b:
	print("a가 큼")
elif a==b:
	print("a와b가 같음")
else:
	print("b가 큼")

a= input("문자열을 입력하시오: ") #문자열의 중간문자
b=len(a)
c=b//2

if b%2==0:
	print(a[c-1:c+1])
else:
	print(a[c-1])

print("숫자 게임에 오신 것을 환영합니다") #숫자 맞추기 게임
a=10
b=int(input("숫자를 맞춰보세요:"))

while(1):
	if(a>b):
		print("작음")
		break
	elif(a==b):
		print("정답!")
		print("게임종료")
		break
	else:
		print("너무 큼")
		break

import random #가위 바위 보
player=input("(가위,바위,보) 중에서 하나를 선택하시오: ")
number=random.randint(0,2)
if player == '가위':
   if number == 0:
      print("비김")
   elif number == 1:
      print("짐")
   else:
      print("이김")

if player == '바위':
   if number == 0:
      print("이김")
   elif number == 1:
      print("비김")
   else:
      print("짐")

if player == '보':
   if number == 0:
      print("짐")
   elif number == 1:
      print("이김")
   else:
      print("비김")


a=int((input("도형을 선택하시오(1. 사각형, 2. 삼각형, 3.원):"))) #면적 구하기
width=int(input("가로:")) #면적 구하기
height=int(input("세로:")) 
radius=3.14
if(a==1):
	print("면적:",width*height)
elif(a==2):
	print("면적:",width*height*(1/2))
else:
	print("면적:",width*width*radius)


for x in [0,1,2,3,4,5,6,7,8,9]:
	print(x, end="")#줄바꿈 안됨

print()

for i in range(0,101,2): #range(start,stop,step)
	print(i,end="")

터틀
import turtle
star = turtle.Turtle()
for i in range(5):
	star.forward(300)
	star.right(144)

import turtle
p = turtle.Turtle()
num_sides=int(input("숫자를 입력하시오: "))
side_length=70
angle=360.0/num_sides
for i in range(num_sides):
	p.forward(side_length)
	p.right(angle)

i=0;
while i<5:
	print("환영합니다")
	i=i+1
	break
print("반복이 종료되었습니다")

a=int(input("숫자를 입력하시오: ")) #구구단

for i in range (1,10):
	print(a,"=", a*i)

sum=0 #배수의 합

for i in range(0,100,3):
	sum=sum+i
print("1부터 100사이의 모든 3의 배수의 합은", sum ,"입니다")

list1=[]
for i in range (1,101):
	list1.append(i)
list1.append("a") #리스트 뒤에 추가
print(sum(list1))


