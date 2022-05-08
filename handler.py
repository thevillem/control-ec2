import datetime
import logging

import boto3

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ec2 = boto3.client("ec2", region_name="us-east-1")


def lookup_instance(name):
    custom_filter = [
        {"Name": "tag:Name", "Values": [f"{name}"]},
        {"Name": "tag:Terraform", "Values": ["true"]},
    ]

    ec2_query = ec2.describe_instances(Filters=custom_filter)

    matched_instances = []

    for instances in ec2_query["Reservations"]:
        for instance in instances["Instances"]:
            matched_instances.append(instance["InstanceId"])

    return matched_instances


def start(event, context):
    current_time = datetime.datetime.now().time()
    instances = lookup_instance("minecraft-server")
    ec2.start_instances(InstanceIds=instances)
    logger.info(f"started instances: {instances}")
    name = context.function_name
    logger.info(f"Your cron function {name} ran at {current_time}")


def stop(event, context):
    current_time = datetime.datetime.now().time()
    instances = lookup_instance("minecraft-server")
    ec2.stop_instances(InstanceIds=instances)
    logger.info(f"stopped instances: {instances}")
    name = context.function_name
    logger.info(f"Your cron function {name} ran at {current_time}")
