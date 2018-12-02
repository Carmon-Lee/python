# import operator
# import itertools
# from collections import Counter
# import functools
#
# if __name__ == '__main__':
#     print(itertools.count(10))
#
#     print(list(zip(itertools.cycle([1,2]),[3,4,4,24,5])))
#     print(list(itertools.repeat(10,3)))
#     print(list(itertools.chain('fdas','5432')))
#     print(list(map(lambda x,y:x*y,[1,2,3],[5,4,3,6])))

#
# # sorted()
# import heapq
#
# if __name__ == '__main__':
#     a=[4,5,6,74,5,2]
#     b=heapq.heapify(a)
#     print(a)
#     heapq.heappop(a)
import time
from functools import wraps


def switchable_timer(enabled=True):
    def timethis(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            print('===start to count===')
            result = f(*args, **kwargs)
            print('===  end  count  ===')
            return result
        if enabled:
            return wrapper
        else:
            return f

    return timethis


@switchable_timer(enabled=True)
def demo():
    print('this is a demo')


if __name__ == '__main__':
    # demo=timethis(demo)
    demo()
