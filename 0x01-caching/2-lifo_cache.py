#!/usr/bin/env python
""" Implement a FIFO cache algorithm
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Implement a FIFO cache algorithm
    """

    def __init__(self):
        """ initializer """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Assign to the dictionary the item value to the key"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.stack:
                newest = self.stack.pop()
                del self.cache_data[newest]
                print("DISCARD: {}".format(newest))
        if key not in self.stack:
            self.stack.append(key)
        else:
            if self.stack[len(stack) - 1] != key:
                self.stack.remove(key)
                self.stack.append(key)

    def get(self, key):
        """ return the value in the dictionary link to the
        given key"""
        if (key is None) or (key not in self.cache_data):
            return None
        return self.cache_data[key]

    def print_cache(self):
        """ Print the cache data"""
        for key, value in self.cache_data.items():
            print("{}: {}".format(key, value))
