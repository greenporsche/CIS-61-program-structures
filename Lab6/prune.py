def prune_leaves(t, vals):
    """Return a modified copy of t with all leaves that have a label that appears in vals removed. Return None if the entire tree is pruned away.
    >>> t = tree(2)
    >>> print(prune_leaves(t, (1, 2)))
    None
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6,[tree(7)])])
    >>> numbers
    [1, [2], [3, [4], [5]], [6, [7]]]
    >>> prune_leaves(numbers, (3, 4, 6, 7))
    [1, [2], [3, [5]], [6]]
    """
    if is_leaf(t) and label(t) in vals:
        return None
    pruned_branches = [prune_leaves(b, vals) for b in branches(t)]
    pruned_branches = [b for b in pruned_branches if b is not None]
    return tree(label(t), pruned_branches)

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