from . import cpplib

def add_wrapper(a, b):
    return cpplib.add(a, b)

__all__ = [add_wrapper]
