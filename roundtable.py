import mpi4py 
mpi4py.rc.recv_mprobe = False 

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

s = 0 
temp = rank 

for i in range(size):
    if rank == size - 1:
        des = 0
    else: 
        des = rank + 1
    comm.send(temp, dest=des)

    if rank == 0:
        src = size - 1 
    else: 
        src = rank - 1
    
    temp = comm.recv(source= src)
    print("process %s receives %s from process %s"%(rank, temp, des))
    s += temp

print("Process %s has final sum is %s"%(rank, s))

