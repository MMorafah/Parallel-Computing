import mpi4py 
mpi4py.rc.recv_mprobe = False 

from  mpi4py  import  MPI
import socket 
import time 

start = time.time()

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size
name = MPI.Get_processor_name()
hostname = socket.gethostname()

t = time.time() - start 
print("Hello! I’m rank  %02d from  %02d, hostname %s, time %f" % (comm.rank , comm.size, hostname, t))



