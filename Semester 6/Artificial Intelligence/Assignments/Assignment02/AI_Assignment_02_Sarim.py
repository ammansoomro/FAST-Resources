from queue import PriorityQueue
import networkx as nx

from numpy import source

graph=nx.Graph()

graph.add_edge('Craiova','Pitesti',weight=138)
graph.add_edge('Rimnicu Vilcea','Pitesti',weight=97)
graph.add_edge('Fagaras','Bucharest',weight=211)
graph.add_edge('Urziceni','Vaslui',weight=92)
graph.add_edge('Vaslui','Iasi',weight=92)
graph.add_edge('Iasi','Neamt',weight=87)
graph.add_edge('Pitesti','Bucharest',weight=101)
graph.add_edge('Bucharest','Urziceni',weight=85)
graph.add_edge('Timisoara','Lugoj',weight=111)
graph.add_edge('Lugoj','Mehadia',weight=70)
graph.add_edge('Bucharest','Giurgiu',weight=90)
graph.add_edge('Oradea','Zerind',weight=71)
graph.add_edge('Oradea','Sibiu',weight=151)
graph.add_edge('Zerind','Arad',weight=75)
graph.add_edge('Arad','Sibiu',weight=140)
graph.add_edge('Arad','Timisoara',weight=118)
graph.add_edge('Urziceni','Hirsova',weight=98)
graph.add_edge('Hirsova','Eforie',weight=86)
graph.add_edge('Mehadia','Drobeta',weight=75)
graph.add_edge('Drobeta','Craiova',weight=120)
graph.add_edge('Sibiu','Fagaras',weight=99)
graph.add_edge('Sibiu','Rimnicu Vilcea',weight=80)
graph.add_edge('Rimnicu Vilcea','Craiova',weight=146)

values={
    'Arad':366,
    'Bucharest':0,
    'Craiova':160,
    'Drobeta':242,
    'Eforie':161,
    'Fagaras':176,
    'Giurgiu':77,
    'Hirsova':151,
    'Iasi':226,
    'Lugoj':244,
    'Mehadia':241,
    'Neamt':234,
    'Oradea':380,
    'Pitesti':100,
    'Rimnicu Vilcea':193,
    'Sibiu':253,
    'Timisoara':329,
    'Urziceni':80,
    'Vaslui':199,
    'Zerind':374
}

sourcecity=input("Enter Source City: ")
destinationcity=input("Enter Destination City: ")

while sourcecity not in values:
    print("")
    sourcecity=input("Re-Enter Source City: ")

while destinationcity not in values:
    print("")
    destinationcity=input("Re-Enter Destination city: ")

dict=nx.to_dict_of_dicts(graph)

#BFS
print(" ")

bfscost={sourcecity:0}
bfsparent={sourcecity:None}
bfsvisitedcities=[]
bfsqueuecities=[]

bfsvisitedcities.append(sourcecity)
bfsqueuecities.append(sourcecity)

while bfsqueuecities:
    curr=bfsqueuecities.pop(0)
    # if curr!=destinationcity:
    #     print(curr,end="->")
    for adjacent in dict[curr]:
        if adjacent not in bfsvisitedcities:
            bfsvisitedcities.append(adjacent)
            bfsqueuecities.append(adjacent)

            bfscost[adjacent]=bfscost[curr]+dict[curr][adjacent]['weight']
    
    if curr==destinationcity:
        # print(curr)
        print("BFS Cost: ",bfscost[destinationcity])

#UCS

ucscost=0
ucsvisitedcities=[]
ucsqueuecities=PriorityQueue()

ucsqueuecities.put((0,sourcecity))
ucsparent={sourcecity:None}
print(" ")
while ucsqueuecities:
    actcost,curr=ucsqueuecities.get()

    if curr not in ucsvisitedcities:
        ucsvisitedcities.append(curr)

        if curr==destinationcity:
            ucscost=actcost
            break
        for adjacent in dict[curr]:
            if adjacent not in ucsvisitedcities:
                ucscost=actcost+dict[curr][adjacent]['weight']
                ucsqueuecities.put((ucscost,adjacent))
                ucsparent[adjacent]=curr

print("UCS Cost: ",ucscost)



#GBFS

gbfscost=0
gbfsvisited=[]

gbfsqueuecities=PriorityQueue()
gbfsqueuecities.put((0,sourcecity))

while gbfsqueuecities:
    bctcost,curr=gbfsqueuecities.get()
    gbfscost+=bctcost

    if curr==destinationcity:
        break

    else:
        for adjacent in dict[curr]:
            if adjacent not in gbfsvisited:
                gbfsvisited.append(adjacent)
                gbfsqueuecities.put((values[adjacent],adjacent))
print(" ")
print("GBFS Cost: ",gbfscost)

# IDDFS


#IDDFS

iddfscost=0
iddfsvisited=[]

def OutOfDepth(sourcecity,destinationcity,depth):
    for i in range(depth):
        if OutOfDepth(sourcecity,destinationcity,i)==True:
            iddfsvisited.reverse()



def Depth(sourcecity,destinationcity,depth):
    iddfsactcost=0
    
    if sourcecity==destinationcity:
        iddfsvisited.append(sourcecity)
        return True
    iddfsactcost+=10000
    if depth<0:
        return False
    for adjacent in dict[sourcecity]:
        if OutOfDepth(adjacent,destinationcity,depth-1):
            iddfsvisited.append(sourcecity)
            
    print(" ")
    
    print("IDDFS Cost: ",iddfsactcost)
    print(" ")
    return iddfsactcost

iddfscost=Depth(sourcecity,destinationcity,5)

if (bfscost[destinationcity]<=ucscost and bfscost[destinationcity]<=gbfscost and bfscost[destinationcity]<=iddfscost):
    print("BFS has lowest cost.")

elif (ucscost<=bfscost[destinationcity] and ucscost<=gbfscost and ucscost<=iddfscost):
    print("UCS has lowest cost.")

elif (gbfscost<=ucscost and gbfscost<=bfscost[destinationcity] and gbfscost<=iddfscost):
    print("GBFS has lowest cost.")

elif (iddfscost<=ucscost and iddfscost<=gbfscost and iddfscost<=bfscost[destinationcity]):
    print("IDDFS has lowest cost.")