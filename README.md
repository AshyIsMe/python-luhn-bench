# A terrible attempt at luhn checksum counting with numpy


```
./testdata.sh # Generates 3 * 1MB txt files
time python3 main.py
Count,File
137514,test1.txt
137514,test2.txt
137514,test3.txt
python3 main.py  18.26s user 1.32s system 111% cpu 17.627 total

# 0.17019345322516594 MB/s 
# extremely very slightly horrifically slow...
```
