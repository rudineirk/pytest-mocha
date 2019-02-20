import pytest


def foo(arg):
    return 'bar'


@pytest.fixture(params=["thing", "thang"])
def thing(request):
    return request.param


class TestClassForFoo(object):
    def test_foo(self, thing):
        '''subsection :: test description'''
        assert foo(thing) == 'bar'
