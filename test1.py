from expModel import *
from obsTest import *
m = Model()
m.addNodes(2)
"""
print('Two nodes added')
print(m.nodeList)
print(m.val)
print(m.worldsNum)
print(m.rel)
print('--------------------------')
"""
m.deleteNode(0)
"""
print('Node 0 deleted')
print(m.nodeList)
print(m.val)
print(m.worldsNum)
print(m.rel)
print('--------------------------')
"""
m.addNode()
"""
print('Node added')
print(m.nodeList)
print(m.val)
print(m.worldsNum)
print(m.rel)
print('--------------------------')
"""
m.addAgent('B')
"""
print('Agent B added')
print(m.nodeList)
print(m.val)
print(m.worldsNum)
print(m.rel)
print('--------------------------')
"""
