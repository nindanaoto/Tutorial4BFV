#!/bin/python3
import numpy as np
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))
import mulfft

n=2048

def polymul(a,b):
    res = np.zeros(n,dtype=np.int64)
    # ここに処理を書く。resに答えを入れれば良い。
    # return res
    # res = np.zeros(n,dtype=np.int64)
    # for i in range(n):
    #     for j in range(n):
    #         mul = a[i]*b[j]
    #         res[(i+j)%n] += -mul if((i+j)>=n) else mul
    # return res
    # 当日用高速版
    return mulfft.polymul(a,b)

if __name__ == "__main__":
    a = []
    b = []
    with open(sys.argv[1]) as f:
        a = np.array([int(s.strip()) for s in f.readlines()],dtype=np.int64)
    with open(sys.argv[2]) as f:
        b = np.array([int(s.strip()) for s in f.readlines()],dtype=np.int64)
    res = polymul(a,b)
    for i in res:
        print(i)
