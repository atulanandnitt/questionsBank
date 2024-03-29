class Vertex:
    def __init__(self,n):
        self.name=n
        self.neighbors=list()
        
        self.distance =999
        self.color='black'
        
    def add_neighbor(self,v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()
            
class Graph:
    vertices ={}
    
    def add_vertex(self,vertex):
        if isinstance(vertex,Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False
        
    def add_edge(self,u,v):
        if u in self.vertices and v in self.vertices:
            for key,value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key ==v:
                    value.add_neighbor(u)
            return True
        else:
            return False
        
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key +str(self.vertices[key].neighbors))
            
    def bfs(self,vert):
        q=list()
        vert.distance =0
        vert.color='red'
        for v in vert.neighbors:
            self.vertices[v].distance = vert.distance +1
            q.append(v)
        while len(q) > 0:
            u=q.pop(0)
            node_u = self.vertices[v]
            
                
        