#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

nb = 10
if len(sys.argv) == 2:
    nb = int(sys.argv[1])
N = []
TMP = []
N.append(1)

for x in range(nb):
    i = 0
    count = 0
    char = N[0]
    TMP = []
    print N
    while i < len(N):
        if N[i] == char:
            count = count + 1
        else:
            TMP.append(count)
            TMP.append(char)
            count = 1
            char = N[i]
        i+=1
    if (count == 0):
        if (N[i - 1] == char):
            count = count + 1
    if (count != 0):
        TMP.append(count)
        TMP.append(char)
    N = list(TMP)

