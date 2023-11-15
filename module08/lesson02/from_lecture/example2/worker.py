import pika

import time
import json

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost',
                              port=5672,
                              credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    message = json.loads(body.decode())
    print(f" [x] Received {message}")
    time.sleep(1)
    print(f" [x] Done: {method.delivery_tag}")
    ch.basic_ack(delivery_tag=method.delivery_tag)  # when worker and will be success message


channel.basic_qos(prefetch_count=1)  # no new message untill worker finish first
channel.basic_consume(queue='line_two',
                       on_message_callback=callback)


if __name__ == '__main__':
    channel.start_consuming()
