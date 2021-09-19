# wapp to display id, marks, name, address of student using subclass & superclass
class person:
	def __init__(self, id, name, address):
		self.id = id
		self.name = name
		self.address = address
	def show(self):
		print("id = ", self.id)
		print("name = ", self.name)
		print("address = ", self.address)
class student(person):
	def __init__(self, id, name, address, marks):
		self.id = id
		self.name = name
		self.address = address
		self.marks = marks
	def show(self):
		print("id = ", self.id)
		print("name = ", self.name)
		print("address = ", self.address)
		print("marks = ", self.marks)
s = student(10, "amit", "thane", 90)
s.show()
		