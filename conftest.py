from pytest_mocha.plugin import pytest_addoption as addopt
from pytest_mocha.plugin import pytest_configure as configure

CACHE = {
    'opts': False,
    'config': False
}

def pytest_addoption(parser):
    if CACHE['opts']:
        return

    addopt(parser)
    CACHE['opts'] = True

def pytest_configure(config):
    if CACHE['config']:
        return

    configure(config)
    CACHE['config'] = True
