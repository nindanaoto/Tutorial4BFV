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
    #ここに処理を書く。resに答えを入れれば良い。
    return res

def Encrypt(key, alpha):
    res = np.zeros((2,n),dtype=np.int64)
    #ここに処理を書く。resに答えを入れれば良い。
    return res

def Decrypt(c, key):
    res = np.zeros(n,dtype=np.int64)
    #ここに処理を書く。resに答えを入れれば良い。
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