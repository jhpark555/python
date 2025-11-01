import queue
import math
from queue import PriorityQueue

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
            return self.edges[neighbor]
        return None
    
    def get_neighbors(self):
        neighbors=set()
        for edge in self.edges.values():
            neighbors.add(edge.to_node)
        return neighbors
    
    def get_out_neighbors(self):
        neighbors=set()
        for edge in self.edges.values():
            neighbors.add(edge.to_node)
        return neighbors
    
        
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
            self.nodes[to_node].add_edge(from_node,weight)
            
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
    
    def get_in_neighbors(self,target):
        neighbors=set()
        for node in self.nodes:
            if target in node.edges:
                neighbors.add(node.index)
        return neighbors


class GraphMatrix:
    def __init__(self,num_nodes,undirected=False):
        self.num_nodes=num_nodes
        self.undirected =undirected
        self.connections =[[0.0]*num_nodes for _ in range(num_nodes)]
        
    def get_edge(self,from_node,to_node):
        if from_node< 0 or from_node>=self.num_nodes:
            raise IndexError
        if to_node <0 or to_node>=self.num_nodes:
            raise IndexError
        return self.connections[from_node][to_node]
        
    def set_edge(self,from_node,to_node,weight):
        if from_node< 0 or from_node>=self.num_nodes:
            raise IndexError
        if to_node <0 or to_node>=self.num_nodes:
            raise IndexError
        
        self.connections[from_node][to_node]=weight
        if self.undirected:
            self.connections[to_node][from_node]=weight
            


class UnionFindNode:
    def __init__(self,label):
        self.label=label
        self.parent=None

class UnionFind:
    def __init__(self,num_sets):
        self.nodes=[UnionFindNode(i) for i in range(num_sets)]
        self.set_sizes=[1 for i in range(num_sets)]
        self.num_disjoint_sets=num_sets

    def find_set(self,label):
        if label<0 or label>=len(self.nodes):
            raise IndexError
        current=self.nodes[label]
        while current.parent is not None:
              current= current.parent
        return current.label
    def are_disjoint(self,label1,label2):
        return self.find_set(label1) !=self.find_set(label2)
    def union_sets(self,label1,label2):
        set1_label=self.find_set(label1)
        set2_label=self.find_set(label2)
        if set1_label==set2_label:
            return
        if self.set_sizes[set1_label]< self.set_sizes[set2_label]:
            small=set1_label
            large=set2_label
        else:
            small=set2_label
            large=set1_label
        self.nodes[small].parent=self.nodes[large]
        self.set_sizes[large] +=self.set_sizes[small]
        self.set_sizes[small]=0
        self.num_disjoint_sets -=1
         


class DFSTreeStats:
    def __init__(self,num_nodes):
        self.parent=[-1]*num_nodes
        self.next_order_index=0
        self.order=[-1]*num_nodes
        self.lowest=[-1]*num_nodes

    def set_order_index(self,node_index):
        self.order[node_index]=self.next_order_index
        self.next_order_index +=1
        self.lowest[node_index]=self.order[node_index]

 





            
def clustering_coefficient(g:Graph ,ind:int)->float:
    neighbors=g.nodes[ind].get_neighbors()   
    num_neighbors = len(neighbors)

    count=0
    for nl in neighbors:
        for edge in g.nodes[nl].get_edge_list():
            if edge.to_node >nl and edge.to_node in neighbors:
                count +=1
    total_possible=(num_neighbors *(num_neighbors -1))/2.0

    if total_possible ==0.0 :
        return 0.0
    return count/total_possible     


def check_node_path_vaild(g,path):
    num_nodes_on_path=len(path)
    if num_nodes_on_path==0:
        return True
    prev_node=path[0]
    if prev_node<0 or prev_node>=g.num_nodes:
        return False
    for step in range(1,num_nodes_on_path):
        next_node =path[step]
        if not g.is_edge(prev_node,next_node):
            return False
        prev_node=next_node
    return True

