# -*- coding: utf-8 -*-
import re
from importlib import import_module

import pytest

MODULE_CACHE = {}
CLASS_CACHE = {}
FUNC_CACHE = {}
PYTEST_MAJOR_VERSION = int(pytest.__version__.split('.')[0])


def load_module(module_name):
    try:
        return MODULE_CACHE[module_name]
    except KeyError:
        pass

    MODULE_CACHE[module_name] = import_module(module_name)
    return MODULE_CACHE[module_name]


def load_class(module_name, class_name):
    if not class_name:
        return ''

    key = module_name + '::' + class_name
    try:
        return CLASS_CACHE[key]['name']
    except KeyError:
        pass

    module = MODULE_CACHE[module_name]

    text = class_name
    if class_name and hasattr(module, class_name):
        module_class = getattr(module, class_name)
        if hasattr(module_class, '__doc__') and module_class.__doc__:
            text = module_class.__doc__

    CLASS_CACHE[key] = {
        'name': text,
        'class': module_class
    }
    return text


def load_func(module_name, class_name, func_name):
    key = module_name
    class_key = module_name + '::' + class_name
    if class_name:
        key = class_key

    key += '::' + func_name

    try:
        return FUNC_CACHE[key]['name']
    except KeyError:
        pass

    module = MODULE_CACHE[module_name]
    module_class = None
    class_text = ''
    try:
        module_class = CLASS_CACHE[class_key]['class']
    except KeyError:
        pass

    text = func_name
    module_func = None
    if module_class and hasattr(module_class, func_name):
        module_func = getattr(module_class, func_name)
    elif hasattr(module, func_name):
        module_func = getattr(module, func_name)

    if module_func and hasattr(module_func, '__doc__') and module_func.__doc__:
        text = module_func.__doc__
        text = text.strip().replace('\n', ' ')
        text = re.sub(' +', ' ', text)

    FUNC_CACHE[key] = {
        'name': text,
        'func': module_func
    }
    return text


def load_test_info(nodeid):
    data = nodeid.split('::')
    file_name = data[0]
    class_name = ''
    func_name = ''
    arg_text = ''
    func_text = []
    if len(data) > 3 and PYTEST_MAJOR_VERSION <= 2:
        # test classes without TestCase as base on pytest 2.x
        class_name = data[1]
        func_text = data[3]
    elif len(data) > 2:
        class_name = data[1]
        func_text = data[2]
    else:
        func_text = data[1]

    func_text = func_text.split('[')
    func_name = func_text[0]
    if len(func_text) > 1:
        arg_text = '[' + func_text[1]

    module_name = file_name.replace('.py', '').replace('/', '.').replace('\\', '.')
    load_module(module_name)
    class_text = load_class(module_name, class_name)
    func_text = load_func(module_name, class_name, func_name)

    text = func_text
    if class_text:
        text = class_text + ' :: ' + text

    text = text + arg_text
    return file_name, text
