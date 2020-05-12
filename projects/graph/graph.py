"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist!")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
        path = []
        while q.size() > 0:
            visit = q.dequeue()
            if visit not in visited:
                path.append(visit)
                visited.add(visit)
                for next_vertex in self.get_neighbors(visit):
                    q.enqueue(next_vertex)
        print(path)

    def dft(self, starting_vertex):
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        path = []
        while s.size() > 0:
            visit = s.pop()
            if visit not in visited:
                path.append(visit)
                visited.add(visit)
                for next_vertex in self.get_neighbors(visit):
                    s.push(next_vertex)
        print(path)

    def dft_recursive(self, starting_vertex, visited=set()):
        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
            for next_vertex in self.get_neighbors(starting_vertex):
                self.dft_recursive(next_vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        # create an empty queue and enqueue the path to the starting vertex id
        q = Queue()
        q.enqueue([starting_vertex])
        # create a set to store visited vertices
        visited = set()
        # while queue not empty
        while q.size() > 0:
            # dequeue the first path
            path = q.dequeue()
            # grab the last vertex from the path
            v = path[-1]
            # if vertex is not in visited
            if v not in visited:
                # check if it is the target
                if v == destination_vertex:
                    # return the path to the target
                    return path
                # mark it visited
                visited.add(v)
                # add `PATH TO` neighbours to back of queue
                for next_vertex in self.get_neighbors(v):
                    # copy the path
                    new_path = list(path)
                    # append the neighbor to the back of it
                    new_path.append(next_vertex)
                    q.enqueue(new_path)
        # return none
        return None

    def dfs(self, starting_vertex, destination_vertex):
        # create an empty stack and push the path to the starting vertex id
        s = Stack()
        s.push([starting_vertex])
        # create a set to store visited vertices
        visited = set()
        # while queue not empty
        while s.size() > 0:
            # pop the first path
            path = s.pop()
            # grab the last vertex from the path
            v = path[-1]
            # if vertex is not in visited
            if v not in visited:
                # check if it is the target
                if v == destination_vertex:
                    # return the path to the target
                    return path
                # mark it visited
                visited.add(v)
                # add `PATH TO` neighbours to back of queue
                for next_vertex in self.get_neighbors(v):
                    # copy the path
                    new_path = list(path)
                    # append the neighbor to the back of it
                    new_path.append(next_vertex)
                    s.push(new_path)
        # return none
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, stack=Stack(), visited=set()):
        if len(visited) == 0:
            stack.push([starting_vertex])
        elif stack.size() == 0:
            return None
        path = stack.pop()
        v = path[-1]
        if v not in visited:
            if v == destination_vertex:
                return path
            visited.add(v)
            for next_vertex in self.get_neighbors(v):
                new_path = list(path)
                new_path.append(next_vertex)
                stack.push(new_path)
        return self.dfs_recursive(
            starting_vertex, destination_vertex, stack, visited)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
