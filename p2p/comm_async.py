
from mpi4py import MPI
import time 

comm = MPI.COMM_WORLD
assert comm.size == 2

rank = comm.rank
start = MPI.Wtime()

if rank == 0:
    sendmsg = 123 
    target = 1
else: 
    target = 0 
if rank == 0:
    request = comm.isend(sendmsg, dest=target, tag=11)
    flag = not comm.Iprobe(source=target, tag = 11)
    for _ in range(10):
        print(request.Test())
        time.sleep(0.2)

    #time.sleep(1)
    print(request.Test())
else:
    time.sleep(2)
    while not comm.Iprobe(source=target, tag=11):
        print("[%02d] Waiting for message "% rank)
        time.sleep(0.5)
    time.sleep(2)
    #recvmsg = comm.recv(source = target, tag=11)
    print("[%02d] Message received %s " % (rank, str(recvmsg)))

#comm.Barrier()
end = MPI.Wtime()

if rank == 0 :
    print("Total time %f" % (end-start))
