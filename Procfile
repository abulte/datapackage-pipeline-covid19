web: gunicorn -b 0.0.0.0:5000 datapackage_pipelines.web:app
scheduler: SCHEDULER=1 python -m celery -b $DPP_CELERY_BROKER -A datapackage_pipelines.app -l INFO worker -B