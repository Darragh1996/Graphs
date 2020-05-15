from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


# class Queue():
#     def __init__(self):
#         self.queue = []

#     def enqueue(self, value):
#         self.queue.append(value)

#     def dequeue(self):
#         if self.size() > 0:
#             return self.queue.pop(0)
#         else:
#             return None

#     def size(self):
#         return len(self.queue)


# class Stack():
#     def __init__(self):
#         self.stack = []

#     def push(self, value):
#         self.stack.append(value)

#     def pop(self):
#         if self.size() > 0:
#             return self.stack.pop()
#         else:
#             return None

#     def size(self):
#         return len(self.stack)


class Graph():
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = {}

    def add_edge(self, v1, v2, direction):
        inverse_dir = {
            "n": "s",
            "s": "n",
            "e": "w",
            "w": "e"
        }
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1][direction] = v2
            self.vertices[v2][inverse_dir[direction]] = v1
        else:
            raise IndexError("Vertex does not exist!")


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# graph = Graph()
# q = Queue()
# room = player.current_room.id
# graph[room] = {"n": "?","s": "?","e": "?","w": "?"}
# q.enqueue([room])
# while q.size() > 0:
#     path = q.dequeue()
#     v = path[-1]
#     if v not in graph.vertices:
#         graph.add_vertex(v)
#         for p_exit in player.current_room.get_exits():
#             if graph[v][p_exit] == "?":


def navigate(graph=Graph(), direction=None,):
    inverse_dir = {
        "n": "s",
        "s": "n",
        "e": "w",
        "w": "e"
    }
    room = player.current_room.id
    exits = player.current_room.get_exits()
    if room not in graph.vertices:
        graph.add_vertex(room)
    for ext in exits:
        if ext not in graph.vertices[room]:
            player.travel(ext)
            traversal_path.append(ext)
            current_room = player.current_room.id
            if current_room not in graph.vertices:
                graph.add_vertex(current_room)
            graph.add_edge(room, current_room, ext)
            navigate(graph, ext)

    if direction != None:
        player.travel(inverse_dir[direction])
        traversal_path.append(inverse_dir[direction])


navigate()

# s = Stack()
# g = Graph()
# g.add_vertex(player.current_room.id)
# s.push(player.current_room.id)
# while s.size() > 0:
#     for ext in player.current_room.get_exits():

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
