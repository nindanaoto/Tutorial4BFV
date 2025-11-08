#!/usr/bin/env bash
failwith() {
  echo -e "\e[31m[ERROR]\e[m $1"
  exit 1
}
unittest() {
  diff <(python3 kadai2-2.py < ./testdata/in/in$1.txt) ./testdata/out/out$1.txt || failwith "Test $1 failed"
}
for((i=0;i<1000;i++)); do
    unittest ${i}
done
echo "PASS"