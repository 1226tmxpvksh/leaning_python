#s=' Never put off till tomorrow what tou can do today.'

#print(s.split())
#print(s.isalpha())
#print(s.startswith(s))
#print(s.endswith(s))
#print(s.find(s))
#print(s.rfind(s))
#print(s.count(s))
#print(s.upper())
#print(s.lower())
#print(s.capitalize())
#print(s.replace("put","one"))
#print(s.strip())
#print(s.lstrip())
#print(s.rstrip())

#a=input("문자열을 입력하시오:") #회문 판단
#b=len(a)
#c=''
#for i in range(b-1,-1,-1):
#	c=c+a[i]
#if c==a:
#	print('회문')
#else:
#	print("회문이 아닙니다")

#f=open("E:\\studnet.txt", "r") #CSV 파일

#for line in f.readlines(): 
#	line = line.strip()
#	print(line)
#	words = line.split(",")
#	for word in words:
#		print("   ", word)

#def process(w):
#	output =""
#	for ch in w:
#		if(ch.isalpha()):
#			output += ch
#	return output.lower()
#words= set()

#fname = input("입력파일 이름:")
#file = open(fname,"r")

#for line in file:
#	linewords = line.split()
#	for word in linewords:
#		words.add(process(word))

#print("사용된 단어의 개수=", len(words))
#print(words)

#a = input("입력 파일 이름: ") #파일에서 중복되지않는 단어 개수
#b = open(a)
#data = b.read()
#data = data.split()   

#for i in range(0,len(data)):
#	s = ''
#	for c in data[i]:
#		if c.isalnum():
#			s += c
#	data[i] = s.lower()

#dic = {}

#for s in data:
#	if s not in dic.keys():
#		dic[s] = 1
#	else:
#		dic[s] += 1

#print(dic)

a = open('test.txt', encoding='utf-8') #문자열 분석
data = a.read()
digits = spaces = alphas = 0
for i in data:
	if i.isdigit():
		digits += 1
	elif i.isalpha():
		alphas += 1
	elif i is ' ':
		spaces += 1

print('digits:',digits,'alphas:',alphas,'spaces:',spaces)
