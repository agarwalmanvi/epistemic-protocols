import sys
from obsExp import *
from modalLogic import *
from expModel import *

nodesNum = int(sys.argv[1])
propsNum = int(sys.argv[2])
temp = list(str(sys.argv[3]))
reltemp = list(str(sys.argv[4]))
target = str(sys.argv[5]) + str(sys.argv[6])
val = []
for letter in temp:
	val.append(int(letter))
m = Model()
m.addNodes(nodesNum)
propsdict = dict()
for i in range(propsNum):
	temp = 'p'+str(i)
	propsdict[i] = Atom(temp)
	m.propList.append(propsdict[i])
for node in range(nodesNum):
	startPos = propsNum*node
	endPos = propsNum*(node+1)
	l = val[startPos:endPos]
	for ind in range(len(l)):
		if l[ind] == 1:
			m.addProp(node,m.propList[ind])


