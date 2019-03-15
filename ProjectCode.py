import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import networkx as nx
#from networkx.utils import py_random_state
import csv
import itertools

graph=[]
#G = nx.Graph()
url='network_data1.csv'
names=['time','node_0','node_1','auth_orientation','status']
df = pandas.read_csv(url,parse_dates=True,names=names ,header=0)
df=df.head(100)
print (df)
g = nx.from_pandas_edgelist(df, source='node_0', target='node_1')
fig = plt.subplots(figsize=(30,50))
pos = nx.spring_layout(g)
nx.draw(g, pos)     #showing graph of first 100 nodes
G = nx.from_pandas_edgelist(df,'node_0','node_1', edge_attr='auth_orientation')
durations = [i['auth_orientation'] for i in dict(G.edges).values()]
labels = [i for i in dict(G.nodes).keys()]
labels = {i:i for i in dict(G.nodes).keys()}

fig, ax = plt.subplots(figsize=(40,40))
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, ax = ax, labels=True)
nx.draw_networkx_edges(G, pos, width=durations, ax=ax)
_ = nx.draw_networkx_labels(G, pos, labels, ax=ax)      #showing graph with different edge width and node name
elarge = [(node_0, node_1) for (node_0, node_1, auth_orientation) in G.edges(data=True) if auth_orientation['auth_orientation'] == 6]
esmall = [(node_0, node_1) for (node_0, node_1, auth_orientation) in G.edges(data=True) if auth_orientation['auth_orientation'] == 2]
print(elarge)  #edges with logon orientation
print(esmall)   #edges with logoff orientation
#pos = nx.spring_layout(G)  # positions for all nodes
# nodes
fig = plt.subplots(figsize=(50,50))
nx.draw_networkx_nodes(G, pos, node_size=500)

# logon edges
nx.draw_networkx_edges(G, pos, edgelist=elarge,width=6, style='dashed')
fig = plt.subplots(figsize=(50,50))
nx.draw_networkx_nodes(G, pos, node_size=500)

# logoff edges
nx.draw_networkx_edges(G, pos, edgelist=esmall,width=2, style='solid')
self_nodes= G.selfloop_edges()
print(self_nodes)
list_degree=[]

print ('Degree of Every Node \n')
list_degree=G.degree(G)
for i,j in list_degree:
    print(i) #degree of every node in the graph G

print ('\n\n')

print ('betweenness_centrality of every node \n')
list_betweenness=nx.betweenness_centrality(G)
for k,v in list_betweenness.items():
    print(k,':',v) #betweenness_centrality of all the selected node in graph

print ('\n\n')

print ('closeness_centrality of every node \n')
list_closeness=nx.closeness_centrality(G)
for k,v in list_closeness.items():
    print(k,':',v)  #closeness_centrality of all the selected node in graph

print ('\n\n')

print ('degree_centrality of every node \n')
list_degreecentrality=nx.degree_centrality(G)
for k,v in list_degreecentrality.items():
    print(k,':',v) #degree_centrality of all the selected node in graph

print ('\n\n')

print ('Clustering Coefficient of the graph \n')
list_clustering=nx.clustering(G)
for k,v in list_clustering.items():
    print(k,':',v) #clustering Coefficient of the nodes in given graph
