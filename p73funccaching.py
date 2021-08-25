"""function caching -- allows us to cache the return values of a function depending on the arguments 
it can save time when I/O bound function is periodicly called with the same arguments 
@lru_cache decorator gives you the abillity to cache  result of your function using least used strategy 
"""
import time
from functools import lru_cache

@lru_cache(maxsize=23)
def some_work(n):
    #Some task taking n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    some_work(1)
    # some_work(6)
    # some_work(2)
    print("Done... Calling again")
    some_work(5)
    # input()
    print("Called again")

