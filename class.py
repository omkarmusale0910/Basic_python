
class Dog:

	# Class Variable
	animal = 'dog'

	# The init method or constructor
	def __init__(self, breed):
		# Instance Variable
		self.breed = breed
	

	# Adds an instance variable
	def setColor(self, color):
		self.color = color

	# Retrieves instance variable
	def getColor(self):
		return self.color


# Driver Code
Rodger = Dog("pug")
Rodger.setColor("brown")
print(Rodger.color)



class GFG:
	def __init__(self, name, company):
		self.name = name
		self.company = company

	def __str__(self):
		return f"My name is {self.name} and I work in {self.company}."


my_obj = GFG("John", "GeeksForGeeks")
print(my_obj)
