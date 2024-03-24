graph=dict()
graph['A']=['B','D','G']
graph['B']=['A','E','F']
graph['C']=['F','H']
graph['D']=['A','F']
graph['E']=['B','G']
graph['F']=['B','C','D']
graph['G']=['A','E']
graph['H']=['C']

matrix_elements=sorted(graph.keys())
#print(matrix_element)
cols=rows=len(matrix_elements)

adjacency_matrix=[[0 for x in range(rows)] for y in range(cols)]
#print(adjacency_matrix)
edges_list=[]

for key in matrix_elements:
    for neighbor in graph[key]:
        edges_list.append((key,neighbor))
        
#print(edges_list)
for edge in edges_list:    
    index_of_first_vertex =matrix_elements.index(edge[0])
    index_of_second_vertex=matrix_elements.index(edge[1])
    #print(index_of_first_vertex,index_of_second_vertex)
    adjacency_matrix[index_of_first_vertex][index_of_second_vertex]=1
    
#print(adjacency_matrix)

from collections import deque

def breadth_first_search(graph,root):
    visited_vertices=list()
    graph_queue=deque([root])
    visited_vertices.append(root)
    
    node =root
    
    while len(graph_queue) >0:
        node =graph_queue.popleft()
        adj_nodes=graph[node]
        #print(node,adj_nodes)
        
        remaining_elements=set(adj_nodes).difference(set(visited_vertices))
        #print(remaining_elements)
        if len(remaining_elements) >0:
            for elem in sorted(remaining_elements):
                visited_vertices.append(elem)
                graph_queue.append(elem)
                
    return visited_vertices

#print(breadth_first_search(graph, 'A'))



graph=dict()
graph['A']=['B','S']
graph['B']=['A']
graph['S']=['A','G','C']
graph['D']=['C']
graph['G']=['S','F','H']
graph['H']=['G','E']
graph['E']=['C','H']
graph['F']=['C','G']
graph['C']=['D','S','E','F']


def depth_first_search(self,root):
    visited_vertices=list()
    graph_stack=list()
    
    graph_stack.append(root)
    node =root
    
    while graph_stack:
        if node not in visited_vertices:
            visited_vertices.append(node)
        adj_nodes=graph[node]
        #print(adj_nodes)
        if set(adj_nodes).issubset(set(visited_vertices)):
            graph_stack.pop()
            #print("@",graph_stack)
            if len(graph_stack) >0:
                node =graph_stack[-1]
                #print(graph_stack,node)
            continue
        else:
            remaining_elements=set(adj_nodes).difference(set(visited_vertices))
            #print(remaining_elements)
            
        first_adj_node=sorted(remaining_elements)[0]
        #print(first_adj_node)
        graph_stack.append(first_adj_node)
        node=first_adj_node
    return visited_vertices


print(depth_first_search(graph,'A'))
            