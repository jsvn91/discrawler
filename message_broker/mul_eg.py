import pika
from multiprocessing import Process


def callback():
    print ('callback got data')


class c1():
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='e1', durable='true')
        result = self.channel.queue_declare(durable='false', queue='q1')
        queue_name = result.method.queue
        binding_key = "b1"
        self.channel.queue_bind(exchange='e1', queue=queue_name, routing_key=binding_key)
        self.channel.basic_consume(callback,queue = queue_name)

    def run(self):
        self.channel.start_consuming()


class c2():
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='e2', durable='true', type='topic')
        result = self.channel.queue_declare(durable='false', queue='q2')
        queue_name = result.method.queue
        binding_key = "b2"
        self.channel.queue_bind(exchange='e1', queue=queue_name, routing_key=binding_key)

        self.channel.basic_consume(callback,queue=queue_name,no_ack=False)

    def run(self):
        self.channel.start_consuming()

if __name__ == '__main__':

    c1 = c1()
    c2 = c1()
    c3 = c1()
    c4 = c1()

    subscriber_list = []
    subscriber_list.append(c1())
    subscriber_list.append(c1())
    subscriber_list.append(c2())
    subscriber_list.append(c2())

    # execute
    process_list = []
    for sub in subscriber_list:
        process = Process(target=sub.run)
        process.start()
        process_list.append(process)

    # wait for all process to finish
    for process in process_list:
        process.join()