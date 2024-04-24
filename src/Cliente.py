import rpyc
import sys
import time
import numpy

def remote_sum_vector(server, num):

    if num <= 0:
        num = max(0, int( input("Please enter th length of the vector: ") ) )

    start = time.time()

    vect = numpy.random.randint(0, num, num)

    conn = rpyc.connect(server, 18861)
    conn._config['sync_request_timeout'] = None

    
    result = conn.root.sum_vector(vect)
    
    print("Vetor:", vect)
    print("Soma dos elementos:", result)

    end = time.time()

    total = end-start

    print(f"Execution time: {total} s")

if len(sys.argv) < 3:
    exit("Usage {} SERVER".format(sys.argv[0]))


server = sys.argv[1]
remote_sum_vector(server, int(sys.argv[2]))