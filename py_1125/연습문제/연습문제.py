class Shape: #도형
	def __init__(self):
		self.x=0
		self.y=0
	def setPosition(self,x,y):
		self.x=x
		self.y=y
	def area(self):
		pass
	def parimeter(self):
		pass
class rectangle:
	def __init__(self):
		self.width=10
		self.height=10
	def area(self):
		return self.width * self.height
	def parimeter(self):
		return self.width * 2 + self.height *2
	def setSize(self,width,height):
		self.width = width
		self.height = height
r=rectangle()
r.setSize(20,20)
print(r.area())
print(r.parimeter())


class Vehicle: #Vehicle 와 car,Truck
	def __init__(self, name):
		self.name = name
	def drive(self):
		raise NotImplementedError("이것은추상메소드입니다. ")
	def stop(self):
		raise NotImplementedError("이것은추상메소드입니다. ")

class Car(Vehicle):
	def drive(self): 
		return '승용자를운전합니다. '
	def stop(self):
		return '승용자를정지합니다. '

class Truck(Vehicle):
	def drive(self):
		return '트럭을운전합니다. '
	def stop(self):
		return '트럭을정지합니다. '

cars = [Truck('truck1'), Truck('truck2'),  Car('car1')]

for car in cars:
   print(car.name + ': ' + car.drive())