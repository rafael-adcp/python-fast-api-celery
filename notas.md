https://flower.readthedocs.io/en/latest/prometheus-integration.html#start-flower-monitoring


# command=celery 
#     --app=%(ENV_CELERY_APP_PATH)s worker
#     --loglevel=%(ENV_CELERY_LOG_LEVEL)s
#     --concurrency=%(ENV_CELERY_PROCESSES)s
#     -Ofair
#     -Q %(ENV_CELERY_QUEUE)s
#     -n %(ENV_CELERY_QUEUE)s-worker@%%h




# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std-setting-worker_prefetch_multiplier
app.conf.worker_prefetch_multiplkier = 1

class DefaultWorkerConfig(Task):
    max_retries = 10
    task_reject_on_worker_lost = True

    # leaves the msg unacked until the worker finishes / errors
    acks_late = True

    # auto retry on given exceptions
    autoretry_for=[Exception]

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print("error on")
        print(self.__dict__['__qualname__'])
        print(self)
        print(args)
        print(kwargs)
        print(einfo)
