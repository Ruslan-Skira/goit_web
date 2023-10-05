import pika


def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='hello_world')  # creating queue with name

    channel.basic_publish(exchange='', routing_key='hello_world', body='Hello world!'.encode())  # excahnge by default AMQP default
    print(" [x] Sent 'Hello World!'")
    connection.close()  # close connection 


if __name__ == '__main__':
    main()