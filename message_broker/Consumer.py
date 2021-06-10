import time

import pika, sys, os
from multiprocessing import Process

class Consumer():

    def __init__(self,queue_name):
        self.queue_name =queue_name

    def callback(self,ch, method, properties, body):
        print(" [x] Received %r" % body)

    def run(self):
        queue_name = self.queue_name
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()

        self.channel.queue_declare(queue=queue_name)

        self.channel.basic_consume(queue=queue_name, on_message_callback=self.callback, auto_ack=True)

        print( queue_name , '##' , ' [*] Waiting for messages. To exit press CTRL+C')

        self.channel.start_consuming()

if __name__ == '__main__':
    s1 = Consumer('scrapper')
    s2 = Consumer('scrapper')
    s3 = Consumer('scrapper')
    s4 = Consumer('scrapper')

    p1 = Consumer('parser')
    p2 = Consumer('parser')
    p3 = Consumer('parser')
    p4 = Consumer('parser')

    subscriber_list = []
    subscriber_list.append(s1)
    subscriber_list.append(s2)
    subscriber_list.append(s3)
    subscriber_list.append(s4)

    subscriber_list.append(p1)
    subscriber_list.append(p2)
    subscriber_list.append(p3)
    subscriber_list.append(p4)

    # execute
    process_list = []
    for sub in subscriber_list:
        process = Process(target=sub.run)
        process.start()
        process_list.append(process)

    # wait for all process to finish
    for process in process_list:
        process.join()