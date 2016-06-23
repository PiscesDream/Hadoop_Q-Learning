#!/usr/bin/python

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file):
    for line in file:
        yield line.strip().split('\t')

def main(separator='\t'):
    data = read_mapper_output(sys.stdin)
    data = sorted(data, key=lambda x: (x[0], x[1]))
    g = groupby(data, lambda x: (x[0], x[1]))
#   print [s for s in g]
    for (state, action), group in g:
        Qvalues = [float(q) for s, a, q in group]
        avgQ = sum(Qvalues)/len(Qvalues)
        if avgQ > 0.0:
            print "{}\t{}\t{}".format(state, action, avgQ)

if __name__ == "__main__":
    main()
