# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# all tests passed
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        output = []
        
        def get_val(root):
            if not root:
                output.append("N")
                return
            
            output.append(str(root.val))
            get_val(root.left)
            get_val(root.right)


        get_val(root)
        return ";".join(output)


        

    def deserialize(self, data):
        data_vals = data.split(";")
        idx = [0]

        def get_node():
            if idx[0] >= len(data_vals):
                return
            
            if data_vals[idx[0]] == "N":
                idx[0]+=1
                return None

            curr = TreeNode(int(data_vals[idx[0]]))
            idx[0] +=1
            curr.left = get_node()
            curr.right = get_node()

            return curr
        
        return get_node()