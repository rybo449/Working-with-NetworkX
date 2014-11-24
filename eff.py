import heapq as hq
import string
import time
import math
from collections import deque
inf = float('Inf')

def makeGraph(G):
	fo = open("karate.gml","r")
	line = fo.readline()	
	while line:
		ip = string.split(line)
		if ip[0] == "source":
			a = int(ip[1])
		elif ip[0] == "target":
			G[a][int(ip[1])] = 1
			G[int(ip[1])][a] = 1
		#print G
		line = fo.readline()

def dijkstra(G, s):
    n = len(G)
    Q = [(0, s)]

    d = [inf for i in range(n+1)]
    d[s]=0


    while len(Q)!=0:
        (cost, u) = hq.heappop(Q)

        for v in G[u]:
            if d[v] > d[u] + G[u][v]:
                d[v] = d[u] + G[u][v]
                hq.heappush(Q, (d[v], v))

    '''for i in xrange(n+1):
	if '''
    return d

def between(G):
	CB = [0 for i in xrange(len(G)+1)]
	for s in G.keys():
		S = []
		#P = [0 for i in xrange(len(G)+1)]
		P = [[] for i in xrange(len(G)+1)]		
		DT = [0 for i in xrange(len(G)+1)]
		DT[s] = 1
		#dT = [-1 for i in xrange(len(G)+1)]
		#dT[s] = 0
		D ={}
		D[s] = 0
		Q = deque()
		Q.append(s)
		while len(Q) != 0:
			v = Q.popleft()
			S.append(v)
			for w in G[v].keys():
				if w not in D:
					Q.append(w)
					D[w] = D[v] + 1
				if D[w] == D[v] + 1:
					DT[w] = DT[w] + DT[v]
					P[w].append(v)
				#if dT[w]<0:
					#Q.append(w)
					#dT[w] = dT[v]+1
				#if dT[w] == dT[v] + 1:
					#DT[w] = DT[w] + DT[v]
					#P[w].append(v)
		delta = [0 for i in xrange(len(G)+1)]
		while len(S) != 0:
			w= S.pop()
			for v in P[w]:
				delta[v] = delta[v] + (DT[v]/float(DT[w]))*(1 + delta[w])
			if w != s:
				CB[w]+=delta[w]
		#print CB
	order = len(CB)
	if order <= 2:
		return CB
	scale = 1/float((order-1)*(order-2))
	for v in xrange(1,len(CB)):	
		CB[int(v)]= CB[int(v)]*scale
	return CB

