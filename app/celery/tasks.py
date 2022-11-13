from celery import Celery, Task


app = Celery(
    'tasks',
    broker='amqp://guest@localhost//',
    include=['app.celery.tasks']
)



@app.task
def hello():
    # @celery.task(name='tasks.test_tasks.test_task')
    print("Celery Task  !!!!")
    return 'hello world'