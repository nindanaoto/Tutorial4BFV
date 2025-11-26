#!/bin/python3
# Relinealization of TRLWE ciphertexts

import numpy as np
import time
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from jizenkadai.kadai1.kadai1 import polymul, n
sys.path.append(str(Path(__file__).resolve().parent.parent))
from kadai3.kadai3 import Encrypt, Decrypt, alpha, t
from tojitsukadai.kadai6.kadai6 import Mul

Bgbit = 10
Bg = 2**Bgbit
l = 4

def RelinearlizationKeyGen(key):
    rlk = np.zeros((l,2,n),dtype=np.int64)
    # ここに処理を書く。rlkに答えを入れれば良い。
    return rlk


def Decomposition(a):
    res = np.zeros((l,n),dtype=np.int64)
    # ここに処理を書く。resに答えを入れれば良い。
    # 基本的には課題2のDecompositionと同じだがint64
    return res

def Relinearization(c):
    res = np.zeros((2,n),dtype=np.int64)
    # ここに処理を書く。resに答えを入れれば良い。
    return res

if __name__ == "__main__":
    # 時間計測用なのでテストとしては1にすると良い
    numtest = 10
    key = np.random.randint(-1,2,size=n,dtype=np.int8)
    rlk = RelinearlizationKeyGen(key)
    m0 = np.zeros((numtest,n),dtype=np.int8)
    m1 = np.zeros((numtest,n),dtype=np.int8)
    c1 = np.zeros((numtest,2,n),dtype=np.int64)
    c2 = np.zeros((numtest,2,n),dtype=np.int64)
    c4 = np.zeros((numtest,2,n),dtype=np.int64)
    for i in range(numtest):
        m0[i][0] = np.random.randint(0,t,dtype=np.int8)
        m1[i][0] = np.random.randint(0,t,dtype=np.int8)
        c1[i] = Encrypt(m0[i], key, alpha)
        c2[i] = Encrypt(m1[i], key, alpha)
    start = time.perf_counter()
    for i in range(numtest):
        print(i)
        c3 = Mul(c1[i], c2[i])
        c4[i] = Relinearization(c3, rlk)
    end = time.perf_counter()

    for i in range(numtest):
        res = Decrypt(c4[i], key)
        if not np.array_equal((m0[i] * m1[i]) % t, res):
            print("Error")
            exit(1)
    print("PASS")
    print("Time:", "{:.3f}".format((end - start)/numtest), "s")