from queue import PriorityQueue


def get_cost(cost, current, next):
    return cost[(current, next)]


# uniform cost search
def uniform_cost_search(graph, start, goal, cost):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
        for next in graph[current]:
            new_cost = cost_so_far[current] + get_cost(cost, current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current
    return came_from, cost_so_far


def breadth_first_search(graph, start, goal):
    frontier = [start]
    came_from = {}
    came_from[start] = None
    while frontier:
        current = frontier.pop(0)
        if current == goal:
            break
        for next in graph[current]:
            if next not in came_from:
                frontier.append(next)
                came_from[next] = current
    return came_from


def best_first_search(graph, start, goal, heuristic):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
        for next in graph[current]:
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic[next]
                frontier.put(next, priority)
                came_from[next] = current
    return came_from, cost_so_far

def depth_limited_search(graph, start, goal, limit,path):

    frontier = [start]
    came_from = {}
    came_from[start] = None
    while frontier:
        current = frontier.pop(len(frontier)-1)
        path.append(current)
        if current == goal[0]:
            return path
        if limit == 0:
            return False
        for next in graph[current]:
            if next not in came_from:
                frontier.append(next)
                came_from[next] = current
        limit -= 1
    return False

def iterative_deepening_search(graph, start, goal):
    for depth in range(1, 50):
        path = []
        if depth_limited_search(graph, start, goal, depth,path):
            return path
    return False



algorithms = []

graph,cost=[[] for i in range(20)],{}

cities={
    0:'Arad',
    1:'Zerind',
    2:'Oradea',
    3:'Sibiu',
    4:'Fagaras',
    5:'Rimnicu Vilcea',
    6:'Pitesti',
    7:'Timisoara',
    8:'Lugoj',
    9:'Mehadia',
    10:'Drobeta',
    11:'Craiova',
    12:'Bucharest',
    13:'Giurgiu',
    14:'Urziceni',
    15:'Hirsova',
    16:'Vaslui',
    17:'Iasi',
    18:'Neamt',
    19:'Eforie'
}

heuristic={
    0:366,
    1:374,
    2:380,
    3:253,
    4:176,
    5:193,
    6:100,
    7:329,
    8:244,
    9:241,
    10:242,
    11:160,
    12:0,
    13:77,
    14:80,
    15:151,
    16:199,
    17:226,
    18:234,
    19:161
}

graph[0].append(1)
graph[0].append(7)
graph[1].append(0)
graph[1].append(2)
graph[2].append(1)
graph[2].append(3)
graph[3].append(0)
graph[3].append(2)
graph[3].append(4)
graph[3].append(5)
graph[4].append(3)
graph[4].append(12)
graph[5].append(3)
graph[5].append(6)
graph[5].append(11)
graph[6].append(5)
graph[6].append(11)
graph[6].append(12)
graph[7].append(0)
graph[7].append(8)
graph[8].append(7)
graph[8].append(9)
graph[9].append(8)
graph[9].append(10)
graph[10].append(9)
graph[10].append(11)
graph[11].append(5)
graph[11].append(10)
graph[11].append(6)
graph[12].append(13)
graph[12].append(14)
graph[12].append(4)
graph[12].append(6)
graph[13].append(12)
graph[14].append(12)
graph[14].append(15)
graph[14].append(16)
graph[15].append(14)
graph[15].append(19)
graph[16].append(14)
graph[16].append(17)
graph[17].append(16)
graph[17].append(18)
graph[18].append(17)
graph[19].append(15)

cost[(0,1)] = 75
cost[(0,7)] = 118
cost[(0,3)] = 140
cost[(1,0)] = 75
cost[(1,2)] = 71
cost[(2,1)] = 71
cost[(2,3)] = 151
cost[(3,0)] = 140
cost[(3,2)] = 151
cost[(3,4)] = 99
cost[(3,5)] = 80
cost[(4,3)] = 99
cost[(4,12)] = 211
cost[(5,3)] = 80
cost[(5,6)] = 97
cost[(5,11)] = 146
cost[(6,5)] = 97
cost[(6,11)] = 138
cost[(6,12)] = 101
cost[(7,0)] = 118
cost[(7,8)] = 111
cost[(8,7)] = 111
cost[(8,9)] = 70
cost[(9,8)] = 70
cost[(9,10)] = 75
cost[(10,9)] = 75
cost[(10,11)] = 120
cost[(11,5)] = 146
cost[(11,10)] = 120
cost[(11,6)] = 138
cost[(12,4)] = 211
cost[(12,6)] = 101
cost[(12,13)] = 90
cost[(12,14)] = 85
cost[(13,12)] = 90
cost[(14,12)] = 85
cost[(14,15)] = 98
cost[(14,16)] = 142
cost[(15,14)] = 98
cost[(15,19)] = 86
cost[(16,14)] = 142
cost[(16,17)] = 92
cost[(17,16)] = 92
cost[(17,18)] = 87
cost[(18,17)] = 87
cost[(19,15)] = 86

s=input("Enter the starting city: ")
g=input("Enter the goal city: ")


goal_city=0
start_city=0

for key,value in cities.items():
    if value==s:
        start_city=key
    if value==g:
        goal_city=key

goal=[]
goal.append(goal_city)


answer=iterative_deepening_search(graph,start_city,goal)


temp=[]
temp.append("Iterative Deepening search")

string=""
for city in answer[:-1]:
    string+=cities[city]+" --> "
string+=cities[answer[-1]]
temp.append(string)

c=0
for i in range(len(answer)-1):
    c+=cost[(answer[i],answer[i+1])]

temp.append(c)


algorithms.append(temp)
temp=[]

answer=uniform_cost_search(graph,start_city,goal,cost)

#print the answer
so_far=goal_city
ans=[]
while(so_far!=start_city):
    ans.append(cities[so_far])
    so_far=answer[0][so_far]

#print ans in reverse order
ans.reverse()
temp.append("Uniform cost search: ")
string=cities[start_city]+" --> "
for city in ans[:-1]:
    string+=city+" --> "

string+=ans[-1]
temp.append(string)

#print the cost
temp.append(answer[start_city+1][goal_city])
algorithms.append(temp)
temp=[]


answer=breadth_first_search(graph,start_city,goal)

#print the answer
so_far=goal_city
ans=[]
c=0
while(so_far!=start_city):
    ans.append(cities[so_far])
    c += cost[(so_far, answer[so_far])]
    so_far=answer[so_far]

#print ans in reverse order
ans.reverse()
temp.append("Breadth First search: ")
string=cities[start_city]+" --> "
for city in ans[:-1]:
    string+=city+" --> "

string+=ans[-1]
temp.append(string)

#print the cost
temp.append(c)

algorithms.append(temp)
temp=[]



answer=best_first_search(graph,start_city,goal,heuristic)

#print the answer
so_far=12
ans=[]
c=0
while(so_far!=0):
    ans.append(cities[so_far])
    c += cost[(so_far, answer[0][so_far])]
    so_far=answer[0][so_far]

#print ans in reverse order
ans.reverse()
temp.append("Best first search: ")
string=cities[start_city]+" --> "
for city in ans[:-1]:
    string += city + " --> "

string+=ans[-1]
temp.append(string)
temp.append(c)

algorithms.append(temp)

n=len(algorithms)
for i in range(n):
    for j in range(n-1-i):
        if algorithms[j][-1]>algorithms[j+1][-1]:
            temp=algorithms[j][-1]
            algorithms[j][-1]=algorithms[j+1][-1]
            algorithms[j + 1][-1]=temp


for i in algorithms:
    print("Algorithm: ",i[0])
    print("Path: ",i[1])
    print("Cost: ", i[2])
    print()