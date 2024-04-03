#!/usr/bin/env python
""" Implement a LIFO cache algorithm
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO caching """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ Puts item in cache """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.stack:
                newest = self.stack.pop()
                del self.cache_data[newest]
                print("DISCARD: {}".format(newest))

        if key not in self.stack:
            self.stack.append(key)
        else:
            length = len(self.queue)
            if self.queue[length - 1] != item:
                self.queue.remove(item)
                self.queue.append(item)

    def get(self, key):
        """ Gets item from cache """
        return self.cache_data.get(key, None)
