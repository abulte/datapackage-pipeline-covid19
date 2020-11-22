web: gunicorn -b 0.0.0.0:5000 datapackage_pipelines.web:app
scheduler: bash run-scheduler.sh
worker: python -m celery -b $DPP_CELERY_BROKER -A datapackage_pipelines.app -Q datapackage-pipelines-management,datapackage-pipelines -l INFO worker