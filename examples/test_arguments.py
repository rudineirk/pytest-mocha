import pytest


def foo(arg):
    return 'bar'


@pytest.fixture(params=["foo", "bar"])
def stub(request):
    return request.param


def test_foo(stub):
    '''foo :: test arguments'''
    assert foo(stub) == 'bar'
