import copy
import numpy as np
import matplotlib.pyplot as plt


# Matrix for creating blank map
blankmap = np.zeros((301,401))

# Taking input from the user
def GetUserInput():
    global initial
    global finalNode

    # Taking x and y coordinates for start point
    while(True):
        print("Enter the co-ordinates of starting point separated by space (x,y) i.e x y:")
        initial = list(map(int, input().split()))
        if (len(initial)==2) and not(check_obstacles(initial)):
            break
        else:
            print("Please provide valid starting point")

    # Taking x and y coordinates for goal point
    while(True):
        print("Enter the co-ordinates of goal point separated by space  (x,y) i.e. x y : ")
        finalNode = list(map(int, input().split()))
        if len(finalNode)==2 and not(check_obstacles(finalNode)):
            break
        else:
             print("Please provide valid goal point")

# Defining function for generating map with obstacles
def Gen_map():
    Map = copy.deepcopy(blankmap)
    for x in range(401):
        for y in range(301):

            # considering circle as a obstacle
            if((x-90)**2 + (y-70)**2 <= 35**2):
                Map[300-y][x] = 1
                obs_x.append(x)
                obs_y.append(y)

            # considering ellipse as a obstacle
            if (((x - 246) ** 2) / (60 * 60) + ((y - 145) ** 2) / (30 * 30)) <= 1:
                Map[300-y][x] = 1
                obs_x.append(x)
                obs_y.append(y)

            # considering rectangle as a obstacle
            if (y - 0.7 * x - 74.4 >= 0) and (y - 0.7 * x - 90.8 <= 0) and (y + 1.43 * x - 176.64 >= 0) and (y + 1.43 * x - 438.64 <= 0):
                Map[300 - y][x] = 1
                obs_x.append(x)
                obs_y.append(y)

            # considering c-shape as a obstacle
            if (200 <= x <= 210 and 230 <= y <= 280) or (210 <= x <= 230 and 270 <= y <= 280) or (210 <= x <= 230 and 230 <= y <= 240):
                Map[300 - y][x] = 1
                obs_x.append(x)
                obs_y.append(y)

            # Considering complex object as a obstacle
            if (y + (42 / 43) * x - (16485 / 43) >= 0) and (y - x + 265 >= 0) and (x <= 354) and (y - x + 180 <= 0) and (y + (7 / 29) * x - (6480 / 29) <= 0):
                Map[300 - y][x] = 1
                obs_x.append(x)
                obs_y.append(y)

            if (y - x + 265 >= 0) and (y - x + 216 <= 0) and (x >= 354) and (x <= 381):
                Map[300 - y][x] = 1
                obs_x.append(x)
                obs_y.append(y)
    return Map

# Function for creating the grid using plot functions
def Creategrid():
    plt.plot(grid[0],grid[1])
    plt.plot(initial[0], initial[1], "r+")
    plt.plot(finalNode[0], finalNode[1], "r+")
    plt.scatter(obs_x, obs_y, s=0.5, color = 'g')


# Function to check the node in obstacle space
def check_obstacles(Node):
    if(Map[300-Node[1]][Node[0]]) == 1:
        return True
    else:
        return False

# Defining functions for the movements in 8 directions
def move_up(curr_node):
    if curr_node[1] < grid[1] :
        newnode = copy.deepcopy(curr_node)
        newnode[1]  = curr_node[1] + 1
        return newnode

def move_down(curr_node):
    if curr_node[1] > 0 :
        newnode = copy.deepcopy(curr_node)
        newnode[1]  = curr_node[1] - 1
        return newnode

def move_left(curr_node):
    if curr_node[0] > 0:
        newnode = copy.deepcopy(curr_node)
        newnode[0] = curr_node[0] - 1
        return newnode

def move_right(curr_node):
    if curr_node[0] < grid[0] :
        newnode = copy.deepcopy(curr_node)
        newnode[0]  = curr_node[0] + 1
        return newnode

