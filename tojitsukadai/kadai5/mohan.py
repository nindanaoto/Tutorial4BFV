#!/bin/python3
# Decryption of Extended TRLWE ciphertexts

import numpy as np
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from jizenkadai.kadai1.kadai1 import polymul, n
sys.path.append(str(Path(__file__).resolve().parent.parent))
from kadai3.kadai3 import ModularGaussian, q, alpha, t, Delta

def ExtendedEncrypt(m, key, alpha):
    res = np.zeros((3,n),dtype=np.int64)
    ksquare = polymul(key, key)
    # ここに処理を書く。resに答えを入れれば良い。
    # a の生成
    res[0] = np.random.randint(-q//2, q//2, size=n, dtype=np.int64)
    # e の生成
    e = ModularGaussian(alpha)
    # c の計算
    res[2] = np.random.randint(-q//2, q//2, size=n, dtype=np.int64)
    # b の計算
    res[1] = polymul(res[0], key) - polymul(res[2],ksquare) + e + (Delta * m)
    return res

def ExtendedDecrypt(c, key):
    res = np.zeros(n,dtype=np.int64)
    ksquare = polymul(key, key)
    # ここに処理を書く。resに答えを入れれば良い。
    phase = c[1] - polymul(c[0], key) + polymul(c[2],ksquare)
    res = ((np.uint64(phase) + (np.uint64(Delta) // 2)) // np.uint64(Delta)) % t
    return res

if __name__ == "__main__":
    for i in range(10):
        print(i)
        # ternary key
        key = np.random.randint(-1,2,size=n,dtype=np.int8)
        m = np.random.randint(0,t,size=n,dtype=np.int8)
        c = ExtendedEncrypt(m, key, alpha)
        res = ExtendedDecrypt(c, key)
        if not np.array_equal(m, res):
            print("Error")
            print("m:", m)
            print("res:", res)
            exit(1)
    print("PASS")