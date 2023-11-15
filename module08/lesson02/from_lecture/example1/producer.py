import pika


def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='line_one')  # creating queue with name

    channel.basic_publish(exchange='',
                          routing_key='line_one',
                          body='third message!'.encode())  # excahnge by default AMQP default
    print(" [x] Sent 'third message!'")
    connection.close()  # close connection


if __name__ == '__main__':
    main()