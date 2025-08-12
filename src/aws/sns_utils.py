import boto3

sns = boto3.client("sns")


def publish_message(topic_arn: str, subject: str, message: str):
    sns.publish(TopicArn=topic_arn, Subject=subject, Message=message)
