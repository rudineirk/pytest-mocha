from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='pytest-mocha',
    packages=['pytest_mocha'],
    version='0.0.1',
    entry_points={
        'pytest11': ['pytest_mocha = pytest_mocha.plugin']
    },
    description='pytest plugin to display test execution output like a mochajs',
    long_description=long_description,
    author='Rudinei Goi Roecker',
    author_email='rudinei.roecker@gmail.com',
    url='https://github.com/rudineirk/pytest-mocha',
    license='MIT'
)
