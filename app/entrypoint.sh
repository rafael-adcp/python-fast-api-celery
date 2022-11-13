#!/bin/bash

# if any of the commands in your code fails for any reason, the entire script fails
set -o errexit

# fail exit if one of your pipe command fails
set -o pipefail

# exits if any of your variables is not set
set -o nounset

echo "Running entrypoint script..."

case $1 in
    api)
        echo "starting api";
        uvicorn --app-dir=.. app.api.main:app --host 0.0.0.0 --port 8080 --reload
    ;;
    flower)
        echo "starting flower";
        cd /app/workers/
        #celery --broker="${CELERY_BROKER_URL}" flower --broker_api=http://guest:guest@localhost:15672/api/
        celery -A tasks flower
    
    ;;
    worker)
        echo "starting worker";
        cd /app/workers/
        watchmedo  auto-restart -- celery -A tasks worker --loglevel=info -Q ${RABBIT_QUEUE_NAME} -Ofair --pool solo -n ${RABBIT_WORKER_NAME}
        # documentar o q eh o #     -Ofair
    ;;
    *)
        echo "Invalid option!";
        exit 1;
    ;;
esac