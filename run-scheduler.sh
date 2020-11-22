#!/usr/bin/env bash

# we need a wrapper for SCHEDULER=1
SCHEDULER=1 python -m celery -b $DPP_CELERY_BROKER -A datapackage_pipelines.app -l INFO beat