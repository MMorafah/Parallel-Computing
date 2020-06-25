import numpy as np 
from mpi4py import MPI 

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

print(f'size: {size}, rank: {rank}')

if rank == 0:
    print('I am Rank 0')
    msg = 'Hello, world'
    comm.send(msg, dest=1)
elif rank == 1:
    print('I am Rank 1')
    s = comm.recv()
    print("rank %d: %s" % (rank, s))
