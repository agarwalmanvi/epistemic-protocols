import itertools
from collections import *

class obsExp:
	def __dotObs__(self):
		return DotObs(self)
	def __plusObs__(self):
		return PlusObs(self)

class DeltaObs(obsExp):
	op = ""
	def __init__(self):
		self.name = u"\u03B4"
	def __hash__(self):
		return hash(str(self))
	def __str__(self):
		return self.name
	__repr__ = __str__
	#.L() returns a (set of) strings
	def L(self):
		return set()
		
deltaObs = DeltaObs()

class EpsilonObs(obsExp):
	op = ""
	def __init__(self):
		self.name = u"\u0190"
	def __hash__(self):
		return hash(str(self))
	def __str__(self):
		return self.name
	__repr__ = __str__
	def L(self):
		return {""}

epsilonObs = EpsilonObs()
	
class AlphabetObs(obsExp):
	op = ""
	def __init__(self, name):
		self.name = name
	def __hash__(self):
		return hash(str(self))
	def __str__(self):
		return self.name
	__repr__ = __str__
	def L(self):
		return {str(self)}

class NaryOpObs(obsExp):
	def __init__(self, firstChild, *args):
		self.children = []
		self.children.append(firstChild)
		for arg in args:
			self.children.append(arg)
	def __str__(self):
		tempStr = '('
		for i in range(len(self.children)):
			if i!=(len(self.children)-1):
				tempStr = tempStr + str(self.children[i]) + self.op
			else:
				tempStr = tempStr + str(self.children[i])
		tempStr = tempStr + ')'
		return tempStr
	def __hash__(self):
		return hash(str(self))

class DotObs(NaryOpObs):
	op = "."
	def L(self):
		x = []
		for i in self.children:
			x.append(i.L())
		temp = [p for p in itertools.product(*x)]
		x = []
		for i in temp:
			x.append(''.join(i))
		return set(x)
			
class PlusObs(NaryOpObs):
	op = "+"
	def L(self):
		temp = set()
		for i in self.children:
			temp = temp.union(i.L())
		return temp



#########################SUPPORTER FUNCTIONS#############################################################


#tests for equality of two regex expressions --- return boolean
def eq(exp1,exp2):
	return exp1.L() == exp2.L() and type(exp1) == type(exp2)

#helper function for makeObservation --- returns obsExp
def output(expression):
	if type(expression) == EpsilonObs:
		return epsilonObs
	if type(expression) == DeltaObs or type(expression) == AlphabetObs:
		return deltaObs
	if type(expression) == PlusObs:
		outputs = []
		for i in expression.children:
			outputs.append(output(i))
		return PlusObs(*outputs)
	if type(expression) == DotObs:
		outputs = []
		for i in expression.children:
			outputs.append(output(i))
		return DotObs(*outputs)
		
#tests if w \in init(pi) --- returns boolean
def isInit(searchString, pi):	
	lang = list(pi.L())
	truthCounter = []
	comparedStrings = []
	for i in lang:
		if searchString in i:
			for index in range(len(searchString)):
				if searchString[index] == i[index]:
					truthCounter.append(True)
				else:
					truthCounter.append(False)
			if False in truthCounter:
				comparedStrings.append([])
			else:
				comparedStrings.append(i[len(searchString):])
		else:
			comparedStrings.append([])
	return comparedStrings[0], not all(x==[] for x in comparedStrings)

#.makeObservation returns an unsimplified regex --- returns obsExp
#use str() to get string representation of the unsimplified regex -- use .L() to get set of strings corresponding to this regex
def makeObservation(pi, w):
	if len(w) != 1:
		l = list(w)
		for i in l:
			if l.index(i) == 0:
				temp = makeObservation(pi, i)
			else:
				temp = makeObservation(temp, i)
		return temp
	if type(pi) == DeltaObs:
		return deltaObs
	elif type(pi) == EpsilonObs:
		return epsilonObs
	elif type(pi) == AlphabetObs:
		if str(pi) == w:
			return epsilonObs
		else:
			return deltaObs
	elif type(pi) == DotObs:
		return False
		#TODO finish this part in the general case of n arguments
	elif type(pi) == PlusObs:
		l = []
		for i in pi.children:
			l.append(makeObservation(i,w))
		return PlusObs(*l)
			
#TODO round 2 for testing
def simplify(expression):
	if type(expression) == PlusObs:
		#remove all duplicate children
		hashList = []
		for i in expression.children:
			hashList.append(hash(i))
		hashList = list(set(hashList))
		newChildren = []
		for i in expression.children:
			if hash(i) in hashList:
				newChildren.append(i)
				hashList.remove(hash(i))
		#if all children are epsilon, or all children are either epsilon or delta, then only return epsilon 
		if all(x==epsilonObs for x in newChildren) or all(x==epsilonObs or x==deltaObs for x in newChildren):
			return epsilonObs
		#if all children are delta then return only delta
		elif all(x==deltaObs for x in newChildren):
			return deltaObs
		#if newChildren list contains something apart from delta or epsilon
		else:
			#if the newChildren list contains delta
			if deltaObs in newChildren:
				l = list(filter((deltaObs).__ne__, newChildren))
				new = []
				for i in l:
					new.append(simplify(i))
				if deltaObs in new:
					l = list(filter((deltaObs).__ne__, new))
				return PlusObs(*l)
			#if newChildren list does not contain delta
			else:
				new = []
				for i in newChildren:
					new.append(simplify(i))
				return PlusObs(*new)
	elif type(expression) == DotObs:
		#no filtering of children can take place since this uses concatenation
		#if any child is delta return delta
		if deltaObs in expression.children:
			return deltaObs
		#if all children are epsilon, return epsilon
		elif all(x==epsilonObs for x in expression.children) == True:
			return epsilonObs
		else:	
			#if epsilon is in children, eliminate it
			if epsilonObs in expression.children:
				l = list(filter((epsilonObs).__ne__, expression.children))
				new = []
				for i in l:
					new.append(simplify(i))
				return DotObs(*new)
			#if children does not contain epsilon
			else:
				new = []
				for i in expression.children:
					print(str(simplify(i)))
					new.append(simplify(i))
				return DotObs(*new)
	else:
		return expression
		

	
#TODO seperate out protocol expressions and observation expressions -- PARTIALLY DONE


a = AlphabetObs('a')
b = AlphabetObs('b')
