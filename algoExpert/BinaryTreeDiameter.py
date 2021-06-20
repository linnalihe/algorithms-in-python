# Binary Tree Diameter

# Write function that takes Binary Tree and returns diameter
# diameter is the longest path and a path is defined as a collection of connected noes in a tree where no doe is connected to more than two other nodes

# Initial thoughts:

# function that takes binary tree and returns diameter
# diameter is the length of it's longest path
# path is the number of edges between the path's first node and it's last

# tree  =          1
#			     /   \
#				3     2
#             /  \
#			7      4
#         /          \
#        8            5
# longest path is 8 -> 7 -> 3 -> 4 -> 5

# have to keep track of the longest path
# output is the longest path
# brute force: from each node, calculate the number of edges in the collection
# this is order of O(N^2) because you check each node and for each node you have
# to iterate through all the connected node.
# optimization: start out at the top and check left until leaf, check right until leaf
# store the length of the right for the right child, store the left for the left child
# so that the children only have to find the length of the opposite path

# check 1 and length of right is 1, length of left is 4 so 5
# for the left child 3, length is 4 - 1 = 3, for right child, length is 1 -1 =0
# check 3, if value is stored, get value + length of right. store for 7 left length is 3 - 1 = 2
#															store for 4 right length is 3 - 1 = 2

# recursively? or iteratively?
# recursivley: keep calling left child + right child
# iteratively: for each node, while next is not null, keep going down right and keep going down left
