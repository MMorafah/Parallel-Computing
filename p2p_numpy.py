from mpi4py import MPI

import numpy as np

comm = MPI.COMM_WORLD

assert comm.size == 2

rank = comm.rank 

if rank == 0:
    data = np.arange(10, dtype=np.float64)
    comm.Send(data, dest=1, tag=13)
elif rank == 1:
    data = np.empty(10, dtype=np.float64)
    comm.Recv(data, source=0, tag=13)
    print("[%02d] Received: %s" % (rank, data))

