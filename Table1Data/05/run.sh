time gzip 01_soilmoisture_dataset_cleaned.csv -k -f -9
#python3 01_soilmoisture_dataset_cleaned.csv
echo 'SZ Compress'
time ../../../SZ/sz_build/bin/testfloat_compress  sz.config 01_soilmoisture_dataset_cleaned.csv.bin 86233
echo 'SZ Decompress'
time ../../../SZ/sz_build/bin/testfloat_decompress 01_soilmoisture_dataset_cleaned.csv.bin.sz 86233
#python3 comparebin.py 01_soilmoisture_dataset_cleaned.csv.bin 01_soilmoisture_dataset_cleaned.csv.bin.sz.out f
#python3 readbin.py 01_soilmoisture_dataset_cleaned.csv.bin.sz.out f > 01_soilmoisture_dataset_cleaned.csv.bin.sz.out.csv
