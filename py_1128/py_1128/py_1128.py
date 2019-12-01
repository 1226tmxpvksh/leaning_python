#from tkinter import* #label

#window = Tk()

#label = Label(window, text="Hello World!")
#label.pack()

#window.mainloop()

#from tkinter import* #Button

#window = Tk()

#b1 = Button(window, text="첫번째 버튼")
#b2 = Button(window, text="두번째 버튼")
#b1.pack()
#b2.pack()

#window.mainloop()

#from tkinter import* #Button 정력

#window = Tk()

#b1 = Button(window, text="첫번째 버튼")
#b2 = Button(window, text="두번째 버튼")
#b1.pack(side=LEFT)
#b2.pack(side=LEFT)

#window.mainloop()

#from tkinter import* #button padding x,y

#window = Tk()

#b1 = Button(window, text="첫번째 버튼")
#b2 = Button(window, text="두번째 버튼")
#b1.pack(side=LEFT,padx=30)
#b2.pack(side=LEFT,pady=30)

#window.mainloop()

#from tkinter import* #텍스트 변경

##window = Tk()

##b1 = Button(window, text="첫번째 버튼")
##b2 = Button(window, text="두번째 버튼")
##b1.pack(side=LEFT,padx=10)
##b2.pack(side=LEFT,pady=10)
##b1["text"]="One"
##b2["text"]="Two"

##window.mainloop()

#from tkinter import* #버튼의 이벤트를 처리하면

#def callback():
#	button["text"]="버튼이 클릭되었음!"

#window = Tk()
#button=Button(window, text="클릭", command=callback)
#button.pack(side=LEFT)

#window.mainloop()

#from tkinter import*
#class App:
#	def __init__(self):
#		window = Tk()
#		helloB=Button(window, text="Hello", command=self.hello, fg="red")
#		helloB.pack(side=LEFT)
#		quitB = Button(window, text="Quit", command=self.quit)
#		quitB.pack(side=LEFT)
#		window.mainloop()

#	def hello(self):
#		print("Hello 버튼이 클릭되었음!")

#	def quit(self):
#		print("Quit 버튼이 클릭외었음!")

#App()

#from tkinter import* #색상
#window =Tk()
#button = Button(window, text="버튼을 클릭하세요")
#button.pack()
#button["fg"]="yellow"
#button["bg"]="green"
#window.mainloop()

#from tkinter import*
#window =Tk()
#color=colorchooser.askcolor()
#print(color)
#widow.mainloop()

#from tkinter import*

#window = Tk()

#w = Label(text="Helvetica", font="Helvetica 16")
#w.pack()

#window.mainloop()

#import tkinter as tk
#import tkinter.font as font 

#class App:
#   def __init__(self):
#      root = tk.Tk()

#      self.customFont = font.Font(family = "Helvetica", size = 12)

#      buttonframe = tk.Frame()
#      label = tk.Label(root, text = "Hello, World!",font = self.customFont)
#      buttonframe.pack()
#      label.pack()

#      bigger = tk.Button(root, text = "폰트를 크게",command = self.BigFont)
#      smaller = tk.Button(root, text = "폰트를 작게",command = self.SmallFont)
#      bigger.pack()
#      smaller.pack()
#      root.mainloop()

#   def BigFont(self):
#      size = self.customFont['size']
#      self.customFont.configure(size = size + 2)

#   def SmallFont(self):
#         size = self.customFont['size']
#         self.customFont.configure(size = size - 2)

#app = App()

#from tkinter import*

#window = tk()
#photo = photoimage(file='c:\\users\\1226t\\desktop\\iu.jpg')
#w=label(window, image=photo)
#w.photo=photo
#w.pack()
#window.mainloop()

#from tkinter import*

#window =Tk()

#Label(window,text="Times Font 폰트와 빨강색을 사용합니다", fg="red", font="Times 32 bold italic").pack()
##Label(window, text="Helvetica 폰트와 녹색을 사용합니다.", fg="blue",bg="yellow", font="Helvetica 32 bold italic").pack()
##window.mainloop()

#from tkinter import*

#window=Tk()
#Label(window,text="이름").grid(row=0)
#Label(window,text="나이").grid(row=1)

#e1=Entry(window)
#e2=Entry(window)

#e1.grid(row=0,column=1)
#e2.grid(row=1,column=1)

#window.mainloop()

#from tkinter import*

#def show():
#	print("이름:%s\n 나이: %s" %(e1.get(),e2.get()))

#parent = Tk()
#Label(parent,text="이름").grid(row=0)
#Label(parent,text="나이").grid(row=1)

#e1=Entry(parent)
#e2=Entry(parent)

#e1.grid(row=0, column=1)
#e2.grid(row=1, column=1)

#Button(parent,text='보이기', command=show).grid(row=3, column=1, sticky=W, pady=4)
#Button(parent,text='종료', command=parent.quit).grid(row=3, column=0, sticky=W, pady=4)

#mainloop()

#from tkinter import*

#window=Tk()
#T=Text(window,height=5,width=60)
#T.pack()
#T.insert(END,"집가고 싶다")
#mainloop()

#from tkinter import*
#from math import*

#def calculate(event):
#	label.configure(text = "결과: "+str(eval(entry.get())))

#window=Tk()

#Label(window,"파이썬 수식 입력").pack()
#entry = Entry(window)
#entry.bind("<Return>", calculate)
#entry.pack()

#label=Label(window,text="결과")
#label.pack()

#w.mainloop()

#import time
#from tkinter import*
#window=Tk()
#canvas = Canvas(window, width=400, height=300)
#canvas.pack()
#id=canvas.create_oval(10,100,50,50,fill="#ffffff")

#for i in range(100):
#	canvas.move(id,3,0)
#	window.update()
#	time.sleep(0.05)

#from tkinter import*
#window=Tk()
#canvas = Canvas(window, width=400, height=300)
#canvas.pack()

#id=canvas.create_oval(10,100,50,150,fill="green")

#def move_right(event):
#	canvas.move(id,5,0)
#canvas.bind_all('<KeyPress-Right>',move_right)

#window.mainloop()

#from tkinter import*

#window=Tk()
#choice=IntVar()

#Label(window,text="가장 선호하는 프로그래밍 언어를 선택하시오", justify=LEFT, padx=20).pack()
#Radiobutton(window, text="Python",padx=20,variable=choice,value=1).pack(anchor=W)
#Radiobutton(window, text="C",padx=20,variable=choice,value=2).pack(anchor=W)
#Radiobutton(window, text="Java",padx=20,variable=choice,value=3).pack(anchor=W)
#Radiobutton(window, text="Swift",padx=20,variable=choice,value=4).pack(anchor=W)

#window.mainloop()

from tkinter import*

window=Tk()

lb=Listbox(window, height=4)
lb.pack()
lb.insert(END,"Python")
lb.insert(END,"C")
lb.insert(END,"Java")
lb.insert(END,"Swift")

window.mainloop()