def check_edge_path_valid(g, path):
    if len(path)==0:
        return True
    prev_node=path[0].from_node
    if prev_node <0 or prev_node>=g.num_nodes:
        return False
    for edge in path:
        if edge.from_node !=prev_node:
            return False
        next_node=edge.to_node
        if not g.is_edge(prev_node,next_node):
            return False
        prev_node=next_node
    return True

def make_node_path_from_last(last, dest):
    reverse_path=[]
    current=dest
    while current !=-1:
        reverse_path.append(current)
        current=last[current]
    path=list(reversed(reverse_path))
    return path

def check_last_path_valid(g, last):
    if len(last)!=g.num_nodes:
        return False
    for to_node, from_node in enumerate(last):
        if from_node!=-1 and not g.is_edge(from_node,to_node):
            return False
    return True

def compute_path_cost_from_edges(path):
    if len(path) ==0:
        return 0.0
    cost = 0.0
    prev_node= path[0].from_node
    for edge in path:
        if edge.from_node !=prev_node:
            cost=math.inf
        else :
            cost=cost+edge.weight
        prev_node=edge.to_node
    return cost    


def dfs_recursive_basic(g,ind,seen):
    seen[ind]=True
    current=g.nodes[ind]

    for edge in current.get_edge_list():
        #print("@",edge.to_node)
        neighbor=edge.to_node
        if not seen[neighbor]:
            print(neighbor,end="->")
            dfs_recursive_basic(g,neighbor,seen)

def depth_first_search_basic(g,start):
    seen=[False]*g.num_nodes
    dfs_recursive_basic(g,start,seen)


def dfs_recursive_path(g,ind,seen,last):
    seen[ind]=True
    current=g.nodes[ind]

    for edge in current.get_edge_list():
        #print("@",edge.to_node)
        neighbor=edge.to_node
        if not seen[neighbor]:
            last[neighbor]=ind
            dfs_recursive_path(g,neighbor,seen,last)    

def depth_first_search_path(g):
    seen=[False]*g.num_nodes
    last=[-1]*g.num_nodes
    for ind in range(g.num_nodes):
        if not seen[ind]:
            dfs_recursive_path(g,ind,seen,last)
    return last

def depth_first_search_basic_all(g):
    seen=[False]*g.num_nodes
    for ind in range(g.num_nodes):
        if not seen[ind]:
            dfs_recursive_basic(g,ind,seen)

def depth_first_search_stack(g,start):
    seen = [False]*g.num_nodes
    last = [-1] *g.num_nodes
    to_explorer=[]

    to_explorer.append(start)
    while to_explorer:
        ind = to_explorer.pop()
        if not seen[ind]:
            current= g.nodes[ind]
            seen[ind]= True

            all_edges = current.get_sorted_edge_list()
            all_edges.reverse()
            for edge in all_edges:
                neighbor = edge.to_node
                if not seen[neighbor]:
                    last[neighbor]=ind
                    to_explorer.append(neighbor)
    return last


#dfs for connected-components
def dfs_recursive_cc(g,ind,component,curr_comp):
    component[ind]=curr_comp
    current=g.nodes[ind]

    for edge in current.get_edge_list():
        neighbor=edge.to_node
        if component[ind]==-1:
            dfs_recursive_cc(g,neighbor,component,curr_comp)

def dfs_connected_components(g):
    component=[-1]*g.num_nodes
    curr_comp=0

    for ind in range(g.num_nodes):
        if component[ind]==-1:
            dfs_recursive_cc(g,ind,component,curr_comp)
            curr_comp +=1
    return component



def breadth_first_search(g,start):
    seen=[False]*g.num_nodes
    last=[-1]*g.num_nodes
    pending = queue.Queue()

    pending.put(start)
    seen[start]=True

    while not pending.empty():
        index=pending.get()
        current=g.nodes[index]

        for edge in current.get_edge_list():
            neighbor =edge.to_node
            if not seen[neighbor]:
                pending.put(neighbor)
                seen[neighbor]=True
                last[neighbor]=index
    return last


def make_grid_graph(width,height):
    num_nodes= width*height
    g=Graph(num_nodes,undirected=True)
    for r in range(height):
        for c in range(width):
            index = r*width+c
            if(c< width -1):
                g.insert_edge(index,index+1,1.0)
            if(r<height-1):
                g.insert_edge(index,index+width,1.0)

    return g



