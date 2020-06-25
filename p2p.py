
from mpi4py import MPI

comm = MPI.COMM_WORLD

if comm.rank == 0:
    sendmsg = 123
    comm.send(sendmsg, dest=1, tag=11)
    recvmsg = comm.recv(source=1, tag=22)
    print("[%02d] Received message: %s" % (comm.rank, recvmsg))
else: 
    recvmsg = comm.recv(source=0, tag=11)
    print("[%02d] Received message: %s" % (comm.rank, recvmsg))
    sendmsg = "Message from 1" 
    comm.send(sendmsg, dest=0, tag=22)
