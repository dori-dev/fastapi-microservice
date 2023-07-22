# Simple Microservice

The simple microservice project that use `FastAPI` and `RabbitMQ`.

# Usage

Run RabbitMQ server.

```bash
docker-compose up -d
```

Run the rpc servers.

```bash
python rpc/server.py
```

```bash
python rpc/notification_server.py
```

Run the application

```bash
uvicorn app:main --reload
```

Home Page: [localhost:8000/fib/10](http://localhost:8000/fib/10/)<br>
