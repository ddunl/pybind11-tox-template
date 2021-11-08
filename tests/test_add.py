from python_example import add_wrapper


def test_add():
    assert add_wrapper(2, 2) == 4
