import sys
from sayings_custom_module import hello

if len(sys.argv) ==2:
    hello(sys.argv[1])