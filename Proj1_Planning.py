
import numpy as np
import time

m = int(input("Enter number of Rows: "))
n = int(input("Enter number of columns: "))
Mat = []
for i in range(0, n):
    Mat.append([])
for i in range(0, m):
    for j in range(0,n):
        Mat[i].append(j)
        Mat[i][j] = 0
for i in range(0, m):
    for j in range(0, n):
        print('Entry in row', i+1, 'column', j+1)
        Mat[i][j] = int(input())
mat = np.array(Mat)


print("Starting the program: \n")

Nodes = []
# Node_Init=np.array([[1, 2, 3], [4, 0, 5], [6, 7, 8]])
Node_Init = np.array(Mat)
Nodes.append(Node_Init)

Nodes_Info = []

Nodes_Info_Init = [1, 0, 0]
Nodes_Info.append(Nodes_Info_Init)

Node_Goal = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])


count_Nodes = 0
cost_to_come = 1

start = time.time()


def get_blank_location(node):
    row, column = np.where(node == 0)
    return row, column


def add_node(current_node):
    added = False
    if np.any([(current_node == x).all() for x in Nodes]):
        added = False
    else:
        added = True
        Nodes.append(current_node)
    return added


def action_move_right(current_node):
    status = False
    temp_node = current_node.copy()
    row = np.where(current_node == 0)[0]
    column = np.where(current_node == 0)[1]
    if column == 2:
        status = False
    else:
        status = True
        # print("Performing Action: Right")
        zero = temp_node[row, column]
        temp_node[row, column] = current_node[row, column + 1]
        temp_node[row, column + 1] = zero

    return status, temp_node


def action_move_left(current_node):
    status = False
    temp_node = current_node.copy()
    row = np.where(current_node == 0)[0]
    column = np.where(current_node == 0)[1]
    if column == 0:
        status = False
    else:
        status = True
        # print("Performing Action: Left")
        zero = temp_node[row, column]
        temp_node[row, column] = temp_node[row, column - 1]
        temp_node[row, column - 1] = zero

    return status, temp_node


def action_move_up(current_node):
    status = False
    temp_node = current_node.copy()
    row = np.where(current_node == 0)[0]
    column = np.where(current_node == 0)[1]
    if row == 0:
        status = False
    else:
        status = True
        # print("Performing Action: Up")
        zero = temp_node[row, column]
        temp_node[row, column] = temp_node[row - 1, column]
        temp_node[row - 1, column] = zero

    return status, temp_node


def action_move_down(current_node):
    status = False
    temp_node = current_node.copy()
    row = np.where(current_node == 0)[0]
    column = np.where(current_node == 0)[1]
    if row == 2:
        status = False
    else:
        status = True
        # print("Performing Action: Down")
        zero = temp_node[row, column]
        temp_node[row, column] = temp_node[row + 1, column]
        temp_node[row + 1, column] = zero

    return status, temp_node


count_layer = 0
count_sub_nodes = 1

while count_Nodes < len(Nodes):                       # Length nodes

    r, c = get_blank_location(Nodes[count_Nodes])

    stat2, req_node2 = action_move_up(Nodes[count_Nodes])
    if stat2 is True:
        add = add_node(req_node2)                     # Add is the return value from add_node function

        if add is True:
            count_sub_nodes += 1
            Nodes_Info.append([count_sub_nodes, count_Nodes+1, cost_to_come])
        if np.array_equal(req_node2, Node_Goal):
            break

    stat, req_node = action_move_right(Nodes[count_Nodes])
    if stat is True:
        add = add_node(req_node)

        if add is True:
            count_sub_nodes += 1
            Nodes_Info.append([count_sub_nodes, count_Nodes + 1, cost_to_come])
        if np.array_equal(req_node, Node_Goal):
            break

    stat1, req_node1 = action_move_left(Nodes[count_Nodes])
    if stat1 is True:
        add = add_node(req_node1)

        if add is True:
            count_sub_nodes += 1
            Nodes_Info.append([count_sub_nodes, count_Nodes + 1, cost_to_come])
        if np.array_equal(req_node1, Node_Goal):
            break

    stat3, req_node3 = action_move_down(Nodes[count_Nodes])
    if stat3 is True:
        add = add_node(req_node3)

        if add is True:
            count_sub_nodes += 1
            Nodes_Info.append([count_sub_nodes, count_Nodes+1, cost_to_come])
        if np.array_equal(req_node3, Node_Goal):
            break

    if Nodes_Info[count_Nodes + 1][1] != Nodes_Info[count_Nodes][1]:    # To check if nodes in same level
        cost_to_come += 1

    count_Nodes += 1


