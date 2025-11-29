#!/bin/python3
# Encryption and Decryption of TRLWE
import numpy as np
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from jizenkadai.kadai1.kadai1 import polymul, n
alpha = 2**-51
t = 2
q = 2**64
Delta = np.int64(np.uint64(q // t))

def ModularGaussian(alpha):
    res = np.zeros(n,dtype=np.int64)
    # ここに処理を書く。resに答えを入れれば良い。
    # 模範解答
    def dtot64(d):
        return np.uint64(np.round((d%1)*(2.0**64)))
    res = np.int64(dtot64(np.random.normal(0, alpha, n)))
    return res

def Encrypt(m, key, alpha):
    res = np.zeros((2,n),dtype=np.int64)
    #ここに処理を書く。resに答えを入れれば良い。
    # a の生成
    res[0] = np.random.randint(-q//2, q//2, size=n, dtype=np.int64)
    # e の生成
    e = ModularGaussian(alpha)
    # b の計算
    res[1] = polymul(res[0], key) + e + (Delta * m)
    return res

def Decrypt(c, key):
    res = np.zeros(n,dtype=np.int64)
    #ここに処理を書く。resに答えを入れれば良い。
    phase = c[1] - polymul(c[0], key)
    res = ((np.uint64(phase) + (np.uint64(Delta) // 2)) // np.uint64(Delta)) % t
    return res

if __name__ == "__main__":
    for i in range(10):
        print(i)
        # ternary key
        key = np.random.randint(-1,2,size=n,dtype=np.int8)
        m = np.random.randint(0,t,size=n,dtype=np.int8)
        c = Encrypt(m, key, alpha)
        res = Decrypt(c, key)
        if not np.array_equal(m, res):
            print("Error")
            print("m:", m)
            print("res:", res)
            exit(1)
    print("PASS")