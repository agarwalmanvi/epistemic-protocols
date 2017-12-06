class obsExp:
	def __dot__(self):
		return Dot(self)
	def __plus__(self):
		return Plus(self, other)
	def __star__(self):
		return Star(self, other)

class Delta(obsExp):
	op = ""
	def __init__(self):
		self.name = u"\u03B4"
	def __hash__(self):
		return hash(self.name)
	def __str__(self):
		return self.name
	__repr__ = __str__
	def eq(self, other):
		return self.name == other.name
	def L(self):
		return set()
	def makeObservation(self, observation):
		return self
		
delta = Delta()

class Epsilon(obsExp):
	op = ""
	def __init__(self):
		self.name = u"\u0190"
	def __hash__(self):
		return hash(self.name)
	def __str__(self):
		return self.name
	__repr__ = __str__
	def eq(self, other):
		return self.name == other.name
	def L(self):
		return {""}
	def makeObservation(self, observation):
		return delta

epsilon = Epsilon()
	
class Alphabet(obsExp):
	op = ""
	def __init__(self, name):
		self.name = name
	def __hash__(self):
		return hash(self.name)
	def __str__(self):
		return self.name
	__repr__ = __str__
	def eq(self, other):
		return self.name == other.name
	def L(self):
		return {self}
	def makeObservation(self, observation):
		if str(self) != str(observation):
			return delta
		else:
			return epsilon
			

class BinOp(obsExp):
	def __init__(self, lchild, rchild):
		self.lchild = lchild
		self.rchild = rchild
	def __str__(self):
		return '(' + str(self.lchild) + self.op + str(self.rchild) + ')'

class Dot(BinOp):
	op = "."
	def L(self):
		temp = set()
		for i in self.lchild.L():
			for j in self.rchild.L():
				temp.add(str(i)+str(j))
		return temp
	def makeObservation(self, observation):
		return Plus(Dot(self.lchild.makeObservation(observation),self.rchild),Dot(output(self.lchild),self.rchild.makeObservation(observation)))

class Plus(BinOp):
	op = "+"
	def L(self):
		return self.lchild.L().union(self.rchild.L())
	def makeObservation(self, observation):
		return Plus(self.lchild.makeObservation(observation), self.rchild.makeObservation(observation))

def output(expression):
	if type(expression) == Epsilon:
		return epsilon
	if type(expression) == Delta:
		return delta
	if type(expression) == Alphabet:
		return delta
	if type(expression) == Plus:
		return Plus(output(expression.lchild),output(expression.rchild))
	if type(expression) == Dot:
		return Dot(output(expression.lchild),output(expression.rchild))

a = Alphabet('a')
b = Alphabet('b')
exp1 = Dot(a,b)
exp2 = Dot(Plus(a,b),Dot(a,b))
exp3 = Dot(Dot(a,a),Plus(a,b))
exp4 = Plus(Dot(Dot(a,b),a),Dot(b,b))
