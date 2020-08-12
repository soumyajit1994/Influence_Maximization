import networkx as nx
from networkx.algorithms import community
G=nx.read_edgelist('email-Eu-core.txt',create_using=nx.Graph(),nodetype=int)
communities_generator = community.girvan_newman(G)
top_level_communities = next(communities_generator)
next_level_communities = next(communities_generator)
sorted(map(sorted, next_level_communities))
print(next_level_communities)

