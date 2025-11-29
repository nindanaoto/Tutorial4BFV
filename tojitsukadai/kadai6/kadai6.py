#!/bin/python3
# Multiplication of TRLWE ciphertexts

import numpy as np
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from jizenkadai.kadai1.kadai1 import polymul, n
from jizenkadai.kadai1.mulfft import TwistFFT, TwistIFFT TwistFFTlong, TwistIFFTlong, twistlong, twist
sys.path.append(str(Path(__file__).resolve().parent.parent))
from kadai3.kadai3 import Encrypt, Decrypt, alpha, t, Delta
from kadai5.kadai5 import ExtendedDecrypt

def Extendedpolymul(a, b):
    res = np.zeros(n,dtype=np.int64)
    # ここに処理を書く。resに答えを入れれば良い。
    # float128
    # res = np.int64(np.uint64(
    #     np.round(
    #         TwistIFFTlong(
    #             np.multiply(TwistFFTlong(np.int64(a), twistlong), TwistFFTlong(np.int64(b), twistlong)),
    #             twistlong,
    #         )/np.float128(Delta)
    #     )%np.float128(2)**64)
    # )
    # float64
    # res = np.uint64(
    #     np.round(
    #         TwistIFFT(
    #             np.multiply(TwistFFT(np.int64(a), twist), TwistFFT(np.int64(b), twist)),
    #             twist,
    #         )/np.float64(Delta)
    #     )
    #     % 2 ** 64
    # )
    return res

def Mul(c1, c2):
    res = np.zeros((3,n),dtype=np.int64)
    #ここに処理を書く。resに答えを入れれば良い。
    return res

if __name__ == "__main__":
    for i in range(10):
        print(i)
        key = np.random.randint(0,2,size=n,dtype=np.int8)
        m1 = np.zeros(n,dtype=np.int8)
        m1[0] = np.random.randint(0,t,dtype=np.int8)
        m2 = np.zeros(n,dtype=np.int8)
        m2[0] = np.random.randint(0,t,dtype=np.int8)
        c1 = Encrypt(m1, key, alpha)
        c2 = Encrypt(m2, key, alpha)
        c3 = Mul(c1, c2)
        res = ExtendedDecrypt(c3, key)
        if not np.array_equal((m1 * m2) % t, res):
            print("Error")
            exit(1)
    print("PASS")