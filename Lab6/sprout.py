def sprout_leaves(t, vals):
    """Sprout new leaves containing the data in vals at each leaf in
    the original tree t and return the resulting tree.
    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print(t1)
    [1, [2], [3]]
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print(new1)
    [1, [2, [4, 5]], [3, [4, 5]]]
    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print(t2)
    [1, [2, [3]]]
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print(new2)
    [1, [2, [3, [6, 1, 2]]]]
    """

    if is_leaf(t):
        return tree(label(t), [vals])

    sprouted_branches = [sprout_leaves(b, vals) for b in branches(t)]
    return tree(label(t), sprouted_branches)

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