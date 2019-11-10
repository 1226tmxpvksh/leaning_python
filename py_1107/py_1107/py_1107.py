print(1+1) #2가 출력
print(52) #52가 출력
print(273) #273이 출력
print(1,'\n',2) #1 다음줄에 2가 나옴
print(1,'\n','qeqeqeqeqe',22345678,sep="                 ") #1 다음줄에 qe 나오고 숫자 나오고 문자 간격이 넓어짐
print('Hello World') #Hello World 출력

a = 2
print(a) #a의 수인 2가 출력

a = "asdasdasdad"
print(a) #a의 값인 asdasdasdad 출력

a = 1.123123
print(a) #a의 값인 1.123123  출력

a = 'asd'
print(a) #a의 값인 asd 출력

a=int(input()) #a의 값을 입력
print(a) #a의 값을 출력
print(a+1234) #a의 값에 1234더하기

print('"안녕하세요"라고 말했습니다') #"안녕하세요"로 됨
print("'배가 고픕니다'라고 생각했습니다") #'배가 고픕니다'로 됨
print("\"안녕하세요\"라고 말했습니다") #"안녕하세요"로 됨
print('\'배가 고픕니다\'라고 생각했습니다') #'배가 고픕니다'로 됨

print("asdf"*3) #asf 3번 출력 

print("문자 선택 연산자에 대해 알아볼까요?")
print("안녕하세요"[0]) #안 출력
print("안녕하세요"[1]) #녕 출력
print("안녕하세요"[2]) #하 출력
print("안녕하세요"[3]) #세 출력
print("안녕하세요"[4]) #요 출력

print("안녕하세요"[1:4]) #안녕하세요의 1번자리 부터 4번 미만 까지 출력

alp='abcdefghijklmnopqrstuvwxyz'
print(alp[5:11]) #alp의 5번자리부터 11자리 미만 까지 출력
print(alp[18:26]) #alp의 18번 자리 부터 26자리 미만 까지 출력
print(alp[-26:-18]) #alp의 반대 26자리부터 반재 18자리 까지 출력
print(len(alp)) #문자열의 자리수 출력
for i in alp: #alp에 있는 수까지 출력
	print(i)

print(len("안녕하세요")) #안녕하세요가 5자리니까 5 출력

a=15
b=8
print(a+b,a-b,a*b,a/b,a%b,a//b,a**b) #a와 b의 + - * / 나머지 몫 출력

a=input() #a의 값 입력
print(a) #a의 값 출력

tmp=''
for i in alp:
	tmp +=i #tmp=tmp+i
	print(tmp) #a부터 z까지 늘어나면서 출력

