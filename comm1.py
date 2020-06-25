from mpi4py import MPI 
import time 
import tensorflow as tf 

comm = MPI.COMM_WORLD

rank = comm.rank
size = comm.size
name = MPI.Get_processor_name()

shared = (rank+1)*5
start = time.time()

if rank == 0:
    data = shared 
    comm.send(data, dest=1)
    comm.send(data, dest=2)
    print('From rank, %d, we sent %d'%(rank, data))
    print(f'time: {time.time() - start}')
    #time.sleep(5)

elif rank == 1:
    data = comm.recv(source=0)
    print(f'on node {rank}, we received: {data}')
    print(f'time: {time.time() - start}')

elif rank == 2:
    data = comm.recv(source=0)
    print(f'on node {rank}, we received: {data}')
    print(f'time: {time.time() - start}')
