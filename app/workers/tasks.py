from celery import Celery
import os

broker_url = f"amqp://{os.environ['RABBIT_USER']}:{os.environ['RABBIT_PASSWORD']}@{os.environ['RABBIT_HOST']}:5672{os.environ['RABBIT_VHOST']}"

app = Celery(
    'tasks',
    broker=broker_url
)

@app.task(queue=os.environ['RABBIT_QUEUE_NAME'], name='hello')
def hello():
    print("inside hello worker")
    return 'hello world'

@app.task(queue=os.environ['RABBIT_QUEUE_NAME'], name='add')
def add(x, y):
    print(f'vai somart {x} e {y}')
    return x + y

# app = Celery(
#     'hello',
#     broker='amqp://guest@localhost//',
#     include=['app.workers.tasks']
# )

