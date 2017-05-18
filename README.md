# pytest-mocha

Pytest output in [MochaJS](http://mochajs.org) format

![pytest-mocha](https://cloud.githubusercontent.com/assets/5260987/26183565/eaa21f8e-3b55-11e7-8c9e-bdf1613d3903.png)

It uses docstrigs as a tool to create the sections that mocha creates using the `describe` and `it` structure. Example:

```python
# file examples/test_example.py
def test_case():
    '''Section :: subsection :: Should execute test'''
    pass
```

outputs this:

```
Section :: examples/test_example.py
    subsection
        ✓ Should execute test
```

## Install

```
pip install pytest-mocha
```

## Use

```
pytest --mocha
```

## Args

* `--mocha`: Enable mocha as pytest reporter
* `--mocha-force-disable`: Disable mocha reporter even if enabled with `--mocha` flag
