# Please see instructions.txt for the description of this problem.
# from exceptions import NotImplementedError

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

    # if len(self.graph) == 0: 
    #     return ()

    visited = []
    dist = {}
    dist[source] = 0
    previous = {}

    queue = [(source, graph.get_neighbors(source))]
    # print("current_node: ", current_node)
    # print("queue: ", queue)
    visited.append(source)

    while len(queue) > 0:
        current = queue.pop(0)
        current_node = current[0]
        neighbour_arr = current[1]
        # print("-------------------")
        # print("current_node: ", current_node)
        # print("neighbour_arr: ", neighbour_arr)

        for edge in neighbour_arr:
            # print("edge: ", edge)

            if edge[0] not in visited:
                neighbours = graph.get_neighbors(edge[0])
                if neighbours and len(neighbours) > 0:
                    queue = queue + [(edge[0], neighbours)]
                    visited.append(edge[0])
            
            # print("visited:", visited)
            # print("queue:", queue)
            # print("calculate dist...")
            if current_node not in dist:
                dist[current_node] = float('inf')

            if edge[0] not in dist:
                dist[edge[0]] = float('inf')

            if edge[1] + dist[current_node] < dist[edge[0]]:
                dist[edge[0]] = edge[1] + dist[current_node]
                previous[edge[0]] = current_node

            # print(">> dist:", dist)
            # print(">> previous: ", previous)

    # generate the path
    path_start = target
    arr = [path_start]
    while path_start in previous:
        # print('/////////')
        p = previous[path_start]
        arr.insert(0, p)
        path_start = p
        # print("path_start: ", path_start)
        # print("arr: ", arr)

    ret = (arr, dist[target])
    # print("====> ret: ", ret)
    return ret





