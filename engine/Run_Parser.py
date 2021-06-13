import importlib
import logging
import time
from queue import Queue
from threading import Thread

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
recrawl = []

class DownloadWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.scrapper_name = scrapper_name
        # m1.__init__(self)
        self.queue = queue


    def run(self):
        # while True:
        # Get the work from the queue and expand the tuple
        n = self.queue.get()

        # while True:
        try:

            m1 = object()

            for module in module_list:
                mod = importlib.import_module(module)
                class_ = getattr(mod, module.split(".")[1])

            try:
                m1 = class_()
                m1.url = m1.get_a_input(n)
                m1.url_id_2 = str(n + 1)
            except:

                recrawl.append(n)

                pass
            del m1

        finally:
            self.queue.task_done()


if __name__ == '__main__':
    ts = time.time()

    scrapper_name = "parser_flipkart_category"
    module_list = ['parsers.' + scrapper_name]
    m1 = object()

    for module in module_list:
        mod = importlib.import_module(module)
        class_ = getattr(mod, module.split(".")[1])
        m1 = class_()

    # Create a queue to communicate with the worker threads
    queue = Queue()

    # Put the tasks into the queue as a tuple
    worker_ls = []
    for n in m1.urls_ls:

        logger.info('Queueing {}'.format(n))

        if len(worker_ls) == 2:
            worker_ls = []

        worker_ls.append(DownloadWorker(queue))
        worker_ls[-1].daemon = False
        worker_ls[-1].start()
        queue.put((n))
        worker_ls[-1].join()

    if not recrawl:
        #no recrawl
        pass
    else:
        for n in recrawl:

            logger.info('Queueing {}'.format(n))

            if len(worker_ls) == 2:
                worker_ls = []

            worker_ls.append(DownloadWorker(queue))
            worker_ls[-1].daemon = False
            worker_ls[-1].start()
            queue.put((n))
            worker_ls[-1].join()

        pass

    # Causes the main thread to wait for the queue to finish processing all the tasks
    queue.join()
    print('Took {}'.format(time.time() - ts))
