from mpi4py import MPI
import numpy as np
import time 

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    time.sleep(0.2)
    data = [0, 2, 3]
    for i in range(1, size+1):
        #data = np.arange(4.) + i
        if i == 2:
            data = [4, 5, 6, 'ss', 'b']
        req = comm.isend(data, dest=1, tag = i)
        print(f'Process {rank}, send request to {i}  initiated')
        print(f'Process {rank}, send test is {req.Test()}')
        #req.Wait()
        #print('Process {} sent data:'.format(rank), data)

else:
    time.sleep(5)
    data = [1, 1, 1]
    #req = comm.irecv(source=0, tag = 1)
    print(f'Process {rank}, receive initiated')
    #print(f'Process {rank}, receive test is {req.Test()}')
    print(f'Process {rank}, prob test {comm.Iprobe(0)}')
    if comm.Iprobe(0):  
    #req.wait()
        data = comm.recv(source=0, tag=1)
        print('Process {} received data:'.format(rank), data)
    time.sleep(5)
    data2 =  np.zeros(4)
    #if req.Test():
     #   data = req.wait()
    #print(f'Process {rank}, receive test is {req.Test()}')
    print(f'Process {rank}, prob test {comm.Iprobe(0)}')
    print('Process {} received data: '.format(rank), data)
    req2 = comm.irecv(source=0, tag = 1)
    time.sleep(3)
    if comm.Iprobe(0):
        data = comm.recv(source=0, tag=2)
        print('Process {} received data: '.format(rank), data)
