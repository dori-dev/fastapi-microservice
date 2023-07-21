# Simple Microservice with FastAPI & RPC

The simple microservice project that use `FastAPI` and `RabbitMQ`.

# Usage

Run RabbitMQ server.

```bash
docker-compose up -d
```

Run the rpc servers.

```bash
python rpc/server.py

# run second consumer
python3 rpc/notification_server.py

# run web server
uvicorn app:main --reload
```

Home Page: [localhost:8000/fib/5](http://localhost:8000/fib/5/)<br>
