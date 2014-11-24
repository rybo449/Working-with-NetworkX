import networkx as nx
import matplotlib.pyplot as plt
import string
import math
import random

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
	'''G = nx.Graph()
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

	avg = []
	x = 1
	a = []
	y = []
	b = []
	x1 = []
	for i in G:
		b.append([G.degree(i),i])
	b.sort(key = lambda x: x[0])
	
	length = len(G)
	print len(G)
	while len(G1)>0:

		H = nx.connected_components(G1)
		cCentral = sum(nx.closeness_centrality(G1,normalized = True))
		print "H[0] = ",len(H[0]), " and closeness = ",(cCentral/float(length*length))
		a.append(len(H[0])*(cCentral)/float(length*length*length))
	
		y.append(x/float(length))

		x1 = b.pop()
		G1.remove_node(x1[1])

		x+=1


	
	plt.plot(y,a,"bo")'''


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

	avg = []
	x = 1
	a = []
	y = []
	b = []
	for i in G:
		b.append(i)
	x1 = []
	
	length = len(G)
	print len(G)
	while len(G1)>0:

		H = nx.connected_components(G1)

		cClose = sum(nx.closeness_centrality(G1,normalized = True))
		print "H[0] = ",len(H[0]), " and closeness = ",(cClose)/float(length*length)
		a.append(len(H[0])*(cClose)/float(length*length*length))
	
		y.append(x/float(length))

		x1 = random.choice(b)
		b.remove(x1)
		G1.remove_node(x1)

		x+=1


	
	plt.plot(y,a,"g^")


	'''G = nx.Graph()
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
	G2 = dict(G.nodes(data = True))

	print len(G1)
	x = 1
	a = []
	y = []
	b = []
	x1 = []
	b1 = nx.betweenness_centrality(G)
	print b1
	for i in b1:
		b.append([b1[i],i])
	b.sort(key = lambda x: x[0])


	length = len(G)
	print len(G)
	while len(G1)>0:

		H = nx.connected_components(G1)
		cClose = sum(nx.closeness_centrality(G1,normalized = True))
		print "H[0] = ",len(H[0]), " and closeness = ",(cClose)/float(length*length)
		a.append(len(H[0])*(cClose)/float(length*length*length))
		
		y.append(x/float(length))

		x1 = b.pop()
		G1.remove_node(x1[1])

		x+=1
	plt.plot(y,a,"bo")'''
	
	'''G = nx.Graph()
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
	G2 = dict(G.nodes(data = True))

	print len(G1)
	x = 1
	a = []
	y = []
	b = []
	x1 = []
	for i in G:
		b.append([G.degree(i),i])
	b.sort(key = lambda x: x[0])


	length = len(G)
	print len(G)
	while len(G1)>0:

		H = nx.connected_components(G1)

		cClose = sum(nx.closeness_centrality(G1,normalized = True))
		print "H[0] = ",len(H[0]), " and closeness = ",(cClose)/float(length*length)
		a.append(len(H[0])*(cClose)/float(length*length*length))
		y.append(x/float(length))

		x1 = b.pop()
		G1.remove_node(x1[1])
		b = []
		for i in G1:
			b.append([G.degree(i),i])
		b.sort(key = lambda x: x[0])
		x+=1
	plt.plot(y,a,"bo")'''
	
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
	G2 = dict(G.nodes(data = True))

	print len(G1)
	x = 1
	a = []
	y = []
	b = []
	x1 = []
	b1 = nx.betweenness_centrality(G)
	#print b1
	for i in G:
		b.append([b1[i],i])
	b.sort(key = lambda x: x[0])


	length = len(G)
	print len(G)
	while len(G1)>0:

		H = nx.connected_components(G1)

		cClose = sum(nx.closeness_centrality(G1,normalized = True))
		print "H[0] = ",len(H[0]), " and closeness = ",(cClose)/float(length*length)
		a.append(len(H[0])*(cClose)/float(length*length*length))
		
		y.append(x/float(length))

		x1 = b.pop()
		print x1
		G1.remove_node(x1[1])
		b1 = nx.betweenness_centrality(G1)
		print b1
		b = []
		for i in G1:
			b.append([b1[i],i])
		b.sort(key = lambda x: x[0])
		x+=1
	plt.plot(y,a,"ro")

	plt.title("Efficiency plot of the Email-Network through targetted and random attacks")
	plt.ylabel("Size of Giant Component * Avg. Closeness Centrality")
	plt.xlabel("Fraction of Nodes Removed")

	plt.show()
main()
