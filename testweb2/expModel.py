import copy
from copy import deepcopy
import numpy as np
import math
from itertools import chain, combinations
from graph_tool.all import *
from obsExp import *
from modalLogic import *
import modalLogic

class Model:
	def __init__(self):
		self.nodeList = []
		self.val = dict()
		self.worldsNum = 0
		self.propList = []
		self.agentList = ['A']
		self.rel = dict()
		self.rel[self.agentList[0]] = np.zeros((1,1))
		
		self.sigma = []
		self.expectations = dict()
		
		self.g = Graph(directed=False)

	def addNode(self):
		self.nodeList.append(self.worldsNum)
		self.val[self.worldsNum] = []
		self.expectations[self.worldsNum] = 0
		if self.worldsNum == 0:
			for i in self.rel.keys():
				self.rel[i][0][0] = 1
		else:
			addBot = np.zeros((1,len(self.nodeList)-1))
			addSide = np.zeros((1,len(self.nodeList))).T
			for i in self.rel.keys():
				self.rel[i] = np.concatenate((self.rel[i],addBot), axis=0)
				self.rel[i] = np.concatenate((self.rel[i],addSide), axis=1)
				self.rel[i][len(self.nodeList)-1][len(self.nodeList)-1] = 1
		self.worldsNum = self.worldsNum + 1

	def addNodes(self, num):
		for i in range(num):
			self.addNode()
			
	def addAgent(self, agent):
		self.agentList.append(agent)
		#nodes = len(self.nodeList)
		self.rel[agent] = np.zeros((len(self.nodeList), len(self.nodeList)))
		matrix = self.rel[agent]
		for i in range(len(self.nodeList)):
			matrix[i][i] = 1
			
	def deleteNode(self, node):
		if node in self.nodeList:
			index = self.nodeList.index(node)
			for i in self.rel.keys():
				self.rel[i] = np.delete(self.rel[i], (index), axis=0)
				self.rel[i] = np.delete(self.rel[i], (index), axis=1)
			self.nodeList.remove(node)
			del self.val[node]
			del self.expectations[node]
		else:
			print("That node doesn't exist!")
			
	def addEdge(self, u, v, agent):
		if u in self.nodeList and v in self.nodeList and agent in self.agentList:
			indexU = self.nodeList.index(u)
			indexV = self.nodeList.index(v)
			self.rel[agent][indexV][indexU] = 1
			self.rel[agent][indexU][indexV] = 1

	def addProp(self, node, prop):
		if type(prop) == Atom:
			if node in self.nodeList:
				self.val[node].append(prop)
			if prop not in self.propList:
				self.propList.append(prop)
		else:
			print('This is not an atomic proposition!')
		
		
	def addPropToAll(self, prop):
		if type(prop) == Atom:
			for i in self.nodeList:
				self.addProp(i, prop)
		else:
			print('This is not an atomic proposition!')

	def transitiveClosure(self):
		for agent in self.agentList:
			for k in range(len(self.nodeList)):
				for i in range(len(self.nodeList)):
		         		for j in range(len(self.nodeList)):
		         			self.rel[agent][i][j] = self.rel[agent][i][j] or (self.rel[agent][i][k] and self.rel[agent][k][j])

	#define \sigma of alphabets for regex
	def buildLang(self, *argv):
		for arg in argv:
			self.sigma.append(arg)

	def addObservation(self, node, obs):
		self.expectations[node] = obs
	#Are we allowing only one observation expression per world?

	def v(self, formula, world):
		if type(formula) == Atom:
			return formula in self.val[world]
		elif type(formula) == Not:
			return not self.v(formula.child,world)
		elif type(formula) == Or:
			return any(self.v(child, world) for child in formula.children)
		elif type(formula) == And:
			return all(self.v(child, world) for child in formula.children)
		elif type(formula) == Imp:
			return not self.v(formula.leftChild,world) or self.v(formula.rightChild,world)
		elif type(formula) == Iff:
			return self.v(formula.leftChild,world) is self.v(formula.rightChild,world)
		elif type(formula) == modalLogic.K:
			nodes = []
			for i in range(len(self.nodeList)):
				if self.rel[formula.agent][self.nodeList.index(world)][i] == 1:
					nodes.append(self.nodeList[i])
