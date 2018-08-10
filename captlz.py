!/usr/bin/python
import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    print(data[0].upper())
