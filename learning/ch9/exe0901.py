import time

from functools import wraps


def timethis(func):
    """
    decorate the export the exucution time
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@timethis
def countdown(n,*args,**kwargs):
    while n > 0:
        n -= 1
    print("finish counting down")


countdown.__wrapped__(1000000,2,3,4,5,6,j=1,k=2)
