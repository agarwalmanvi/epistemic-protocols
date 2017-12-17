import sys
from obsExp import *
from modalLogic import *
from expModel import *

nodesNum = int(sys.argv[1])
propsNum = int(sys.argv[2])
temp = list(str(sys.argv[3]))
reltemp = list(str(sys.argv[4]))
worldToCheck = int(sys.argv[5])
formulaToCheck = str(sys.argv[6])
val = []
rel = []
for letter in temp:
	val.append(int(letter))
m = Model()
agent = m.agentList[0]
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
for letter in reltemp:
	rel.append(int(letter))
for nodeU in range(nodesNum):
	startPos = nodeU*nodesNum
	endPos = (nodeU+1)*nodesNum
	l = rel[startPos:endPos]
	for ind in range(len(l)):
		if l[ind] == 1:
			m.addEdge(nodeU, ind, agent)

