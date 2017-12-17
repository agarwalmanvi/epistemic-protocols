import sys
from obsExp import *
from modalLogic import *
from expModel import *

nodesNum = int(sys.argv[1])
propsNum = int(sys.argv[2])
target = str(sys.argv[3]) + str(sys.argv[4])
m = Model()
m.addNodes(nodesNum)
propsdict = dict()
for i in range(propsNum):
	temp = 'p'+str(i)
	propsdict[i] = Atom(temp)
	m.propList.append(propsdict[i])
m.draw(target)
