def isdeadEnd(root):
    # Code here
    leaf = []
    ans = []
    ans.append(0)
    
    def inorder(root):
        if not root:
            return
        inorder(root.left)
        if not root.left and not root.right:
            leaf.append(root.data)
        else:
            ans.append(root.data)
        inorder(root.right)
    
    inorder(root)
    
    for i in range(len(leaf)):
        if (leaf[i] - 1) in ans and (leaf[i] + 1) in ans:
            return True
    return False
