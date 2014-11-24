import networkx as nx
import matplotlib.pyplot as plt
import string
import random
import math

def makeGraph(G):
	fo = open("email.txt","r")
	line = fo.readline()
	while line:
		ip = line.split()
		G.add_edge(int(ip[0]),int(ip[1]))
		G.add_edge(int(ip[1]),int(ip[0]))
		line = fo.readline()
	fo.close()

def main():
	G = nx.Graph()
	G1 = nx.Graph()
	fo = open("email.txt","r")
	line = fo.readline()
	max_a = 0
	a = 0
	while line:
		ip = line.split()
		if ip[0] != a:
			a = int(ip[1])
			G.add_node(a)
		line = fo.readline()
	fo.close()
	makeGraph(G)
	G1 = G
	Closelist = []
	x = 1
	y = []
	#sum1 = 0
	
	#sum1 = sum(G.degree().values())
	#print sum1
	#sum1 = sum1/float(len(G))
	#print sum1
	#cClose = nx.closeness_centrality(G,normalized = True)
	#for i in cClose:
	#	Closelist.append(cClose[i])
	#	y.append(x)
	#	x+=1
	'''Closelist.sort()
	plt.plot(y,Closelist,"g^")
	plt.xlabel("Number of Nodes")
	plt.ylabel("Closeness Centrality of each Node")
	plt.title("Closeness Centrality of Nodes in Zachary's Karate Club")
	plt.show()'''
	#print nx.diameter(G)
	print len(G)
	#print sum(Closelist)/float(len(G))
main()	
