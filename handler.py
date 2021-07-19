import datetime
import logging
import boto3

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
instances = ['']
ec2 = boto3.client('ec2', region_name="us-east-1")

def start(event, context):
    current_time = datetime.datetime.now().time()
    ec2.start_instances(InstanceIds=instances)
    logger.info(f"started instances: {instances}")
    name = context.function_name
    logger.info(f"Your cron function {name} ran at {current_time}")

def stop(event, context):
    current_time = datetime.datetime.now().time()
    ec2.stop_instances(InstanceIds=instances)
    logger.info(f"stopped instances: {instances}")
    name = context.function_name
    logger.info(f"Your cron function {name} ran at {current_time}")
