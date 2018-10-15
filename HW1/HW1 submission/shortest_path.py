#CS5112 Algorithms and Data Structures for Applications
#Assignment 1: Dijkstra's Algorithm
#Authors: Ziyu Qiu(zq64@cornell.edu), Ruoyu Wang(rmw252@cornell.edu)

# Please see instructions.txt for the description of this problem.
from exceptions import NotImplementedError

def shortest_path(graph, source, target):
  # `graph` is an object that provides a get_neighbors(node) method that returns
  # a list of (node, weight) edges. both of your graph implementations should be
  # valid inputs. you may assume that the input graph is connected, and that all
  # edges in the graph have positive edge weights.
  # 
  # `source` and `target` are both nodes in the input graph. you may assume that
  # at least one path exists from the source node to the target node.
  #
  # this method should return a tuple that looks like
  # ([`source`, ..., `target`], `length`), where the first element is a list of
  # nodes representing the shortest path from the source to the target (in
  # order) and the second element is the length of that path
  #
  # NOTE: Please see instructions.txt for additional information about the
  # return value of this method.

  # YOUR CODE HERE
    #initialize
    S = [] #visited nodes
    Q = [(source,graph.get_neighbors(source))] #unvisited nodes
    dist = {}
    dist[source] = 0
    predecessor = {}

    while len(Q) > 0:
      #extract_min
      curr = Q.pop(0)
      curr_node = curr[0]
      neighbors = curr[1]
            
      if neighbors:
        for vertex in neighbors:
          #prevent circle
          if vertex[0] not in S:
            Q = Q + [(vertex[0], graph.get_neighbors(vertex[0]))]
          if vertex[0] not in dist:
            dist[vertex[0]] = float('inf')
          #relax
          if dist[vertex[0]] > dist[curr_node] + vertex[1]:
            dist[vertex[0]] = dist[curr_node]+vertex[1]
            predecessor[vertex[0]] = curr_node
        #add current node to visited
        if curr_node not in S:
          S.append(curr_node)
    
    # output path
    pointer = target
    path = [pointer]
    while pointer in predecessor:
      pre = predecessor[pointer]
      path = [pre] + path
      pointer = pre
    return (path, dist[target])


