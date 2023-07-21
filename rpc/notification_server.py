import time
import pika

from utils import fib


credentials = pika.PlainCredentials("testuser", "1234")
parameters = pika.ConnectionParameters(
    "localhost",
    5672,
    "/",
    credentials,
)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.exchange_declare(
    exchange="fib",
    durable="true",
    exchange_type="direct",
)
channel.queue_declare(queue="notify_queue")
channel.queue_bind(exchange="fib", queue="notify_queue", routing_key="rk1")


def on_request(ch, method, props, body):
    n = int(body)
    print(f"[.] fib({n})")
    response = fib(n)
    time.sleep(5)
    print(f"Send a notify to Mohammad Dori - result is {response}")
    ch.basic_ack(delivery_tag=method.delivery_tag, multiple=True)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="notify_queue", on_message_callback=on_request)
print(" [x] Awaiting RPC requests")
channel.start_consuming()
