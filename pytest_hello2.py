from pytest_hello import hello

def test_default():
    assert hello() == "Hello, world"

def test_argument():
    assert hello("Richard") == "Hello, Richard"

def test_argument2():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"Hello, {name}"

### can turn tests into packages
# 1.create a directory/folder with the tests you want to run
# 2.add file with tests in the folder
# 3.add another file named __init__.py
    # tells python to treat the folder as a package
        # eg. /test/pytest_hello.py
        #     /test/__init__.py
# 4.now you can run pytest on a complete folder
    # pytest test