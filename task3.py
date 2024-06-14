from avl_tree import *

sum_values = 0

def sum_nodes(node):
    global sum_values
    if node:
        sum_nodes(node.left)
        sum_nodes(node.right)
        #print(node.key)
        sum_values += node.key
    return sum_values

if __name__ == "__main__":
    rootAVL = None
    keys = [10,20,30,35,55,5,15,45,40,60,65,70,75]
    #print(sum(keys))
    for key in keys:
        rootAVL = insert(rootAVL, key)

    #print(rootAVL)
    print("Sum of nodes: ", sum_nodes(rootAVL))