def Dijkstras(g: Graph,start_index:int)->list:
    cost:list=[math.inf]*g.num_nodes
    last:list=[-1]*g.num_nodes
    pq = PriorityQueue(min_heap=True)
    pq.enqueue(start_index,0.0)

    for i in range(g.num_nodes):
        if i!= start_index:
            pq.enqueue(i,math.inf)
    cost[start_index]=0.0

    while not pq.is_empty():
        index=pq.dequeue()

        for edge in g.nodes[index].get_edge_list():
            neighbor=edge.to_node
            if pq.in_queue(neighbor):
                new_cost=cost[index]+edge.weight
                if new_cost< cost[neighbor]:
                    pq.update_priority(neighbor,new_cost)
                    last[neighbor]=index
                    cost[neighbor]=new_cost
    return last


def BellmanFord(g,start_index):
    cost = [math.inf]*g.num_nodes
    last =[-1]*g.num_nodes
    all_edges=g.make_edge_list()
    cost[start_index]=0.0
    
    #for i in all_edges:
    #    print(i.from_node,i.to_node)
    for itr in range(g.num_nodes-1):
        for edge in  all_edges:
            cost_thr_node=cost[edge.from_node]+edge.weight
            if cost_thr_node< cost[edge.to_node]:
                cost[edge.to_node]=cost_thr_node
                last[edge.to_node]=edge.from_node
    for edge in all_edges:
        if cost[edge.to_node]> cost[edge.from_node]+edge.weight:
            return Node
    return last


def is_topo_ordered(g,ordering):
    if len(ordering) !=g.num_nodes:
        return False
    index_to_pos=[-1]*g.num_nodes
    for pos in range(g.num_nodes):
        current=ordering[pos]
        if index_to_pos[current] !=-1:
            return False
        index_to_pos[current]=pos
    for n in g.nodes:
        for edge in n.get_edge_list():
            if index_to_pos[edge.to_node] <=index_to_pos[n.index]:
                return False
    return True


def Kahns(g)->list:
    count =[0]*g.num_nodes
    s=[]
    result=[]

    for current in g.nodes:
        for edge in current.get_edge_list():
            count[edge.to_node]=count[edge.to_node]+1
    for current in g.nodes:
        if count[current.index]==0:
            s.append(current.index)

    while len(s)>0:
        current.index=s.pop()
        result.append(current_index)
        for edge in g.nodes[current_index].get_edge_list():
            count[edge.to_node]=count[edge.to_node]-1
            if count[edge.to_node]==0:
                s.append(edge.to_node)
    return result



def topological_dfs(g):
    seen=[False]*g.num_nodes
    s=[]
    for ind in range(g.num_nodes):
        if not seen[ind]:
            topological_dfs_recursive(g,ind,seen,s)
    s.reverse()
    return s

def topological_dfs_recursive(g,index,seen,s):
    seen[index]=True
    current = g.nodes[index]
    for edge in current.get_edge_list():
        neighbor =edge.to_node
        if not seen[neighbor]:
            topological_dfs_recursive(g,neighbor,seen,s)
    s.append(index)


def kruskals(g):
    djs=UnionFind(g.num_nodes)
    all_edges=[]
    mst_edges=[]

    for idx in range(g.num_nodes):
        for edge in g.nodes[idx].get_edge_list():
            if edge.to_node > edge.from_node:
                all_edges.append(edge)
    all_edges.sort(key=lambda  edge:edge.weight)

    for edge in all_edges:
        if djs.are_disjoint(edge.to_node,edge.from_node):
            mst_edges.append(edge)
            djs.union_sets(edge.to_node,edge.from_node)
    if djs.num_disjoint_sets==1:
        return mst_edges
    else:
        return None


def bridge_finding_dfs(g,index,stats:DFSTreeStats,results):
    stats.set_order_index(index)

    for edge in g.nodes[index].get_sorted_edge_list():
        neighbor=edge.to_node
        if stats.order[neighbor]==-1:
            stats.parent[neighbor]=index
            bridge_finding_dfs(g,neighbor,stats,results)
            stats.lowest[index]=min(stats.lowest[index],stats.lowest[neighbor])
            if stats.lowest[neighbor]>=stats.order[neighbor]:
                results.append(edge)
        elif neighbor!=stats.parent[index]:
            stats.lowest[index]=min(stats.lowest[index],stats.order[neighbor])

