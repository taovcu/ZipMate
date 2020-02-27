import sys, struct, os
import numpy as np

def webp_compress():
    #os.system( 'cwebp {0} -m 0 -q 99.999 -short -o {0}.webp'.format(sys.argv[1]) )
    #os.system( 'img2webp {0} -lossless -m 1 -q 0 -short -o {0}.webp'.format(sys.argv[1]) )
    os.system( 'cwebp {0} -lossless -m 1 -q 0 -short -o {0}.webp'.format(sys.argv[1]) )

webp_compress()
