import sys
from re import *


def poisk_vhozhdeniya():
    for line in sys.stdin:
        line = line.rstrip()
        if len(findall('cat', line)) > 1:
            print(line)


def vhozhdenie_slova():
    for line in sys.stdin:
        line = line.rstrip()
        if search(r'\bcat\b', line):
            print(line)


def tri_simv():
    for line in sys.stdin:
        line = line.rstrip()
        if search(r'z...z', line):
            print(line)
