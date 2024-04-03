#!/usr/bin/env python
""" Implement a FIFO cache algorithm
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Implement a FIFO cache algorithm
    """

    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ assign to the dictionary the item value to the key
        """
        if key is None or item is None:
            return

        if key not in self.queue:
            self.queue.append(key)
        else:
            if self.queue[len(self.queue) - 1] != item:
                self.queue.remove(key)
                self.queue.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            num1 = self.queue.pop(0)
            del self.cache_data[num1]
            print("DISCARDS: {}".format(self.cache_data[num1]))

    def get(self, key):
        """ return the value in the dictionary link to the
        given key"""
        if (key is None) or (key not in self.cache_data):
            return None
        return self.cache_data[key]
