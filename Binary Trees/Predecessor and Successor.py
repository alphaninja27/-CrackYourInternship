def findPreSuc(root, pre, suc, key):
    #your code goes here
    if not root:
        return 
    if root.key == key:
        if root.left:
            pre[0] = root.left
            while pre[0].right:
                pre[0] = pre[0].right
        if root.right:
            suc[0] = root.right
            while suc[0].left:
                suc[0] = suc[0].left
        return
    if root.key < key:
        pre[0] = root
        findPreSuc(root.right, pre, suc, key)
    else:
        suc[0] = root
        findPreSuc(root.left, pre, suc, key)
