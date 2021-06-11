# Multithreading in Python using the `threading` module.
# Based on: https://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python

import logging
import time
import random
from queue import Queue
from threading import Thread

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# logging.getLogger('sub_module').setLevel(logging.CRITICAL)
logger = logging.getLogger(__name__)

import importlib
scrapper_name = "scrapper_flipkart_category"
module_list = ['scrappers.' + scrapper_name]
m1 = object()

for module in module_list:

    mod = importlib.import_module(module)
    class_ = getattr(mod, module.split(".")[1])
    m1 = class_

from scrappers.scrapper_flipkart_category import scrapper_flipkart_category
# M1 = eval('from scrappers.scrapper_flipkart_category import scrapper_flipkart_category')
class DownloadWorker(Thread,m1):
    def __init__(self, queue):
        Thread.__init__(self)
        self.scrapper_name = scrapper_name
        m1.__init__(self)
        self.queue = queue

    def run(self):
        # while True:
            # Get the work from the queue and expand the tuple
        n = self.queue.get()
        self.url = self.get_a_input(n)
        self.get_category_crawl()
        try:
            # print(g)
            pass
        finally:
            self.queue.task_done()

if __name__ == '__main__':
    ts = time.time()

    # Create a queue to communicate with the worker threads
    queue = Queue()

    m2 = m1()

    # Create 5 worker threads
    for x in range(4):

        worker = DownloadWorker(queue)

        # Setting daemon to True will let the main thread exit even though the workers are blocking
        worker.daemon = True
        worker.start()

    # Put the tasks into the queue as a tuple
    for n in m2.urls_ls:
        logger.info('Queueing {}'.format(n))
        queue.put((n))

    # Causes the main thread to wait for the queue to finish processing all the tasks
    queue.join()
    print('Took {}'.format(time.time() - ts))
