import time
from queue import Queue
from threading import Thread


# A thread that produces data
def producer(out_q,data):
    # while True:
        # Produce some data
    out_q.put(data)


# A thread that consumes data
def consumer(in_q):
    # while True:
    # Get some data
    time.sleep(3)
    data = in_q.get()
    print(data)
    # Process the data



# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(target=producer, args=(q,"h1 Thread1",))
t2 = Thread(target=producer, args=(q,"h1 Thread2",))
t3 = Thread(target=producer, args=(q,"h1 Thread3",))
t4 = Thread(target=producer, args=(q,"h1 Thread4",))

t5 = Thread(target=consumer, args=(q,))
t6 = Thread(target=consumer, args=(q,))
t7 = Thread(target=consumer, args=(q,))
t8 = Thread(target=consumer, args=(q,))

t1.start()
t2.start()
t3.start()
t4.start()

t5.start()
t6.start()
t7.start()
t8.start()

t1.join()
t2.join()
t3.join()
t4.join()

t5.join()
t6.join()
t7.join()
t8.join()

