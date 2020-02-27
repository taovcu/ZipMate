import struct, sys

if sys.argv[2] == 'f':
    with open(sys.argv[1], 'rb') as fin:
        data = fin.read(4)
        while data:
            #print((int)(struct.unpack('f', data)[0]))
            print((struct.unpack('f', data)[0]))
            data = fin.read(4)

if sys.argv[2] == 'B':
    with open(sys.argv[1], 'rb') as fin:
        data = fin.read(1)
        while data:
            #print((int)(struct.unpack('f', data)[0]))
            print((struct.unpack('B', data)[0]))
            data = fin.read(1)

