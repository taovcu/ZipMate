import struct, sys

if sys.argv[3] == 'f':
    with open(sys.argv[1], 'rb') as fin1:
        with open(sys.argv[2], 'rb') as fin2:
            total = 0
            diff = 0
            totaldiff = 0
            data1 = fin1.read(4)
            data2 = fin2.read(4)
            while data1 and data2:
                total += 1
                f1 = (struct.unpack('f', data1)[0])
                f2 = (struct.unpack('f', data2)[0])
                if f1 != f2:
                    diff += 1
                    totaldiff += abs(f1-f2)

                data1 = fin1.read(4)
                data2 = fin2.read(4)
            print('total points: {}'.format(total))
            print('Diff rate: {}'.format(diff/total))
            print('Avg abs diff: {}'.format(totaldiff/diff))
            print('Amortized Avg abs diff: {}'.format(totaldiff/total))

if sys.argv[3] == 'B':
    with open(sys.argv[1], 'rb') as fin1:
        with open(sys.argv[2], 'rb') as fin2:
            total = 0
            diff = 0
            totaldiff = 0
            data1 = fin1.read(1)
            data2 = fin2.read(1)
            while data1 and data2:
                total += 1
                f1 = (struct.unpack('B', data1)[0])
                f2 = (struct.unpack('B', data2)[0])
                if f1 != f2:
                    diff += 1
                    totaldiff += abs(f1-f2)

                data1 = fin1.read(1)
                data2 = fin2.read(1)
            print('total points: {}'.format(total))
            print('Diff rate: {}'.format(diff/total))
            print('Avg abs diff: {}'.format(totaldiff/diff))
            print('Amortized Avg abs diff: {}'.format(totaldiff/total))

