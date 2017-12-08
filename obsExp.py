#.L() returns a (set of) string
#.makeObservation returns an unsimplified regex -- use str() to get string representation of the unsimplified regex -- use .L() to get set of strings corresponding to this regex

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
		return {str(self)}
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
				temp.add(i+j)
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
	if type(expression) == Delta or type(expression) == Alphabet:
		return delta
	if type(expression) == Plus:
		return Plus(output(expression.lchild),output(expression.rchild))
	if type(expression) == Dot:
		return Dot(output(expression.lchild),output(expression.rchild))
"""
def simplify(expression):
	if type(expression) == Dot:
		if type(expression.lchild) == Delta or type(expression.rchild) == Delta:
			return delta
		elif type(expression.lchild) == Epsilon:
			return simplify(expression.rchild)
		elif type(expression.rchild) == Epsilon:
			return simplify(expression.lchild)
	elif type(expression) == Plus:
		if type(expression.lchild) == Delta and type(expression.rchild) == Delta:
			return delta
		if type(expression.lchild) != Delta and type(expression.rchild) == Delta:
			return simplify(expression.lchild)
		if type(expression.lchild) == Delta and type(expression.rchild) != Delta:
			return simplify(expression.rchild)
		if type(expression.lchild) == Epsilon and type(expression.rchild) == Epsilon:
			return epsilon
		if str(expression.lchild) == str(expression.rchild):
			return simplify(expression.lchild)
	else:
		return expression
	
"""

a = Alphabet('a')
b = Alphabet('b')
exp1 = Dot(a,b)
exp2 = Dot(epsilon,delta)
exp3 = Dot(delta,a)
exp = Plus(Plus(exp1,exp2),exp3)
"""
exp1 = output(epsilon)
exp2 = output(delta)
exp3 = output(a)
exp4 = output(Dot(a,b))
exp5=output(Plus(a,b))

exp1 = Plus(a,delta).makeObservation(a)
exp2 = Plus(delta,a).makeObservation(a)
exp3 = Plus(delta,delta).makeObservation(a)
exp4 = Plus(epsilon,epsilon).makeObservation(a)
exp5 = Plus(delta,epsilon).makeObservation(a)
exp6 = Plus(epsilon, delta).makeObservation(a)
exp7 = Plus(epsilon, a).makeObservation(a)
exp8 = Plus(a, epsilon).makeObservation(a)
exp9 = Plus(a,b).makeObservation(a)
exp10 = Plus(b,a).makeObservation(a)

exp1 = Plus(a,delta)
exp2 = Plus(delta,a)
exp3 = Plus(a,epsilon)
exp4 = Plus(epsilon,a)

exp5 = Plus(a,b)
exp6 = Plus(b,a)

exp1 = Dot(a,b)
exp2 = Dot(Plus(a,b),Dot(a,b))
exp3 = Dot(Dot(a,a),Plus(a,b))
exp4 = Plus(Dot(Dot(a,b),a),Dot(b,b))
"""
