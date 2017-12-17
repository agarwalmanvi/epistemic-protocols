from obsExp import *
from expModel import *
from modalLogic import *

	
a = AlphabetObs('a')
b = AlphabetObs('b')
c = AlphabetObs('c')
p = Atom('p')
q = Atom('q')
m = Model()
m.addNodes(2)
m.addAgent('B')
m.addEdge(0,1,'A')
m.addEdge(0,1,'B')
m.addProp(0,p)
m.addObservation(0,a)
m.addObservation(1,b)

f1 = O(a, p)
f2 = O(b, p)



"""
f1 = Not(K('A',p))
f2 = Not(K('B',p))
f3 = K('A',Not(K('B',p)))
"""
"""
f1 = And(p,q)
f2 = Or(p,q)
f3 = Imp(p,p)
f4 = Imp(q,p)
f5 = Imp(p,q)
"""

"""
c = AlphabetObs('c')
r = AlphabetObs('r')
i = AlphabetObs('i')
t = AlphabetObs('t')

w = DotObs(r,a,b)
pi = DotObs(r,a,b,b,i,t)
pi2 = PlusObs(DotObs(r,a,t),DotObs(r,a,b,b,i,t))
"""
"""
exp1 = makeObservation(deltaObs,deltaObs)
exp2 = makeObservation(deltaObs,epsilonObs)
exp3 = makeObservation(deltaObs, a)
exp4 = makeObservation(epsilonObs,deltaObs)
exp5 = makeObservation(epsilonObs,epsilonObs)
exp6 = makeObservation(epsilonObs,a)
"""
"""
exp1 = makeObservation(a, deltaObs)
exp2 = makeObservation(a,epsilonObs)
exp3 = makeObservation(a,a)
exp4 = makeObservation(a,b)
"""
"""
exp1 = makeObservation(DotObs(a,b),deltaObs)
exp2 = makeObservation(DotObs(a,b),epsilonObs)
exp3 = makeObservation(PlusObs(a,b),deltaObs)
exp4 = makeObservation(PlusObs(a,b),epsilonObs)
"""
"""
exp1 = makeObservation(deltaObs,DotObs(a,b))
exp2 = makeObservation(deltaObs,DotObs(PlusObs(a,b),c))
exp3 = makeObservation(deltaObs,PlusObs(a,b))
exp4 = makeObservation(deltaObs,PlusObs(DotObs(a,b),c))
"""
"""
exp1 = makeObservation(epsilonObs,DotObs(a,b))
exp2 = makeObservation(epsilonObs,DotObs(PlusObs(a,b),c))
exp3 = makeObservation(epsilonObs,PlusObs(a,b))
exp4 = makeObservation(epsilonObs,PlusObs(DotObs(a,b),c))
"""
"""
exp1 = makeObservation(a,DotObs(a,b))
exp2 = makeObservation(a,DotObs(PlusObs(a,b),c))
exp3 = makeObservation(a,PlusObs(a,b))
exp4 = makeObservation(a,PlusObs(DotObs(a,b),c))
"""
"""
exp1 = makeObservation(PlusObs(a,b),a)
exp2 = makeObservation(PlusObs(DotObs(a,c),DotObs(a,b)),a)
"""
"""
exp1 = makeObservation(PlusObs(a,b),DotObs(a,b,c))
exp2 = makeObservation(PlusObs(a,b),DotObs(PlusObs(a,b),c))
exp3 = makeObservation(PlusObs(DotObs(a,c),DotObs(a,b)),DotObs(a,b,c))
exp4 = makeObservation(PlusObs(DotObs(a,c),DotObs(a,b)),DotObs(a,b))
"""

"""

exp1 = epsilonObs
exp2 = deltaObs
exp3 = a
exp4 = DotObs(a,b)
exp5 = PlusObs(DotObs(a,b), epsilonObs, deltaObs, c, DotObs(a,b))
exp6 = DotObs(a,b,epsilonObs,deltaObs,c,a,b)
exp7 = DotObs(epsilonObs,epsilonObs,epsilonObs,epsilonObs,c,epsilonObs,epsilonObs,epsilonObs,a,b)
exp8 = PlusObs(deltaObs,deltaObs,c,epsilonObs,deltaObs,DotObs(a,b))
exp9 = PlusObs(DotObs(deltaObs,a,b),DotObs(epsilonObs,c), DotObs(a,b), deltaObs)
exp10 = DotObs(a,b,c,PlusObs(DotObs(c, epsilonObs),deltaObs),PlusObs(DotObs(deltaObs,a),DotObs(epsilonObs,b)))
"""				
