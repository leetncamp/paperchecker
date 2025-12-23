#!/bin/bash
echo "celery -A tasks purge -f"
echo "redis-cli shutdown"
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
# celery -A tasks worker --concurrency=`python -c "import multiprocessing; print(int(1.6 * multiprocessing.cpu_count()))"`
celery -A tasks worker

