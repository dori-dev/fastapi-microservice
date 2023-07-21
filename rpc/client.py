import pika
import uuid


class FibRpcClient(object):
    def __init__(self):
        self.connection = self.connect()
        self.channel = self.connection.channel()
        queue = self.channel.queue_declare(queue="fib_queue")
        self.channel.queue_bind(
            exchange="fib",
            queue="fib_queue",
            routing_key="rk2",
        )
        self.callback_queue = queue.method.queue
        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True,
        )

    def connect(self):
        credentials = pika.PlainCredentials("testuser", "1234")
        parameters = pika.ConnectionParameters(
            "localhost",
            5672,
            "/",
            credentials,
        )
        connection = pika.BlockingConnection(parameters)
        return connection

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, number):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange="fib",
            routing_key="rk1",
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(number),
        )
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)
