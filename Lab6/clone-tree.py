def clone(tree):
    """
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6,[tree(7)])])
    >>> numbers
    [1, [2], [3, [4], [5]], [6, [7]]]
    """

    """
    if tree is a leaf return [tree]
    if tree has branches then append clone(tree) to existing tree
    """
    new = []
    if is_leaf(tree):
        return [tree]

    tree.append(clone(branch) for branch in branches(tree))
    return new[:len(tree) - 1]

#Constructor
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

#Selectors
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    return True

def is_leaf(tree):
    return not branches(tree)