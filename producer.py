import pika

connection =pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Ola pra voce que esta do outro lado da telinha')
print(" [x] Sent message")
connection.close()