def move_upleft(curr_node):
    if (curr_node[0] > 0) and (curr_node[1] < grid[1]):
        newnode = copy.deepcopy(curr_node)
        newnode[0],newnode[1]  = curr_node[0] - 1 , curr_node[1]+1
        return newnode

def move_upright(curr_node):
    if (curr_node[0] < grid[0]) and (curr_node[1] < grid[1]):
        newnode = copy.deepcopy(curr_node)
        newnode[0],newnode[1]= curr_node[0] + 1 , curr_node[1]+1
        return newnode

def move_downleft(curr_node):
    if (curr_node[0] > 0) and (curr_node[1] > 0):
        newnode = copy.deepcopy(curr_node)
        newnode[0],newnode[1] = curr_node[0] - 1 , curr_node[1]-1
        return newnode

def move_downright(curr_node):
    if (curr_node[0] < grid[0]) and (curr_node[1] > 0) :
        newnode = copy.deepcopy(curr_node)
        newnode[0],newnode[1] = curr_node[0] + 1 , curr_node[1]-1
        return newnode


# Function to check the validity of node and add it to the list
def Checknode(newnode):
    global Map
    global curr_nodeIndex
    global curr_node

    if (Map[300-newnode[1]][newnode[0]]) != 1:
        node.append(newnode)
        P_nodeIndex.append(curr_nodeIndex)
        Map[300-newnode[1]][newnode[0]] = 1

# Function for generating the path for current nodes
def Generatepath(curr_node):
    global curr_nodeIndex
    path.append(curr_nodeIndex)
    while(path[0] != 0):
        path.insert(0,P_nodeIndex[node.index(curr_node)])
        curr_node = node[path[0]]
    for i in range(len(path)):
        Nodepath.append(node[path[i]])

# Function for exploring the possible nodes using BFS
def BFS(InitialNode):
    global initial
    global finalNode
    global curr_node
    global curr_nodeIndex
    global Map
    curr_node = copy.deepcopy(InitialNode)
    node.append(curr_node)
    P_nodeIndex.append(curr_nodeIndex)
    pointX = []
    pointY = []

    # Creating the loop for generating possible moves
    while(((curr_node[0] != finalNode[0]) or (curr_node[1] != finalNode[1]))):
        if(move_left(curr_node) is not None):
            Checknode(move_left(curr_node))
        if(move_right(curr_node) is not None):
            Checknode(move_right(curr_node))
        if(move_up(curr_node) is not None):
            Checknode(move_up(curr_node))
        if(move_down(curr_node) is not None):
            Checknode(move_down(curr_node))
        if(move_upleft(curr_node) is not None):
            Checknode(move_upleft(curr_node))
        if(move_upright(curr_node) is not None):
            Checknode(move_upright(curr_node))
        if(move_downleft(curr_node) is not None):
            Checknode(move_downleft(curr_node))
        if(move_downright(curr_node) is not None):
            Checknode(move_downright(curr_node))

        pointX.append(curr_node[0])
        pointY.append(curr_node[1])
        curr_nodeIndex += 1
        curr_node = node[curr_nodeIndex]

        # To make visualization faster while exploring nodes
        if(len(pointX)%3000 == 0):
            plt.plot(pointX, pointY, '.k')
            plt.pause(0.001)
    return curr_node

# All necessary lists are defined here
grid = [400, 300]
finalNode = []
initial = []
obs_x = []
obs_y = []
node = []
curr_node = []
curr_nodeIndex = 0
P_nodeIndex = []
path = []
Nodepath = []

# Calling function to generate the map
Map = Gen_map()

# Taking input from the user
GetUserInput()

# Creating the grid after considering the obstacles
Creategrid()
print("Searching the path")
finalNode = BFS(initial)

if (finalNode != False):
    Generatepath(finalNode)
    pathX = [x[0] for x in Nodepath]
    pathY = [x[1] for x in Nodepath]
    print("Path Found")
    plt.plot(pathX,pathY,'r',linewidth = 1)
    plt.show()
else:
    print("No Path found")
