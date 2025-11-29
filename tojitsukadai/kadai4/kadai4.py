#!/bin/python3
# Addition of TRLWE ciphertexts
# Since it is almost tirival, this execercise is just for testing
import numpy as np
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from jizenkadai.kadai1.kadai1 import polymul, n
sys.path.append(str(Path(__file__).resolve().parent.parent))
from kadai3.kadai3 import Encrypt, Decrypt, alpha, t

def Add(c1, c2):
    res = c1+c2
    return res

if __name__ == "__main__":
    for i in range(10):
        print(i)
        key = np.random.randint(-1,2,size=n,dtype=np.int8)
        m1 = np.random.randint(0,t,size=n,dtype=np.int8)
        m2 = np.random.randint(0,t,size=n,dtype=np.int8)
        c1 = Encrypt(m1, key, alpha)
        c2 = Encrypt(m2, key, alpha)
        c3 = Add(c1, c2)
        res = Decrypt(c3, key)
        if not np.array_equal((m1 + m2) % t, res):
            print("Error")
            exit(1)
    print("PASS")