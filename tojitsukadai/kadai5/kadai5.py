#!/bin/python3
# Decryption of Extended TRLWE ciphertexts

import numpy as np
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from jizenkadai.kadai1.kadai1 import polymul, n
sys.path.append(str(Path(__file__).resolve().parent.parent))
from kadai3.kadai3 import alpha, t, Delta

def ExtendedEncrypt(m, key, alpha):
    res = np.zeros(n,dtype=np.int64)
    ksquare = polymul(key, key)
    # ここに処理を書く。resに答えを入れれば良い。
    return res

def ExtendedDecrypt(c, key):
    res = np.zeros(n,dtype=np.int64)
    ksquare = polymul(key, key)
    #ここに処理を書く。resに答えを入れれば良い。
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