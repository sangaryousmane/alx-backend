#!/usr/bin/env python
""" Implement a MRU cache algorithm
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ Implement a FIFO cache algorithm
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assign to the dictionary the item value to the key"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = next(reversed(self.cache_data))
            del self.cache_data[mru_key]
            print("DISCARD: {}".format(mru_key))

        self.cache_data[key] = item

    def get(self, key):
        """ return the value in the dictionary link to the
        given key"""
        if (key is None) or (key not in self.cache_data):
            return None
        value = self.cache_data[key]
        self.cache_data.move_to_end(key)
        return value
