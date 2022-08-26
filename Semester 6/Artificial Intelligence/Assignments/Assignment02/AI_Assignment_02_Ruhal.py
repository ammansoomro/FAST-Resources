
graph = {
"arad": {"zer":75,"tim":118,"sib":140},
"zer": {"ora":71,"arad":75},
"tim": {"lug":111,"arad" : 118},
"sib": {"ora":151,"faga":99,"rimVil":80,"arad": 140},
"lug": {"meh":70,"tim": 111},
"ora" : {"sib":151,"zer": 71},
"faga" : {"sib": 99,"buch":211},
"rimVil" : {"pit":97,"cra":146,"sib": 80},
"meh" : {"dro":75,"lug": 70},
"pit" : {"buch":101,"rimVil":146,"cra":138},
"cra" : {"pit":138,"rimVil":146,"dro":120},
"dro" : {"cra":120,"meh":75},
"buch" : {"pit":101,"faga":211,"urz":85,"giug":90},
"giug" : {"buch":90},
"urz" : {"buch" : 85,"vas":142,"ili":98},
"vas" : {"lasi":92,"urz":142},
"ili" : {"efo":86,"urz":98},
"efo" : {"ili":86},
"lasi" : {"nea":87,"vas":92},
"nea" : {"lasi": 87}
}

husristics = {'arad': 366, 'zer': 374, 'tim': 329, 'sib': 253, 'lug': 244, 'ora': 380,
              'faga': 178, 'rimVil': 193, 'meh': 241, 'pit': 98, 'cra': 160, 'dro': 242, 'buch': 0,
              'giug': 77, 'urz': 80, 'vas': 199, 'ili': 151, 'efo': 161, 'lasi': 226, 'nea': 234}

class node:
    def __init__(self,source,destination,cost):
        self.parent = source
        self.child  = destination
        self.pathCost = cost

def bfs(graph,source,destination):
    queue = []
    visited = []
    order_cost = 0
    path_way = []
    queue.append(source)
    visited.append(source)
    parent = source
    index = 0
    count = 0
    while queue:
        source = queue.pop(0)
        path_way.append(source)
        child_list = list(graph[source].keys())
        if source != parent:
            # this is for the same child which is already present in the result set
            if source not in list(graph[parent].keys()):
                index = index + 1
                parent = path_way[index]
            #this tell the index of the child(key) of particular parent by which we can calculate the path_order cost

            if source not in list(graph[parent].keys()):
                index = index + 1
                parent = path_way[index]

            count = list(graph[parent].keys()).index(source)
            if count < len(graph[parent]):
                order_cost = order_cost + graph[parent][source]
                if count == len(graph[parent])-1:
                    index = index + 1
                    parent = path_way[index]
                    count = 0
        if source == destination:
            break
        for j in child_list:
            if j not in visited:
                visited.append(j)
                queue.append(j)
    print(path_way)
    print("Path Cost is: ", end=' ')
    print(order_cost)

def setPriorityQueue(queue,node):
    if len(queue) == 0:
        queue.append(node)
        return queue
    else:
        queue.append(node)
        for i in range(len(queue) - 1):
            for j in range(i + 1, len(queue)):
                if queue[i].pathCost > queue[j].pathCost:  # compare and then swap nodes
                    temp = queue[i].pathCost
                    queue[i].pathCost = queue[j].pathCost
                    queue[j].pathCost = temp

                    temp = queue[i].parent
                    queue[i].parent = queue[j].parent
                    queue[j].parent = temp

                    temp = queue[i].child
                    queue[i].child = queue[j].child
                    queue[j].child = temp


    return queue

def convertListToString(result):
    str1 = " "
    for i in result:
        str1 += str(i) + ""
    return str1

def ucs(graph,src,destination):
    priorityQueue = []
    visited = []
    order_cost = 0
    parent = {}
    path_way = []
    root = node(src,src,0)
    priorityQueue.append(root)
    visited.append(src)
    # parent = root.parent
    while priorityQueue:
        source = priorityQueue.pop(0)
        child_list = list(graph[source.child].keys())
        for j in child_list:
            if j not in visited:
                visited.append(j)


                if source.parent != source.child:
                    temp_cost = graph[source.parent][source.child]+graph[source.child][j]
                else:
                    temp_cost = graph[source.child][j]

                graph[source.child][j] = temp_cost
                parent[j] = [source.child]

                new_child = node(source.child, j, temp_cost)
                priorityQueue = setPriorityQueue(priorityQueue, new_child)

            else:
                for i in priorityQueue:
                    if i.child == j:
                        temp_list = []
                        for k in list(graph.keys()):
                            if j in list(graph[k].keys()):
                                if source.child != k:
                                    if graph[k][j] >= (graph[source.parent][source.child] + graph[source.child][j]):
                                        graph[source.child][j] = (graph[source.parent][source.child] + graph[source.child][j])
                                        parent[j] = [source.child]
                                        if j == destination:
                                            path_way.append(j)
                                            temp = j
                                            while 1:
                                                if temp == src:
                                                    break
                                                temp = convertListToString(parent[temp])
                                                temp = temp[1:len(temp)]
                                                path_way.append(temp)

                                        path_way.reverse()
                                        print(path_way)
                                        print("Path Cost is =",end=" ")
                                        print(graph[source.child][j])


def calcCostFromPath(graph,result_set):
    path_cost = 0
    for i in range(len(result_set)-1):
        path_cost += graph[result_set[i]][result_set[i+1]]
    return path_cost

def greedyAlgorithm(graph,husristics,source,destination):
    result_set = []
    visited = []
    path_cost = 0
    result_set.append(source)
    visited.append(source)
    while 1:
        if source == destination:
            break
        lower_hur = 99999
        for i in list(graph[source].keys()):
            if lower_hur > husristics[i] and i not in visited:
                visited.append(i)
                lower_hur = husristics[i]
                source = i
        result_set.append(source)

    path_cost = calcCostFromPath(graph,result_set)
    print(result_set)
    print("Path Cost is: ", end=' ')
    print(path_cost)


iddfs_cost = 0
iddfs_path = []


def DepthLimited(src, dest, limit):
    if src == dest:
        iddfs_path.append(src)
        return True

    if limit < 0:
        return False

    for neighbour in graph[src]:
        if DepthLimited(neighbour, dest, limit - 1):
            iddfs_path.append(src)
            return True

    return False


def IDDFS(src, dest, limit):
    for x in range(limit):
        if DepthLimited(src, dest, x) == True:
            iddfs_path.reverse()
            print(iddfs_path)
            print("Path Cost is: ",end=' ')
            print(calcCostFromPath(graph,iddfs_path))
            return
    return ("Path not found")



print("ucs")
ucs(graph,"arad","nea")
print("Greedy Best first search")
greedyAlgorithm(graph,husristics,"arad","nea")
print("bfs")
bfs(graph,"arad","nea")
print("IDDFS")
IDDFS('arad', 'nea', 5)
print("UCS performs better than all algorithms")

