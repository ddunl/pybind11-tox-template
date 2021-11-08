from . import cpplib


def add_wrapper(a, b):
    return cpplib.add(a, b)


def sub_wrapper(a, b):
    return cpplib.sub(a, b)


__all__ = ["add_wrapper", "sub_wrapper"]
