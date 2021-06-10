#!/usr/bin/env python
import pika

class Producer():

    def __init__(self,queue_name,call_back_function_name):

        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        channel.queue_declare(queue=queue_name)

        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body=call_back_function_name)
        print(" [x] Sent ",call_back_function_name)

        connection.close()

p1 = Producer('scrapper','Hello Queue')
p1 = Producer('scrapper','Hello Queue')
p1 = Producer('scrapper','Hello Queue')
p1 = Producer('scrapper','Hello Queue')
p1 = Producer('scrapper','Hello Queue')
p1 = Producer('scrapper','Hello Queue')
p1 = Producer('scrapper','Hello Queue')
p1 = Producer('parser','Hello Parser')
p1 = Producer('parser','Hello Parser')
p1 = Producer('parser','Hello Parser')
p1 = Producer('parser','Hello Parser')
p1 = Producer('parser','Hello Parser')
p1 = Producer('parser','Hello Parser')
p1 = Producer('parser','Hello Parser')