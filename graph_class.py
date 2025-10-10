class Edge:
    def __init__(self,from_node,to_node,weight):
        self.from_node=from_node
        self.to_node=to_node
        self.weight=weight
        
class Node:
    def __init__(self,index,label=None):
        self.index=index
        self.edges={}
        self.label=label
    
    def num_edges(self):
        return len(self.edges)
    
    def get_edge(self,neighbor):
        if neighbor in self.edges:
            return self.edges[neightbor]
        return None
        
    def add_edge(self,neighbor,weight):
        self.edges[neighbor]=Edge(self.index,neighbor,weight)
        
    def remove_edge(self,neighbor):
        if neighbor in self.edges:
            del self.edges[neighbor]
            
    def get_edge_list(self):
        return list(self.edges.values())
        
    def get_sorted_edge_list(self):
        result=[]
        neighbors=(list)(self.edges.keys())
        neighbors.sort()
        
        for n in neighbors:
            result.append(self.edges[n])
        return result
        
class Graph:
    def __init__(self,num_nodes,undirected=False):
        self.num_nodes=num_nodes
        self.undirected= undirected
        self.nodes=[Node(j) for j in range(num_nodes)]
        
    def get_edge(self,from_node,to_node):
        if from_node< 0 or from_node >=self.num_nodes:
            raise IndexError
        if to_node<0 or to_node >=self.num_nodes:
            raise IndexError
        return self.nodes[from_node].get_edge(to_node)
    
    def is_edge(self,from_node,to_node):
        return self.get_edge(from_node,to_node) is not None
    
    def make_edge_list(self):
        all_edges=[]
        for node in self.nodes:
            for edge in node.edges.values():
                all_edges.append(edge)
        return all_edges
        
    def insert_edge(self,from_node,to_node,weight):
        if from_node<0 or from_node>= self.num_nodes:
            raise IndexError
        if to_node<0 or to_node >=self.num_nodes:
            raise IndexError
        self.nodes[from_node].add_edge(to_node,weight)
        if self.undirected:
            self.node[to_node].add_edge(from_node,weight)
            
    def remove_edge(self,from_node,to_node):
        if from_node<0 or from_node>= self.num_nodes:
            raise IndexError
        if to_node<0 or to_node >=self.num_nodes:
            raise IndexError
        self.nodes[from_node].remove_edge(to_node)
        if self.undireced :
            self.node[to_node].remove_edge(from_node)
            
    def insert_node(self,label=None):
        new_node=Node(self.num_nodes,label=label)
        self.nodes.append(new_node)
        self._num_nodes +=1 
        return new_node
        
    def make_copy(self):
        g2=Graph(self.num_nodes,undirected=self.undirected)
        for node in self.nodes:
            g2.nodes[node.index].label=node.label
            for edge in node.edges.values():
                g2.insert_edge(edge.from_node, edge.to_node,edge.weight)
        return g2
            

if __name__ == '__main__':
    g= Graph(5, False)
    g.insert_edge(0,1,1.0)
    g.insert_edge(0,3,1.0)
    g.insert_edge(0,4,3.0)
    g.insert_edge(1,2,2.0)
    g.insert_edge(1,4,1.0)
    g.insert_edge(3,4,3.0)
    g.insert_edge(4,2,3.0)
    g.insert_edge(4,3,3.0)
    
    
    
    r=g.make_edge_list()
    for i in r:
        print(i.from_node,i.to_node,i.weight)
        