import networkx as nx
import math
import csv
import random as rand
import sys
import operator
import matplotlib.pyplot as plt
import pandas as pd
_DEBUG_ = False

#########################
def set_all_B(G):
	for each in G.nodes():
		G.node[each]['action']='B'
def set_A(G,list1):
	for each in list1:
		G.node[each]['action']='A'
def get_colors(G):
	list1=[]
	for each in G.nodes():
		if G.node[each]['action']=='B':
			list1.append('red')
		else:
			list1.append('green')
	return list1
def find_neigh(each,c,G):
	num=0
	for each1 in G.neighbors(each):
		if G.node[each1]['action']==c:
			num=num+1
	return num
#list to store the count of influenced nodes
infl=[]
def recalculate_options(G):
	dict1={}
	#Payoff (A)=a=4
	#Payoff (B)=b=3
	a=20
	b=5
	for each in G.nodes():
		num_A=find_neigh(each,'A',G)
		num_B=find_neigh(each,'B',G)
		payoff_A=a*num_A
		payoff_B=b*num_B
		if payoff_A>=payoff_B:
			dict1[each]='A'
		else:
			dict1[each]='B'
	return dict1
def terminate_1(c,G):
	f=1
	for each in G.nodes():
		if G.node[each]['action']!=c:
			f=0
			break
	return f
def terminate(G,count):
	flag1=terminate_1('A',G)
	flag2=terminate_1('B',G)
	if flag1==1 or flag2==1 or count>=100:
		return 1
	else:
		return 0

def reset_node_attributes(G,action_dict):
	for each in action_dict:
		G.node[each]['action']=action_dict[each]
############################################3
lst=list()
def CentralityMeasures2(G):
	y=sorted(nx.closeness_centrality(G),key=nx.closeness_centrality(G).get, reverse=True)
	# Closeness centrality
	clo_cen = y
	#print ("# Closeness centrality:" + str(clo_cen))
	return y
def buildG(G):
    reader = csv.reader(open("graph.csv"))
    next(reader, None)
    for line in reader:    
        G.add_edge(str(line[0]),str(line[3]),weight= float(1.0))
        

def CmtyGirvanNewmanStep(G):
    if _DEBUG_:
        print ("Calling CmtyGirvanNewmanStep")
    init_ncomp = nx.number_connected_components(G)    #no of components
    ncomp = init_ncomp
    while ncomp <= init_ncomp:
        bw = nx.edge_betweenness_centrality(G, weight='weight')    #edge betweenness for G
        #find the edge with max centrality
        max_ = max(bw.values())
        #find the edge with the highest centrality and remove all of them if there is more than one!
        for k, v in bw.items():
            if float(v) == max_:
                G.remove_edge(k[0],k[1])    #remove the central edge
        ncomp = nx.number_connected_components(G)    #recalculate the no of components

#compute the modularity of current split
def _GirvanNewmanGetModularity(G, deg_, m_):
    New_A = nx.adj_matrix(G)
    New_deg = {}
    New_deg = UpdateDeg(New_A, G.nodes())
    #Let's compute the Q
    comps = nx.connected_components(G)    #list of components    
    print ('No of communities in decomposed G: %d' % nx.number_connected_components(G))
    Mod = 0    #Modularity of a given partitionning
    for c in comps:
        EWC = 0    #no of edges within a community
        RE = 0    #no of random edges
        for u in c:
            EWC += New_deg[u]
            RE += deg_[u]        #count the probability of a random edge
        Mod += ( float(EWC) - float(RE*RE)/float(2*m_) )
    Mod = Mod/float(2*m_)
    if _DEBUG_:
        print ("Modularity: %f" % Mod)
    return Mod

def UpdateDeg(A, nodes):
    deg_dict = {}
    nodes=list(nodes)
    n = len(nodes)  #len(A) ---> some ppl get issues when trying len() on sparse matrixes!
    B = A.sum(axis = 1)
    for i in range(n):
        deg_dict[nodes[i]]= B[i,0]
    #print(deg_dict)
    return deg_dict

#run GirvanNewman algorithm and find the best community split by maximizing modularity measure
def runGirvanNewman(G, Orig_deg, m_):
    #let's find the best split of the graph
    BestQ = 0.0
    Q = 0.0
    while True:    
        CmtyGirvanNewmanStep(G)
        Q = _GirvanNewmanGetModularity(G, Orig_deg, m_);
        print ("Modularity of decomposed G: %f" % Q)
        if Q > BestQ:
            BestQ = Q
            Bestcomps = nx.connected_components(G)    #Best Split
            lst=list(Bestcomps)
        else:
            print ("Max modularity (Q): %f" %BestQ)
            size=list()
            tt=(len(lst))
            for i in range(tt):
                size.append(len(lst[i]))
                print("A community of length",len(lst[i]),": ",lst[i])
            maximum=max(size)
            minimum=min(size)
            diff=maximum-minimum
            q=list()
            for i in range(len(size)):
                q.append(math.ceil((size[i]/diff)*4))
            for i in range(len(size)):
                print ("number of nodes to be taken from the community are:", q[i])
            pos = nx.spring_layout(G)
            count = 0.
            colors = ['r', 'b', 'g', '#FF0099', '#660066', '#CD5C5C', '#000000', '#123456', '#00FFFF', '#A056F2', '#888888','#AABBCC','#BFCFDF', '#500000', '#EFFEEF','#FF8C00','#008000','#0000FF','#483D8B']
            for x in range(len(lst)) :
                count = count + 1.
                list_nodes = lst[x]
                nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 30,node_color=colors[int((count-1)%9)])
            nx.draw_networkx_edges(G, pos, alpha=0.5)
            plt.show()
            break
        if BestQ > 0.0:
            print ("Max modularity (Q): %f" %BestQ)
            #print ("Graph communities:", list(Bestcomps))
        else:
            print ("Max modularity (Q): %f" % BestQ)
    return q,lst

def mn():
    
    G = nx.Graph()  #let's create the graph first
    buildG(G)
    print ('G nodes:', G.nodes())
    if _DEBUG_:
        print ('G nodes:', G.nodes())
        print ('G no of nodes:', G.number_of_nodes())
    
    n = G.number_of_nodes()    #|V|
    print("nodes=",n)
    A = nx.adj_matrix(G)    #adjacenct matrix
    print("Matrix=",A)
    m_ = 0.0    #the weighted version for number of edges
    for i in range(0,n):
        for j in range(0,n):
            m_ += A[i,j]
    m_ = m_/2.0
    print("M=",m_)
    if _DEBUG_:
        print ("m: %f" % m_)

    #calculate the weighted degree for each node
    Orig_deg = {}
    Orig_deg = UpdateDeg(A, G.nodes())
    p=CentralityMeasures2(G)
    print("The sorted list:")
    print(p)
    #run Newman alg
    quantity,community=runGirvanNewman(G, Orig_deg, m_)
    seed=list()
    for i in range(len(quantity)):
        j=quantity[i]
        for k in range(len(p)):
            if p[k] in community[i] and j>0:
                j=j-1
                seed.append(p[k])
    print("till now:",seed)
#########################################################################
    set_all_B(G)
    list1=seed
    set_A(G,list1)
    colors=get_colors(G)
    nx.draw(G,node_color=colors, node_size=10)
    plt.show()
    flag=0
    count=0
    while(1):
	    flag=terminate(G,count)
	    if flag==1:
		    break
	    count=count+1
	    action_dict=recalculate_options(G)
	    reset_node_attributes(G,action_dict)
	    colors=get_colors(G)
	    c=terminate_1('A',G)
    active=colors.count('green')
    inactive=colors.count('red')
    print('Total active nodes: ',active,'Total inactive nodes: ',inactive)
    infl.append(active)
    if c==1:
	    print ('Cascade is complete in:',count,'iterations taking two nodes having highest degree centrality initially')
    else:
	    print ('Cascade incomplete')
	
    nx.draw(G,node_color=colors, node_size=80)
    plt.show()
    
if __name__ == "__main__":
    mn()
