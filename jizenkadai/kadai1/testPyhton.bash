#!/usr/bin/env bash
failwith() {
  echo -e "\e[31m[ERROR]\e[m $1"
  exit 1
}
unittest() {
  diff <(python3 kadai2-1.py ./testdata/in/ina$1.txt ./testdata/in/inb$1.txt) ./testdata/out/out$1.txt || failwith "Test $1 failed"
}
for((i=0;i<10;i++)); do
    unittest ${i}
done
echo "PASS"