"""
We have a quad-tree data structure where each node has a data field and 4 children.
The structure is constrained so that either the data value is present OR the 4 children, but not both!
Such structure can be used to efficiently represent a 2-D area map or image.

Assume a NxN grid of on/off pixels. The top level quad-tree node (root) represents this grid.
If all pixels in the grid are the same, then the root node has a data value and no children.
However, if the pixels are different, then divide the grid into 4 sections (quadrants) and use
the 4 children to represent each quadrant respectively.

1. Create a class with constructor to represent the QuadTreeNode data structure
2. Given a Root node and side dimension (N), write a function to reconstruct the image and return it as 2D array
   *Note:* For simplicity, assume the grid dimension is a power of 2 (i.e. N=2, 4, 8, 16, 32, etc...)

1 1
1 1
N=2, root node: {value=1, no children}

1 1
1 0
N=2, root node: {value=None, 
                               topLeft:  {value=1, no children}
                               topRight: {value=1, no children}
                               botLeft:  {value=1, no children}
                               botRight: {value=0, no children}
                             
1 1  1 1
1 1  1 1 

1 1  1 1
1 1  1 0
N=4, root node: {value=None,
                                topLeft:  {value=1, no children}
                                topRight: {value=1, no children}
                                botLeft:  {value=1, no children}
                                botRight: {value=None, 
                                                       topLeft:  {value=1, no children}
                                                       topRight: {value=1, no children}
                                                       botLeft:  {value=1, no children}
                                                       botRight: {value=0, no children}
                                          }
                }

"""

# TODO: fix this algorithm

class QuadNode():
    
    def __init__(self, value):
        self.value:int = value
        self.top_left: QuadNode = None
        self.top_right: QuadNode = None
        self.bot_left: QuadNode = None
        self.bot_right: QuadNode = None
        
        
def construct_matrix(root, n):
    
    output_matrix = [[-1]*n for _ in range(n)]
        
    
    def fill_helper(start_row, end_row, start_col, end_col, currnode):
        
        # nxn matrix with value 
        if currnode.value:
            for row in range(start_row, end_row): # 0, 5 -> 0, 1, 2, 3, 4
                for col in range(start_col, end_col):
                    output_matrix[row][col] = currnode.value
                

        else:
            fill_helper(start_row, end_row//2, start_col, end_col//2, currnode.top_left)

            fill_helper(start_row, end_row//2, end_col//2, end_col, currnode.top_right)

            fill_helper(end_row//2, end_row, start_col, end_col//2, currnode.bot_left)

            fill_helper(end_row//2, end_row, end_col//2, end_col, currnode.bot_right)
            
            


    fill_helper(0, n, root)
    return output_matrix