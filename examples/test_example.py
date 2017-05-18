# -*- coding: utf-8 -*-
from unittest import TestCase

import pytest


class TestExampleClass(TestCase):
    '''Example Class'''

    @pytest.mark.skip(reason='no way of currently testing this')
    def test_do_not_execute(self):
        'example :: Skip this test'
        pass

    def test_example(self):
        '''
        example :: Should pass test
        '''
        pass

    def test_example_error(self):
        'example :: Should fail test'
        raise ValueError('error here')


def test_example_inside():
    '''
    Example Class :: example ::
    Should still be inside the same subsection
    '''
    pass

def test_example_outside():
    '''
    Outside :: example :: Should be outside
    '''
    pass


class TestClassWithoutDoc(TestCase):
    def test_method_without_doc(self):
        pass

    def test_method_with_subsection(self):
        '''subsection :: Test method with subsection'''
        pass

def test_func_without_doc():
    pass

def test_func_without_subsection():
    '''Test without subsection here'''
    pass
