import csv
from datetime import datetime
from celery import shared_task
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)

@shared_task
def upload_location_file(user_id, tenant_id, file, module_name, class_name):
    with open(file) as f:
        logger.info('Upload file task started at '+datetime.now())
        csv_reader = csv.DictReader(f)
        column_names = list(dict(list(csv_reader)[0]).keys())
        reader = csv.reader(f)