# print("All Nodes :", Nodes)
print("Total Number of nodes explored: ", len(Nodes))
# print("Nodes information: ", Nodes_Info)
print("Length of nodes information array:", len(Nodes_Info))


# Code for back-tracking
l = len(Nodes_Info)
Node_No = []
Paren_No = []

for i in range(l):
    Node_No.append(Nodes_Info[i][0])
    Paren_No.append(Nodes_Info[i][1])

required_index = [l-1]
pointer = l-1
i = 0
while i != 1:
    i = Node_No[pointer]        # Last Node's Number
    # i = x
    p = Paren_No[pointer]       # Last Node's Parent No.
    if Node_No.index(p) != 0:
        required_index.append(Node_No.index(p))
        pointer = Node_No.index(p)
    else:
        break

required_index.append(0)        # The root node is obvious, if the path exists
required_index.reverse()

Nodes_Path = []                     # The 3D Array storing the nodes for the path

print("Req.indexes for path:", required_index)
# Finding the nodes
for c in required_index:
    Nodes_Path.append(Nodes[c])
    print("The path is: \n", Nodes[c])

# print("Node_No:", Node_No)
# print("Paren_No: ", Paren_No)
# print(Nodes_Info[Node_No.index(3)])
# print("Corr Node", Nodes[Node_No.index(3)])


end = time.time()
print("Time elapsed:", end-start)


# For all nodes
file = open("Nodes_explored.txt","w")
for a in Nodes:
    for col in range(3):
        for ro in range(3):
            file.write("%i\t" % a[ro][col])
    file.write("\n")
file.close()

# For all the nodes information
file = open("Nodes_Information.txt","w")
for a in Nodes_Info:
    for ro in range(3):
        file.write("%i\t" % a[ro])
    file.write("\n")
file.close()


# For the nodes in path
file = open("Nodes_Path.txt", "w")
for a in Nodes_Path:
    for col in range(3):
        for ro in range(3):
            file.write("%i\t" % a[ro][col])
    file.write("\n")
file.close()











# Nodes=[]
# Node_Init=np.array([[1, 2, 3], [4, 0, 5], [6, 7, 8]])
# Node_Goal = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
# Nodes.append(Node_Init)
# Nodes.append(Node_Goal)
#
# file = open("file_nodes.txt","w")
# for a in Nodes:
#     for column in range(3):
#         for row in range(3):
#             file.write("%i\t" % a[row][column])
#     file.write("\n")
# file.close()
#
# # For all nodes
# file = open("Nodes_explored.txt","w")
# for a in Nodes:
#     for column in range(3):
#         for row in range(3):
#             file.write("%i\t" % a[row][column])
#     file.write("\n")
# file.close()
#
# # For all the nodes information
# file = open("Nodes_Information.txt","w")
# for a in Nodes_Info:
#     for column in range(3):
#         for row in range(3):
#             file.write("%i\t" % a[row][column])
#     file.write("\n")
# file.close()
#
#
# # For the nodes in path
# file = open("Nodes_Path.txt","w")
# for a in Nodes_Path:
#     for column in range(3):
#         for row in range(3):
#             file.write("%i\t" % a[row][column])
#     file.write("\n")
# file.close()