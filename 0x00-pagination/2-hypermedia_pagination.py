#!/usr/bin/env python3
""" Helper class - Server
"""
import csv
import math
from typing import List

index_range = __import__('0-simple_helper_function').index_range
Server = __import__('1-simple_pagination').Server

server = Server()

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Get a page base on the data
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        self.dataset()

        if self.dataset() is None:
            return []

        index = index_range(page, page_size)
        return self.dataset()[index[0]:index[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ method that takes the same arguments (and defaults)
        as get_page and returns a dictionary"""
        data = self.get_page(page, page_size)
        dataset = self.__dataset
        len_of_dataset = len(dataset) if dataset else 0
        pages = math.ceil(len_of_dataset / page_size) if dataset else 0
        page_size = len(data) if data else 0

        prev = page - 1 if page > 1 else None
        next_ = page + 1 if page < pages else None

        return {'page_size': page_size, 'page': page, 'data': data,
                'next_page': next_, 'prev_page': prev, 'total_pages': pages}
