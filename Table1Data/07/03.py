import sys, struct
from numpy import array

output_file = open(sys.argv[1]+'.bin', 'wb')

with open(sys.argv[1]) as csvfile:
    line = csvfile.readline()
    while line:
        #print('line: {}'.format(line))
        fields = line.split(",")
        for i in range(len(fields)):
            if fields[i]:
                fields[i] = float(fields[i])
            else:
                fields[i] = 0
        a = array(fields, 'float32')
        a.tofile(output_file)
            
        line = csvfile.readline()

output_file.close()
