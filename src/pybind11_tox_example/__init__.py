from .cpplib import add, sub


def double(n):
    return add(n, n)


__all__ = ["add", "sub", "double"]
