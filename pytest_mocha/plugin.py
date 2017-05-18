# -*- coding: utf-8 -*-
from .reporter import logstart_replacer, report_replacer


def pytest_addoption(parser):
    group = parser.getgroup('reporting')
    group.addoption(
        '--mocha',
        action='store_true',
        dest='mocha',
        help='Enable test reporter in mochajs format'
    )
    group.addoption(
        '--mocha-force-disable',
        action='store_true',
        dest='mocha_disable',
        help='Force disable mochajs reporter'
    )


def pytest_configure(config):
    if config.option.mocha and not config.option.mocha_disable:
        import imp
        import _pytest
        _pytest.terminal.TerminalReporter \
            .pytest_runtest_logstart = logstart_replacer
        _pytest.terminal.TerminalReporter \
            .pytest_runtest_logreport = report_replacer
        imp.reload(_pytest)
