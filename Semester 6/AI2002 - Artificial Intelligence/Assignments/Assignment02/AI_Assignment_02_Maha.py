def BestFirstSearch(start_node, goal_node):
  print("Path for Best First Search: ")
  visited=[]
  queue= PriorityQueue()
  queue.put((0, start_node))
  pathcost = 0
  start = start_node
  while not queue.empty():
    item=queue.get()
    
    start_node = item[1]
    if start_node == goal_node:
      pathcost = pathcost + H_dist[start_node]
      print(start_node)
      queue.queue.clear()
      return pathcost;
    else:
      if start_node in visited:
        continue
      print(start_node,end=' -> ')
      if(start!=start_node):
        pathcost = pathcost + H_dist[start_node]
      visited.append(start_node)
      for neighbor in graph[start_node]:
        queue.put((H_dist[neighbor[1]], neighbor[1]))


from collections import defaultdict
from queue import PriorityQueue
def UCS(start_node, goal_node):
  print("Path for Uniform Cost Search:")
  visited=[]
  queue= PriorityQueue()
  queue.put((0,start_node,[start_node]))
  while not queue.empty():
    item=queue.get()
    start_node=item[1]
    if start_node == goal_node:
      for node in item[2]:
        if node == item[2][len(item[2])-1]:
          print(node)
        else:
          print(node,end = " -> ")
      queue.queue.clear()
      return item[0]
    else:
      if start_node not in visited:
        visited.append(start_node)
        for neighbor in graph[start_node]:
          path1 = []
          path1 = list(item[2])
          path1.append(neighbor[1])
          queue.put((neighbor[0]+item[0],neighbor[1],path1))


def bfs(node,goal_node): #function for BFS
  print("Path for Breadth First Search:")  
  queue = []
  visited = []
  path_cost = 0
  visited.append(node)
  queue.append((0,node))
  while queue:         
      m = queue.pop(0) 
      path_cost = path_cost+ m[0]
      if (m[1]==goal_node):
        print (m[1])
        return path_cost
      print (m[1], end = " --> ")
      for neighbour in graph[m[1]]:
          if neighbour[1] not in visited:
              visited.append(neighbour[1])
              queue.append(neighbour)


graph = {
  'ZERIND': [(75,'ARAD'),(71,'ORADEA')],
  'ARAD': [(118,'TIMISOARA'),(75,'ZERIND'),(140,'SIBIU')],
  'ORADEA': [(71,'ZERIND'),(151,'SIBIU')],
  'TIMISOARA':[(111,'LUGOJ'),(118,'ARAD')],
  'SIBIU':[(140,'ARAD'),(151,'ORADEA'),(99,'FAGARAS'),(80,'RIMNICU VILCEA')],
  'LUGOJ':[(111,'TIMISOARA'),(70,'MEHADIA')],
  'MEHADIA':[(70,'LUGOJ'),(75,'DROBETA')],
  'DROBETA':[(75,'MEHADIA'),(120,'CRAIOVA')],
  'CRAIOVA':[(120,'DROBETA'),(146,'RIMNICU VILCEA'),(138,'PITESTI')],
  'RIMNICU VILCEA':[(80,'SIBIU'),(146,'CRAIOVA'),(97,'PITESTI')],
  'FAGARAS':[(99,'SIBIU'),(211,'BUCHAREST')],
  'PITESTI':[(97,'RIMNICU VILCEA'),(138,'CRAIOVA'),(101,'BUCHAREST')],
  'BUCHAREST':[(101,'PITESTI'),(211,'FAGARAS'),(90,'GIURGIU'),(85,'URZICENI')],
  'GIURGIU':[(90,'BUCHAREST')],
  'URZICENI':[(85,'BUCHAREST'),(98,'HIRSOVA'),(142,'VASLUI')],
  'HIRSOVA':[(98,'URZICENI'),(86,'EFORIE')],
  'EFORIE':[(86,'HIRSOVA')],
  'VASLUI':[(142,'URZICENI'),(92,'LASI')],
  'LASI':[(92,'VASLUI'),(87,'NEAMT')],
  'NEAMT':[(87,'LASI')]

}

H_dist = {
            'ZERIND': 374,
            'ARAD': 366,
            'ORADEA': 380,
            'TIMISOARA':329,
            'SIBIU':253,
            'LUGOJ':244,
            'MEHADIA':241,
            'DROBETA':242,
            'CRAIOVA':160,
            'RIMNICU VILCEA':193,
            'FAGARAS':176,
            'PITESTI':100,
            'BUCHAREST':0,
            'GIURGIU':77,
            'URZICENI':80,
            'HIRSOVA':151,
            'EFORIE':161,
            'VASLUI':199,
            'LASI':226,
            'NEAMT':234
        }


start_node = input("Enter Start Node:   ")
start_node = start_node.upper()
goal_node = input("Enter goal node:  ")
goal_node = goal_node.upper()
pathcosts = []
visited2 = []
pathcost = 0
pathcosts.append((bfs(start_node,goal_node),"Breadth First Search: "))
print()
pathcosts.append((UCS(start_node,goal_node),"Uniform Cost Search:"))
print()
pathcosts.append((BestFirstSearch(start_node,goal_node),"Best First Search: "))
print()
pathcosts.sort()
print()
print("Path Costs: ")
print()
for i in pathcosts:
  print(i[1],i[0])