def find_bridges(g):
    results=[]
    stats=DFSTreeStats(g.num_nodes)
    for index in range(g.num_nodes):
        if stats.order[index]==-1:
            bridge_finding_dfs(g,index,stats,results)
    return results


def articulation_point_dfs(g,index,stats,results):
    stats.set_order_index(index)
    for edge in g.nodes[index].get_edge_list():
        neighbor= edge.to_node
        if stats.order[neighbor]==-1:
            stats.parent[neighbor]=index
            articulation_point_dfs(g,neighbor,stats,results)
            stats.lowest[index]=min(stats.lowest[index],stats.lowest[neighbor])
            if stats.lowest[neighbor] >=stats.order[index]:
                results.add(index)
        elif neighbor !=stats.parent[index]:
            stats.lowest[index]=min(stats.lowest[index],stats.order[neighbor])

def articulation_point_root(g,root,stats,results):
    stats.set_order_index(root)
    num_subtrees=0

    for edge in g.nodes[root].get_edge_list():
        neighbor=edge.to_node
        if stats.order[neighbor]==-1:
            stats.parent[neighbor]=root
            articulation_point_dfs(g,neighbor,stats,results)
            num_subtrees +=1
    if num_subtrees>=2:
        results.add(root)

def find_articuation_points(g):
    stats=DFSTreeStats(g.num_nodes)
    results=set()
    for index in range(g.num_nodes):
        if stats.order[index]==-1:
            articulation_point_root(g,index,stats,results)
    return results


if __name__ == '__main__':
    g= Graph(10, True)
    g.insert_edge(0,1,1.0)
    g.insert_edge(0,5,1.0)
    g.insert_edge(0,7,1.0)
    g.insert_edge(1,2,1.0)
    g.insert_edge(2,3,1.0)
    g.insert_edge(2,4,1.0)
    g.insert_edge(2,5,1.0)
    g.insert_edge(4,9,1.0)
    g.insert_edge(5,8,1.0)
    g.insert_edge(6,8,1.0)
    g.insert_edge(7,8,1.0)
    g.insert_edge(7,8,1.0)
    g.insert_edge(8,9,1.0)
    
    gg=GraphMatrix(5,undirected=False)
    
    gg.set_edge(0, 1, 1.0)
    gg.set_edge(0, 3, 1.0)
    gg.set_edge(0, 4, 3.0)
    gg.set_edge(1, 2, 2.0)
    gg.set_edge(1, 4, 1.0)
    gg.set_edge(3, 4, 3.0)
    gg.set_edge(4, 2, 3.0)
    gg.set_edge(4, 3, 3.0)
    
    
    r=g.make_edge_list()
    for i in r:
        print(i.from_node,i.to_node,i.weight)
        
    for i in range(5):
        print("{")
        for j in range(5):
            print(gg.get_edge(i,j))
        print("}")

    for i in range(5):
        print(g.get_in_neighbors(i))
        
    r= clustering_coefficient(g,1)
    print(r) 

    r=check_node_path_vaild(g,[1,4])
    print(r)

    depth_first_search_basic(g,0)
    print("")
    depth_first_search_basic(g,1)
    print("")
    depth_first_search_basic_all(g)
    print("")
    r=depth_first_search_path(g)
    print(r)
    r=depth_first_search_stack(g,0)
    print(r)

    r=dfs_connected_components(g)
    print(r)

    r=breadth_first_search(g,0)
    print(r)

   # r=Dijkstras(g,0)
    r=BellmanFord(g,0)
    print(r)
    #print(Kahns(g))
    print(topological_dfs(g))
    r=kruskals(g)
    for i in r:
        print(i.from_node,i.to_node);
    print("###########")
    r=find_bridges(g)
    for i in r:
        print(i.from_node,i.to_node);

    r=find_articuation_points(g)
    print("AR point=",r)