def main():
	
	t1 = time.time()
	fo = open("karate.gml","r")
	line = fo.readline()
	max_a = 0
	while line:
		ip = string.split(line)
		if ip[0] == "id":
			a = int(ip[1])
			max_a = max(a, max_a)
		line = fo.readline()
	fo.close()
	#print max_a
	#create an adjacency list in a dictionary

	G = {i:{} for i in xrange(1,max_a+1)}
	makeGraph(G)
	G1 = {i:{} for i in xrange(1,max_a+1)}
	makeGraph(G1)
	
	#Run for the diameter of the graph
	d = 0
	d_max = 0
	close_sum = []
	for a in xrange(1,max_a):
		d =  dijkstra(G, a)
		for i in xrange(len(d)):
			if d[i] == inf:
				d[i] = 0
		close_sum.append(sum(d))
		d_max =max(d_max, d)
		#print max(d_max)
	print
	print
	print "\t\t    Diameter of the Graph =",max(d_max)
	print
	print
	max_degree = 0
	sum_degree = 0
	#Computing the Centrality measures
	for i in xrange(1,len(G)+1):
		max_degree = max(max_degree, len(G[i]))
		sum_degree+=len(G[i])
	avg_degree = sum_degree/float(max_a)
	SD = 0
	CD = 0
	for i in xrange(1, len(G) + 1):
		SD+=(max_degree - len(G[i]))
		if len(G[i])>avg_degree:
			CD+=(len(G[i])-avg_degree)
		else:
			CD+=(avg_degree-len(G[i]))
	CDG = CD/float(SD)
	print "\t\t\t  max_degree =", max_degree
	print
	print
	print "\t\t     Average Degree =", sum_degree/float(len(G))
	print
	print
	print "\t       Average Degree Centrality =",CDG
	print
	print
	#Closeness Centrality
	Deg = []
	for i in G:
		Deg.append([len(G[i]),i])
	Deg.sort(key=lambda x: x[0])
	bet = []
	BET=between(G)
	for i in xrange(1,len(BET)):
		bet.append([BET[i],i])
	bet.sort(key=lambda x: x[0])
	#print Deg
	Csum = 1
	Close = []
	countG1 = 0
	while Csum!=0 and len(G1)>0:
		C = []
		#print G1
		for i in xrange(len(G1)-1):
			l = close_sum[i]/float(len(G1))
			if l != 0:
				C.append(1/float(l))
		Csum = sum(C)/float(len(G1))
		Close.append(Csum)
		#print Csum,(countG1*100/float(len(G)))
		temp,name = bet.pop()
		del G1[name]
		countG1+=1
		for i in G1.keys():
			for j in G1[i].keys():
				if j==temp:
					del G1[i][j]

				
		
	#print "\t\t   Closeness Centrality =",Close
	#print
	#print
	#Clustering Coefficients
	s = 0
	count = 0
	for i in G.keys():
		for k in G[i].keys():
			l = G[k].keys()
			l1 = G[i].keys()
			count += len(list(set(l) & set(l1)))
			#print l1
			#print l
				
	print "\t\t    The Number of Triangles =",count
	print
	print	
	l = len(G)
	cluster = count*3/float(l*(l-1)*(l-2)/float(6))
	print "\t\t The clustering Coefficient =", cluster
	print
	print
	#Assortativity
	assort = 0
	uv1 = 0
	for i in G.keys():
		for j in G[i].keys():
			assort+=(1-(len(G[i])*len(G[j])/float(sum_degree)))
			homophily = (len(G[i])*len(G[j])/float(sum_degree))
	Q = assort
	Qmax = sum_degree - homophily
	mod = Q/float(Qmax)
	print "\t\t   Modularity Value =",mod
	print
	print
	
	#Power Laws and Calculating alpha
	k_min = inf
	max_D = 0

	for i in G.keys():
		k_min = min(k_min, len(G[i]))
		max_D = max(max_D, len(G[i]))
	if k_min == 0:
		k_min+=1
	pk_rank = []
	sorted_degree_count = []
	for i in xrange(1,len(G)+1):
		sorted_degree_count.append(len(G[i]))
	sorted_degree_count.sort()

	for i in G.keys():
		pk_rank.append(len(G[i])/float(len(G)))
	pk_rank.sort()

	dx1 = 0
	L = len(G)
	pk_max_check = 1000
	alpha_max = 1
	k_max_check = 1
	#print sorted_degree_count
	for i in xrange(k_min,max_D):
		select_E = 0
		X = True
		I = 0
		while X:
			if sorted_degree_count[I]<k_min:
				select_E+=1
			else:
				X = False
			I+=1
		if select_E >= len(G)-1:
			break
		dx1 = 0
		for i in xrange(select_E,len(G)-1):
			dx = sorted_degree_count[int(i)]
			if dx>0:
				dx = dx/float(k_min - (1/float(2)))
				dxt = math.log(dx)
				dx1+=dxt	
		alpha = (len(G) - select_E)/float(dx1)
		alpha+=1 
		C = 0
		#print alpha
		for i in xrange(1, 50):
			C1 = float(pow(i, -alpha))
			C+=C1
		sum_pk = 0
		pk_check = 0
		#print "C = ",C
		#print "alpha =",alpha
		for k in xrange(select_E, len(G)-1):
			pk=pow(sorted_degree_count[k], -alpha)/float(C)

			if pk>pk_rank[k]:
				pk_check+=(pk-pk_rank[k])
			else:
				pk_check+=(pk_rank[k]-pk)

			if pk_check<pk_max_check:
				pk_max_check = pk_check
				alpha_max = alpha
				k_max_check = k_min
			sum_pk+=pk
		k_min+=1
	print "\t\t      Value of alpha =",alpha_max
	print
	print
	sum_pk = 0
	for k in xrange(k_max_check, max_D + 1):
		pk = pow(k, -alpha_max)/float(C)
		print "\t\t\tP",k," =",pk
		sum_pk+=pk
	print
	print
	#Betweenness Centrality
	BET=between(G)
	bet1 = []
	Z = (len(G)*(len(G)-1))/float(2)
	for v in BET:
		bet1.append(v/float(Z))
	#for i in xrange(1,len(BET)):
		#print "\t\tBetweenness of node", i," =",BET[i]
	print "\t\tAverage Betweenness =",sum(BET)/float(len(G))
	print
	print
	t2 = time.time()
	print "\t\tTime taken to compute =",t2-t1
main()
