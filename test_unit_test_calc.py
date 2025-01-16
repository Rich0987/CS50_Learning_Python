from unit_test_calc import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4    #assertion... declare to be true
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9   #changed test_square to a + not *... so Assertion Error appeared
    except AssertionError:
        print("3 square was not 9")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 square was not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 square was not 0")                    ###this could take forever... use pytest


if __name__ == "__main__":
    main()