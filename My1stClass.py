class My1stClass:
	def __init__(self, arg1, arg2, arg3):
		#initializing arguments#
		self.arg1 = arg1
		self.arg2 = arg2
		self.arg3 = arg3

	def printerfunc(self):
		print('Two characters from ' + self.arg1 + ' series are:')
		print(self.arg2)
		print(self.arg3)

my1stObject = My1stClass('Mr. Robot', 'Elliot', 'Angela')
my1stObject.printerfunc()

my2ndObject = My1stClass('Startrek', 'Captain Kirk', 'Dr. Spock')
my2ndObject.printerfunc()

class MyDerivedClass(My1stClass):

	def printerfunc(self):
		print('In ' + self.arg1 + ' Series ' + self.arg2 + ' is ' + self.arg3 + 
			 ' brother.')

	def psychprofile(self):
		print (self.arg2 + ' has an antisocial personality.')

my1stDerivedObject = MyDerivedClass('Mr. Robot', 'Elliot', 'Darlene')
my1stDerivedObject.printerfunc()
my1stDerivedObject.psychprofile()