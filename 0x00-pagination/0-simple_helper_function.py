#!/usr/bin/env python3
""" Return a range of indexes corresponding pagination
"""


def index_range(page, page_size):
    """ Return a range of indexes corresponding pagination
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
