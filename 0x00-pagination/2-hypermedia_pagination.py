#!/usr/bin/env python3
""" method that takes the same arguments (and defaults)
as get_page and returns a dictionary
"""
import math
Server = __import__('1-simple_pagination').Server
index_range = __import__('0-simple_helper_function').index_range
server = Server()


def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
    """ method that takes the same arguments (and defaults)
    as get_page and returns a dictionary"""

    pages = math.ceil()
    data = server.get_data(page, page_size)
    dataset = server.dataset()
    len_of_dataset = len(dataset) if dataset else None
    pages = math.ciel(len_of_dataset / page_size) if dataset else None
    page_size = len(data) if data else None
    prev = page - 1 if page > 1 else None
    next_ = page + 1 if page < pages else None

    return {'page_size': page_size, 'page': page, 'data': data,
            'next_page': next_, 'prev_page': prev,
            'pages': pages}
