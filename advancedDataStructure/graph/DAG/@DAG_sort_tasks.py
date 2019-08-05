import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd



def create_DAG(abs_file = "C:/Users/Atul Anand/PycharmProjects/sunrun3/objectiveDoubt/fileData/task_files/input/test.csv"
               ):
    G2 = nx.DiGraph()
    df1 = pd.read_csv(abs_file)
    print(df1)

    for index, row in df1.iterrows():
        print("row['tasknumber']" , row['tasknumber'], "row['Parent_Task_Numbers']", row['Parent_Task_Numbers'])
        parents = row['Parent_Task_Numbers'].split(",")
        for p in parents:
            G2.add_edge(int(p), int(row['tasknumber']))

    nodes = df1["tasknumber"].tolist()
    map(G2.add_node, nodes)

    for item in nodes:
            print("successors of {} is {}".format(item, list(G2.successors(item))))

    # now draw the graph:
    nx.draw(G2, with_labels=True, edge_color='r')
    plt.show()
    print("graph printed ")

    return G2


G2 = create_DAG()

order = nx.topological_sort(G2)
print("order :", order)
abs_file = "C:/Users/Atul Anand/PycharmProjects/sunrun3/objectiveDoubt/fileData/task_files/input/test.csv"
df2 = pd.read_csv(abs_file)
df3 = pd.DataFrame(columns=df2.columns)

for task in order:
    row1 = df2.loc[df2['tasknumber'] == task]
    df3 = df3.append(row1, ignore_index=True)


print("rearranged data frame is : ", df3)