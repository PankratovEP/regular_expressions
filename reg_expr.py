import sys
from re import *

def poisk_vhozhdeniya():
    for line in sys.stdin:
        line = line.rstrip()
        if len(findall('cat', line)) > 1:
            print(line)