#			print("All worlds reachable from", world," by agent", formula.agent, ": ", nodes)
			return all(self.v(formula.child, k) for k in nodes)
		elif type(formula) == modalLogic.M:
			nodes = []
			for i in range(len(self.nodeList)):
				if self.rel[formula.agent][self.nodeList.index(world)][i] == 1:
					nodes.append(self.nodeList[i])
#			print("All worlds reachable from", world," by agent", formula.agent, ": ", nodes)
			return any(self.v(formula.child, k) for k in nodes)
#What happens when
#a. world vanishes upon updating
#b. all worlds vanish upon updating
		elif type(formula) == O:
			self.updateModel(formula.observation)
			if world in self.nodeList:
				return self.v(formula.child, world)
			else:
				return True
				print('The observation does not hold true for any of the worlds in the model, and so the expression evaluates to True by default!')
			
	def updateModel(self, expression):
		updatedList = []
		for i in self.nodeList:
			expectation = self.expectations[i]
			language = makeObservation(expectation, expression).L()
			if language:
				updatedList.append(i)
		if updatedList:
			for i in self.nodeList:
				if i not in updatedList:
					self.deleteNode(i)
				else:
					self.expectations[i] = makeObservation(self.expectations[i], expression)
			return True
			print('The model was updated successfully!')
		else:
			return False
			print('This updated model does not exist!')
		self.nodeList = updatedList

	def draw(self, fileName):
		graphNode = dict()	#graphNode is a dict with node number for keys and Vertex object for values
		for i in self.nodeList:	
			graphNode[i] = self.g.add_vertex()
		edgeList = []		#edgeList is the minimal edge list without any agent references --- does not contain reflexive edges, and only represents those edges which convey the link between any two different nodes
		for i in range(len(self.nodeList)):
			for j in range(len(self.nodeList)):
				if i != j and (i,j) not in edgeList and (j,i) not in edgeList:
					if any(self.rel[agent][i][j] == 1 for agent in self.agentList):
						edgeList.append((i,j))
		edges = dict()		#edges is a dict with elements for edgeList for keys and the agents on that edge for values
		for i in edgeList:
			self.g.add_edge(graphNode[i[0]],graphNode[i[1]])
			edges[i] = []
			for agent in self.agentList:
				if self.rel[agent][i[0]][i[1]] == 1 :
					edges[i].append(agent)
		#Generate vertex property for valuation and expectation
		nodeProps = self.g.new_vertex_property("string")
		for i in graphNode.keys():
			props = ''
			valuation = self.val[i]
			expectation = self.expectations[i]
			if valuation:		#if valuation exists
				for prop in valuation:
					if valuation.index(prop) == 0 and len(valuation) != 1:
						props = str(i)
						props = props+' : '
						props = props+str(prop)
						props = props+', '
					elif valuation.index(prop) == 0 and len(valuation) == 1:
						props = props+str(i)
						props = props+' : '
						props = props+str(prop)
					elif valuation.index(prop) == (len(valuation)-1):
						props = props+str(prop)
					else:
						props = props+str(prop)
						props = props+', '
				if expectation != 0:
					props = props+' : '
					props = props+str(expectation)
				else:
					props = props+' : '
			else:
				props = str(i) + ' : '
				if expectation != 0:
					props = props+' : '
					props = props+str(expectation)
				else:
					props = props+' : '
			nodeProps[graphNode[i]] = props
		self.g.vertex_properties["nodePropositions"] = nodeProps
		#Generate edge property for relation
		edgeAgents = self.g.new_edge_property("string")
		for i in edgeList:
			source = i[0]
			target = i[1]
			edgeAgents[self.g.edge(source, target)] = ', '.join(edges[i])
		self.g.edge_properties["edgeAgent"] = edgeAgents
		target = "./public/imgs/" + str(fileName) + ".png"
		graph_draw(self.g, vertex_text=self.g.vertex_properties["nodePropositions"], edge_text=self.g.edge_properties["edgeAgent"], vertex_font_size=18, edge_font_size=25, edge_pen_width=2.75, edge_text_distance=8.5, output_size=(1000, 1000), output=target)
	
	#TODO -- give test cases and check for robustness
	#TODO -- give complexity of model checking

