statement=input("문자열을 입력하시오: ") #문자열 조사

alphas=0
digits=0
spaces=0

for c in statement:
	if c.isalpha():
		alphas=alphas+1
	if c.isdigit:
		digits=digits+1
	if c.isspace():
		spaces=spaces+1
print("알파벳 문자의 개수=",alphas)
print("숫자 문자의 개수=",digits)
print("스페이스의 개수=",spaces)

def get_sum(start, end): #1부터10까지 함수
	sum=0
	for i in range(start, end+1):
		sum+=i
	return sum

value = get_sum(1,10)
print(value)


def get_sum(start, end): #함수
	sum=0
	for i in range(start, end+1):
		sum+= i
	print(sum)

value = get_sum(1,10)
print(value)

def asterisk_test(a,b,*num): #가변 인수
	return a+b+sum(num)

print(asterisk_test(1,2,3,4,5))