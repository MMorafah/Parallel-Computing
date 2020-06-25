from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# master process
if rank == 0:
    data = np.arange(4.)
    # master process sends data to worker processes by
    # going through the ranks of all worker processes
    for i in range(1, size):
        comm.Send(data, dest=i, tag=i)
        print('Process {} sent data:'.format(rank), data)

# worker processes
else:
    # initialize the receiving buffer
    data = np.zeros(4)
    # receive data from master process
    comm.Recv(data, source=0, tag=rank)
    print('Process {} received data:'.format(rank), data)

