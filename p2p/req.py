from mpi4py import MPI
import time 
import numpy as np 

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

assert size == 2

if rank == 0:
    print(f'Rank {rank} called')
    requests = [MPI.REQUEST_NULL for _ in range(10)]
    print(f'Rank {rank} is sending messages')
    for i in range(10):
        print(f'Rank {rank} Request {i}: {requests[i].Test()}')
        requests[i] = comm.isend(i+1, dest=1, tag=11)
        print(f'Rank {rank} Message {i+1} sent')
        print(f'Rank {rank} Request {i}: {requests[i].Test()}')
        if i > 0:
            print(f'Rank {rank} Prev Request {i-1}: {requests[i].Test()}')
        time.sleep(0.5)
    print(f'Rank {rank} concluded!')
else:
    print(f'Rank {rank} called')
    time.sleep(0.5)
    d = 22
    #while not comm.Iprobe(source =0, tag=11):
    if True: 
        print(f'Rank {rank} waiting for message...')
        request = comm.irecv(0, tag=11)
        #print(f'Request: {request.Test()}')
        print(f'Rank {rank} Message {d} received')
        time.sleep(0.5)
        request = comm.irecv(d, 0, tag=11)
        print(f'Request: {request.Test()}')
        print(f'Rank {rank} Message {d} received')
    print(f'Rank {rank} concluded!')

