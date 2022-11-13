from celery import Celery
import os

#from app.settings import Settings

# settings = Settings()

# print(settings)


# replace with pydantic Base
broker_url = f"amqp://{os.environ['RABBIT_USER']}:{os.environ['RABBIT_PASSWORD']}@{os.environ['RABBIT_HOST']}:5672{os.environ['RABBIT_VHOST']}"
# broker='amqp://guest:guest@rabbitmq:5672/'
app = Celery(
    'tasks',
    broker=broker_url
)
print("=====" * 50)
print(broker_url)
print(os.environ['RABBIT_QUEUE_NAME'])
print("=====" * 50)

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

