import networkx as n
import queue

def bfs(list_, source, destination):
    global c1
    queue = []
    visited = []

    cost = {source: 0}
    parent = {source: None}
    queue.append(source)
    visited.append(source)
    
    while queue:

        current = queue.pop(0)
        print(current, end=", ")

        for neighbour in list_[current]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                cost[neighbour] = cost[current] + list_[current][neighbour]['weight']
                parent[neighbour] = current

        if current == destination:
            print("\nCost: ", cost[destination])
            c1 = cost[destination]
            break

    path = [destination]
    temp = destination
    while parent[temp] != source:
        path.append(parent[temp])
        temp = parent[temp]
    path.append(source)
    path.reverse()

    print("Path: ", end="")
    for i in path:
        print(i, end=" => ")


def ucs(list_, source, destination):
    global c2
    ucs_cost = 0
    visited = []
    q = queue.PriorityQueue()
    q.put((0, source))
    parent = {source: None}

    while q:
        cost, current = q.get()
        print(current, end=", ") 

        if current not in visited:
            visited.append(current)

            if current == destination:
                ucs_cost = cost
                break

            for neighbour in list_[current]:
                if neighbour not in visited:
                    ucs_cost = cost + list_[current][neighbour]['weight']
                    q.put((ucs_cost, neighbour))
                    parent[neighbour] = current

    print("\nCost: ", ucs_cost)
    c2 = ucs_cost
    path = [destination]
    temp = destination
    while parent[temp] != source:
        path.append(parent[temp])
        temp = parent[temp]
    path.append(source)
    path.reverse()

    print("Path: ", end="")
    for i in path:
        print(i, end=" => ")
        


    
def greedy(list_, source, destination):
    global c3
    gbfs_cost = 0
    visited = []

    q = queue.PriorityQueue()
    q.put((0, source))

    while q:
        cost, current = q.get()
        print(current, end=" => ")
        gbfs_cost += cost

        if current == destination:
            break

        else:
            for neighbour in list_[current]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    q.put((heuristics[neighbour], neighbour))

    print("\nCost: ", gbfs_cost)
    c3 = gbfs_cost


def iddfs():
    run(source, destination, 5)



iddfs_cost = 0
iddfs_path = []


def DepthLimited(src, dest, limit):
    if src == dest:
        iddfs_path.append(src)
        return True

    if limit < 0:
        return False

    for neighbour in lis[src]:
        if DepthLimited(neighbour, dest, limit - 1):
            iddfs_path.append(src)
            return True

    return False


def run(src, dest, limit):
    for x in range(limit):
        if DepthLimited(src, dest, x) == True:
            iddfs_path.reverse()
            for i in iddfs_path:
                print(i, end=" => ")
            return
    return ("No Path")


if __name__ == "__main__":
    g = n.Graph()
    g.add_edge('Oradea', 'Zerind', weight=71)
    g.add_edge('Oradea', 'Sibiu', weight=151)
    g.add_edge('Zerind', 'Arad', weight=75)
    g.add_edge('Arad', 'Sibiu', weight=140)
    g.add_edge('Arad', 'Timisoara', weight=118)
    g.add_edge('Timisoara', 'Lugoj', weight=111)
    g.add_edge('Lugoj', 'Mehadia', weight=70)
    g.add_edge('Mehadia', 'Drobeta', weight=75)
    g.add_edge('Drobeta', 'Craiova', weight=120)
    g.add_edge('Sibiu', 'Fagaras', weight=99)
    g.add_edge('Sibiu', 'Rimnicu Vilcea', weight=80)
    g.add_edge('Rimnicu Vilcea', 'Craiova', weight=146)
    g.add_edge('Craiova', 'Pitesti', weight=138)
    g.add_edge('Rimnicu Vilcea', 'Pitesti', weight=97)
    g.add_edge('Fagaras', 'Bucharest', weight=211)
    g.add_edge('Pitesti', 'Bucharest', weight=101)
    g.add_edge('Bucharest', 'Urziceni', weight=85)
    g.add_edge('Bucharest', 'Giurgiu', weight=90)
    g.add_edge('Urziceni', 'Hirsova', weight=98)
    g.add_edge('Hirsova', 'Eforie', weight=86)
    g.add_edge('Urziceni', 'Vaslui', weight=92)
    g.add_edge('Vaslui', 'Iasi', weight=92)
    g.add_edge('Iasi', 'Neamt', weight=87)
    source = 'Arad'
    destination = 'Bucharest'

    heuristics = {
        "Arad": 366,
        "Bucharest": 0,
        "Craiova": 160,
        "Drobeta": 242,
        "Eforie": 161,
        "Fagaras": 176,
        "Giurgiu": 77,
        "Hirsova": 151,
        "Iasi": 226,
        "Lugoj": 244,
        "Mehadia": 241,
        "Neamt": 234,
        "Oradea": 380,
        "Pitesti": 100,
        "Rimnicu Vilcea": 193,
        "Sibiu": 253,
        "Timisoara": 329,
        "Urziceni": 80,
        "Vaslui": 199,
        "Zerind": 374
    }

    lis = n.to_dict_of_dicts(g)
    print("==================== Breadth First Search ====================")
    bfs(lis, source, destination)
    print("\n\n==================== Uniform Cost Search ====================")
    ucs(lis, source, destination)
    print("\n\n==================== Greedy Best First Search ====================")
    greedy(lis, source, destination)
    print("\n============== Iterative Deepening Depth First Search ==============")
    run(source, destination, 10)

    if(c1 < c2 and c1 < c3):
        print("\nBreadth First Search Gives is the Least Cost.")
    elif(c2 < c1 and c2 < c3):
        print("\nUniform Cost Search Gives is the Least Cost.")
    else:
        print("\nGreedy Best First Search Gives is the Least Cost.")

    