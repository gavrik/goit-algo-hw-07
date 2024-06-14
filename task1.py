from avl_tree import *

def max_value_node(node):
    current = node
    while current.right is not None:
        current = current.right
    return current

if __name__ == "__main__":
    rootAVL = None
    keys = [10,20,30,35,55,5,15,45,40,60,65,70,75]

    for key in keys:
        rootAVL = insert(rootAVL, key)

    #print(rootAVL)
    max_node = max_value_node(rootAVL)
    print("max node value: ", max_node.key)
