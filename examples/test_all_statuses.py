# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def broken_fixture():
    raise Exception('Trigger an error in any test which uses this fixture')


def test_pass():
    """All statuses :: This test passes"""
    assert True


def test_fail():
    """All statuses :: This test fails"""
    assert False


def test_error(broken_fixture):
    """All statuses :: This test has a broken fixture which raises an error"""
    assert True


@pytest.mark.skip
def test_skip():
    """All statuses :: This test is skipped"""
    assert True


@pytest.mark.xfail
def test_xfail():
    """All statuses :: This test is expected to fail and does"""
    assert False


@pytest.mark.xfail
def test_xpass():
    """All statuses :: This test is expected to fail but actually passes"""
    assert True
