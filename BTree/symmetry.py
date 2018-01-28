def issymmetric(tree):
    ''' This method checks if a tree is symmetric or not'''
    if not tree:
        return False

    def isamirrorimage(lefttree, righttree):
        if not lefttree and not righttree:
            return True
        elif not lefttree or not righttree:
            return False
        elif lefttree._data != righttree._data:
            return False

        if not isamirrorimage(lefttree._left, righttree._right):
            return False

        if not isamirrorimage(lefttree._right, righttree._left):
            return False

        return True

    return isamirrorimage(tree._left, tree._right)