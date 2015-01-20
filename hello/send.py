
#! /usr/bin/env python

import pika
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.CRITICAL)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# channel.queue_declare(queue='hello1')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World123!')
print " [x] Sent 'Hello World!'"
connection.close()
