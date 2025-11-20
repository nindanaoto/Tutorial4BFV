#!/bin/python3
import numpy as np
import sys

n=1024

def polymul(a,b):
    res = np.zeros(n,dtype=np.int64)
    #ここに処理を書く。resに答えを入れれば良い。
    return res

a = []
b = []
with open(sys.argv[1]) as f:
    a = np.array([int(s.strip()) for s in f.readlines()],dtype=np.int64)
with open(sys.argv[2]) as f:
    b = np.array([int(s.strip()) for s in f.readlines()],dtype=np.int64)
res = polymul(a,b)
for i in res:
    print(i)
