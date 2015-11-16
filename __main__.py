import threading
from queue import Queue
import time

print_lock = threading.Lock()

q = Queue()
def exampleJob(worker):
    time.sleep(0.5)
    with print_lock:
        print(threading.current_thread().name, worker)
        
def threader():
    while True:
        worker = q.get()
        exampleJob(worker)
        q.task_done()

for x in range(10 ):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()

start = time.time()

for worker in range(20):
    q.put(worker) # q.put() worker moves the item worker (Could be array of strings, but worker simply = x where X in (range(N), which is just an array of #'s 1-N)
    # the queue is get()ing the worker from that queue, and doing exampleJob, that is how the worker variable is passed to the function, it travels through the queue
    # the threader takes the item out of the queue and sends it to exampleJob()
    
q.join()

print('entire job took: '+str(time.time()-start) + "s")