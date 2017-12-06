from obsExp import *
delta = Delta()
eps = Epsilon()
a = Alphabet('a')
b = Alphabet('b')
pi = Plus(a,b)	#a+b
pi2 = Dot(a,b)	#a.b
pi3 = Dot(pi2,pi)	#a.b.(a+b)

"""
exp = Dot(eps,a)
print(str(exp))
print(exp.L())
exp1 = Plus(eps,a)
print(str(exp1))
print(exp1.L())
exp2 = Dot(delta,a)
print(str(exp2))
print(exp2.L())
exp3 = Plus(delta,a)
print(str(exp3))
print(exp3.L())
exp4 = Dot(a,delta)
print(str(exp4))
print(exp4.L())
"""
