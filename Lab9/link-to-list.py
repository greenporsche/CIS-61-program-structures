def link_to_list(link): 
    """Takes a linked list and returns a Python list with the same elements. 
    >>> link = Link(1, Link(2, Link(3, Link(4)))) 
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link.empty)
    []
    """
    if link is Link.empty:
        return []
    return [link.first] + link_to_list(link.rest)

class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest