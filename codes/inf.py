import networkx as nx
import operator
import matplotlib.pyplot as plt
#from igraph import *
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
def CentralityMeasures0(G):
	w=sorted(nx.degree_centrality(G),key=nx.degree_centrality(G).get, reverse=True)
	# Degree centrality
	deg_cen = w
	#print ("# Degree centrality:" + str(deg_cen))
	return w
def CentralityMeasures1(G):
	# Betweenness centrality
	x=sorted(nx.betweenness_centrality(G),key=nx.betweenness_centrality(G).get, reverse=True)
	bet_cen = x
	#print ("# Betweenness centrality:" + str(bet_cen))
	return x
def CentralityMeasures2(G):
	y=sorted(nx.closeness_centrality(G),key=nx.closeness_centrality(G).get, reverse=True)
	# Closeness centrality
	clo_cen = y
	#print ("# Closeness centrality:" + str(clo_cen))
	return y
def CentralityMeasures3(G):
	z=sorted(nx.eigenvector_centrality(G),key=nx.eigenvector_centrality(G).get, reverse=True)
	# Eigenvector centrality
	eig_cen = z
	#print ("# Eigenvector centrality:" + str(eig_cen))
	return z
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

G=nx.read_edgelist('facebook_combined.txt',create_using=nx.Graph(),nodetype=int)

#to find communities
#communities_generator = community.girvan_newman(G)
#top_level_communities = next(communities_generator)
#next_level_communities = next(communities_generator)
#sorted(map(sorted, next_level_communities))
#print(next_level_communities)
#pp=G.community_multilevel()
#print (pp)


set_all_B(G)
a=CentralityMeasures0(G)
list1=[a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12],a[13],a[14],a[15],a[16],a[17],a[18],a[19]]
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
set_all_B(G)
a=CentralityMeasures1(G)
list1=[a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12],a[13],a[14],a[15],a[16],a[17],a[18],a[19]]
set_A(G,list1)
colors=get_colors(G)
nx.draw(G,node_color=colors, node_size=80)
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
	print ('Cascade is complete in:',count,'iterations taking two nodes having highest betweenness centrality initially')
else:
	print ('Cascade incomplete')
	
nx.draw(G,node_color=colors, node_size=80)
plt.show()


set_all_B(G)
a=CentralityMeasures2(G)
list1=[a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12],a[13],a[14],a[15],a[16],a[17],a[18],a[19]]
set_A(G,list1)
colors=get_colors(G)
nx.draw(G,node_color=colors, node_size=80)
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
	print ('Cascade is complete in:',count,'iterations taking two nodes having highest closeness centrality initially')
else:
	print ('Cascade incomplete')
	
nx.draw(G,node_color=colors, node_size=80)
plt.show()

set_all_B(G)
a=CentralityMeasures3(G)
list1=[a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12],a[13],a[14],a[15],a[16],a[17],a[18],a[19]]
set_A(G,list1)
colors=get_colors(G)
nx.draw(G,node_color=colors, node_size=80)
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
	print ('Cascade is complete in:',count,'iterations taking two nodes having highest eigen vector centrality initially')
else:
	print ('Cascade incomplete')
	
nx.draw(G,node_color=colors, node_size=80)
plt.show()
# x-coordinates of left sides of bars  
left = [1, 2, 3, 4] 
  
# heights of bars 
height = infl
  
# labels for bars 
tick_label = ['DC', 'BC', 'CC', 'EVC'] 
  
# plotting a bar chart 
plt.bar(left, height, tick_label = tick_label, 
        width = 0.8, color = ['red', 'green','yellow','blue']) 
  
# naming the x-axis 
plt.xlabel('x - axis') 
# naming the y-axis 
plt.ylabel('y - axis') 
# plot title 
plt.title('INFLUENCING POWER') 
  
# function to show the plot 
plt.show() 

