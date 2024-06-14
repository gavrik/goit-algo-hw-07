from avl_tree import *

if __name__ == "__main__":
    rootAVL = None
    keys = [10,20,30,35,55,5,15,45,40,60,65,70,75]

    for key in keys:
        rootAVL = insert(rootAVL, key)

    #print(rootAVL)
    max_node = min_value_node(rootAVL)
    print("min node value: ", max_node.key)
    
