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
from tojitsukadai.kadai6.mohan import Mul

Bgbit = 10
Bg = 2**Bgbit
l = 4
# 関数内で定義してもいいが共通で使うのでここで定義
h = np.array([2**(64-(i+1)*Bgbit) for i in range(l)],dtype = np.uint64)

def RelinearlizationKeyGen(key):
    res = np.zeros((l,2,n),dtype=np.int64)
    # ここに処理を書く。rlkに答えを入れれば良い。
    res = np.zeros((l,2,n),dtype=np.int64)
    res = np.vstack(
        [[Encrypt(np.zeros(n,dtype=np.int64), key, alpha)] for i in range(l)]
    )
    keysquare = polymul(key, key)
    muh = np.array([h[i] * keysquare for i in range(l)], dtype=np.int64)
    res[:, 1] += muh
    return res


def Decomposition(a):
    res = np.zeros((l,n),dtype=np.int64)
    # ここに処理を書く。resに答えを入れれば良い。
    # 基本的には課題2のDecompositionと同じだがint64
    res = np.zeros((l,n),dtype=np.int64)
    offset = np.uint64(Bg/2 * sum(h))
    t = np.uint64(a) + offset
    t = np.array([t >> i for i in [64 - (p + 1) * Bgbit for p in range(l)]])
    t &= Bg - 1
    t = t.astype(np.int64)
    t -= Bg // 2
    res = t
    return res

def Relinearization(c,rlk):
    res = np.zeros((2,n),dtype=np.int64)
    # ここに処理を書く。resに答えを入れれば良い。
    res = c[0:2]
    decompc = Decomposition(c[2])
    for i in range(l):
        res += [polymul(decompc[i], rlk[i][0]), polymul(decompc[i], rlk[i][1])]
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