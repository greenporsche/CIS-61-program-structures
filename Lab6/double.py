def double_tree(t): 
    """Return a tree with double every element in t 
    >>> numbers = tree(1, [tree(2, [tree(3), tree(4)]), tree(5, [tree(6, [tree(7)]), tree(8)])]) 
    >>> print(double_tree(numbers))
    [2, [4, [6], [8]], [10, [12, [14]], [16]]]
    """

    if is_leaf(t):
        return tree(2 * label(t))

    doubled_branches = [double_tree(b) for b in branches(t)]
    return tree(2 * label(t), doubled_branches)

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