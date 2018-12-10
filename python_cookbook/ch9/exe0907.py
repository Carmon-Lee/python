from inspect import signature
from functools import wraps


def typeassert(*ty_args, **ty_kwargs):
    # def decorate(func):
    #     if not __debug__:
    #         return func

    sig = signature(foo)
    bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments
    return None


def foo():
    return "bar"


typeassert(1, b=1)
