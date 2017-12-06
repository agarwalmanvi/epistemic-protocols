import copy
from copy import deepcopy
import numpy as np
import math
from pyeda.inter import *
import pyeda
from itertools import chain, combinations
#from graph_tool.all import *
from obsExp import *

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
		self.observations = dict()

	def addNode(self):
		self.nodeList.append(self.worldsNum)
		self.val[self.worldsNum] = []
		self.observations[self.worldsNum] = 0
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
			del self.observations[node]
		else:
			print("That node doesn't exist!")
			
	def addEdge(self, u, v, agent):
		if u in self.nodeList and v in self.nodeList and agent in self.agentList:
			indexU = self.nodeList.index(u)
			indexV = self.nodeList.index(v)
			self.rel[agent][indexV][indexU] = 1
			self.rel[agent][indexU][indexV] = 1

	def addProp(self, node, prop):
		if node in self.nodeList:
			self.val[node].append(prop)
		if prop not in self.propList:
			self.propList.append(prop)
		
		
	def addPropToAll(self, prop):
		for i in self.nodeList:
			self.addProp(i, prop)

	def transitiveClosure(self):
		for agent in self.agentList:
			for k in range(len(self.nodeList)):
				for i in range(len(self.nodeList)):
		         		for j in range(len(self.nodeList)):
		         			self.rel[agent][i][j] = self.rel[agent][i][j] or (self.rel[agent][i][k] and self.rel[agent][k][j])

	def buildLang(self, *argv):
		for arg in argv:
			self.sigma.append(arg)

	def addObservation(self, obs, node):
		self.observations[node] = obs
	#Are we allowing only one observation expression per world?

