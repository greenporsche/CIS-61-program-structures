def cumulative_sum(t): 
    """Mutates t so that each node's label becomes the sum of all labels in the corresponding subtree rooted at t. 
    >>> #below test case will not work. Don’t test it. 
    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)]) 
    >>> cumulative_sum(t) 
    >>> t
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)]) 
    """ 
    """
    replace each node of the tree with the sum of its branches
    if no branches then return the node
    """
    if not t.is_leaf():
        t = Tree(sum([cumulative_sum(b) for b in t.branches]), t.branches)






































class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches