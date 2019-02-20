# -*- coding: utf-8 -*-
from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='pytest-mocha',
    version='0.3.0',
    description='pytest plugin to display test execution output like a mochajs',
    long_description=long_description,
    author='Rudinei Goi Roecker',
    author_email='rudinei.roecker@gmail.com',
    url='https://github.com/rudineirk/pytest-mocha',
    license='MIT',
    packages=['pytest_mocha'],
    install_requires=[
        'colorama>=0.3.9',
    ],
    entry_points={
        'pytest11': ['pytest_mocha = pytest_mocha.plugin']
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
)
