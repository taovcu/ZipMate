time gzip $1 -k
python3 06.py $1

inputFILESIZE=$(stat -c%s "$1.bin")
sze=`expr $inputFILESIZE / 4`
../../../SZ/sz_build/bin/testfloat_compress  $2 $1.bin $sze
../../../SZ/sz_build/bin/testfloat_decompress $1.bin.sz $sze
python3 comparebin.py $1.bin $1.bin.sz.out f
python3 readbin.py $1.bin.sz.out f > $1.bin.sz.out.csv
