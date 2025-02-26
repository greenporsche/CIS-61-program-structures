def height(t): 
    """Return the height of a tree. 
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)]) 
    >>> height(t) 
    2
    """

    if is_leaf(t):
        return 0
    return max([1 + height(b) for b in branches(t)])

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