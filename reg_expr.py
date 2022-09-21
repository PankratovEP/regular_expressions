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


def poisk_slsh():
    for line in sys.stdin:
        line = line.rstrip()
        if search(r'\\', line):
            print(line)


def podryad():
    for line in sys.stdin:
        line = line.rstrip()
        pat = r"(\w+)\1"
        if match(pat, line):
            print(line)


def zamena_slov():
    for line in sys.stdin:
        line = line.rstrip()
        line = sub('human', 'computer', line)
        print(line)

