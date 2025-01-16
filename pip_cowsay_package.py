# pip install cowsay

import cowsay   # import a non-built-in package
import sys

if len(sys.argv) ==2:
    cowsay.cow("Hello, " + sys.argv[1])