import sys, struct
from numpy import array

output_file = open(sys.argv[1]+'.bin', 'wb')

with open(sys.argv[1]) as csvfile:
    line = csvfile.readline()
    while line:
        #print('line: {}'.format(line))
        fields = line.split(",")
        for i in range(len(fields)):
            fields[i] = float(fields[i])
        a = array(fields, 'float32')
        a.tofile(output_file)
            
        line = csvfile.readline()

output_file.close()
