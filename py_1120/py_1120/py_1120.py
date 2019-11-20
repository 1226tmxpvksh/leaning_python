#numbers = {2, 1, 3} #set 연산자

#for x in numbers:
#	print(x,end="")

s=' Never put off till tomorrow what tou can do today.'

print(s.split())
print(s.isalpha())
print(s.startswith(s))
print(s.endswith(s))
print(s.find(s))
print(s.rfind(s))
print(s.count(s))
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.replace("put","one"))
print(s.strip())
print(s.lstrip())
print(s.rstrip())

#a=input("문자열을 입력하시오:")
#b=len(a)
#c=''
#for i in range(b,-1,-1):
#	c=c.append(i)
#if c==a:
#	print('회문')

class Counter:
	def reset(self):
		self.count =0
	def increment(self):
		self.count +=1
	def get(self):
		return self.count
a=Counter()

a.reset()
for i in range(5):
	a.increment()
print("카운터 a의 값은",a.get())