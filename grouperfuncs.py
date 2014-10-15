# -*- coding: utf-8 -*-
'''
These two functions take any list, and seperate it into a list of sublists 
each of length (n).
'''
# Simple list comprehension, do not need function but for portability  
def chunker(data, n):
    return [data[x:x+n] for x in range(0, len(data), n)]

# list_chunker makes actual copies in memory, so probably slower
def list_chunker(data, n):    
    chunk = []    
    for i in range(0, len(data), n):
        chunk.append(data[i:i + n])
    return chunk

# list_grouper is ideal for very large data streams not fitting in memory    
from itertools import izip_longest   
def list_grouper(n, iterable, fillvalue=None):
    args = [iter(iterable) * n]
    return izip_longest(fillvalue=fillvalue, *args)

