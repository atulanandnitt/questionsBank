import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import uuid


def create_DAG():
    G = nx.DiGraph()
    G2 = nx.DiGraph()


    abs_file = "C:/Users/Atul Anand/PycharmProjects/folder_name/objectiveDoubt/fileData/task_files/input/test.csv"
    df1 = pd.read_csv(abs_file)
    print(df1)

    for index, row in df1.iterrows():
        print("row['tasknumber']" , row['tasknumber'], "row['Parent_Task_Numbers']", row['Parent_Task_Numbers'])
        parents = row['Parent_Task_Numbers'].split(",")
        for p in parents:
            G.add_edge(int(row['tasknumber']),int(p))
            G2.add_edge(int(p), int(row['tasknumber']))


    nodes = df1["tasknumber"].tolist()
    # add 5 nodes, labeled 0-4:
    map(G.add_node, nodes)
    map(G2.add_node, nodes)


    nodes = list(range(15))
    print("number_of_nodes : ",G.number_of_nodes())
    print("number_of_edges : ",G.number_of_edges())


    for item in nodes:
            print("successors of {} is {}".format(item, list(G.successors(item))))

    for item in nodes:
            print("successors of {} is {}".format(item, list(G2.successors(item))))
    # now draw the graph:
    nx.draw(G2, with_labels=True, edge_color='r')
    # plt.show()
    print("graph printed ")

    return G2


G2 = create_DAG()
if nx.is_directed_acyclic_graph(G2):
    print("graph G2 is DAG" )
else:
    print("graph G2 is NOT DAG")
jobs = {}
# for node in G2:
#    jobs[node] = nx.randomwait
# view = nx.load_balanced_view()

results = {}
order = nx.topological_sort(G2)
print("order :", order, type(order))


for i in order:
    print("i :", i)

# build tree
nodes = [order[0]] # start with first node in topological order
labels = {}
print("edges")
tree = nx.Graph()
while nodes:
    source = nodes.pop()
    labels[source] = source
    for target in G2.neighbors(source):
        if target in tree:
            t = uuid.uuid1() # new unique id
        else:
            t = target
        labels[t] = target
        tree.add_edge(source,t)
        print(source,target,source,t)
        nodes.append(target)

nx.draw(tree,labels=labels)
plt.show()

for node in nx.topological_sort(G2):
   # get list of AsyncResult objects from nodes
   # leading into this one as dependencies
   print("node :", node)
   deps = [ results[n] for n in G2.predecessors(node)]
   print("deps", deps)
#    # submit and store AsyncResult object
#    with view.temp_flags(after=deps, block=False):
#         results[node] = view.apply(jobs[node])
#
# view.wait(results.values())


# from matplotlib.dates import date2num
#
# from matplotlib import gist_rainbow
#
# pos = {}; colors = {}
#
# for node in G2:
#    md = results[node].metadata
#    start = date2num(md.started)
#    runtime = date2num(md.completed) - start
#    pos[node] = (start, runtime)
#    colors[node] = md.engine_id
#
# nx.draw(G2, pos, node_list=colors.keys(), node_color=colors.values(),
#    cmap=gist_rainbow)

# for item in nodes:
#         print("parents of {} is {}".format(item, list(G.parents(item))))




# G = nx.petersen_graph()
# plt.subplot(121)
# nx.draw(G, with_labels=True, font_weight='bold')
# plt.subplot(122)
# nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
# plt.show()
