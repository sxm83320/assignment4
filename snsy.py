import boto3

sns_client = boto3.client('sns', region_name='us-east-1')

response = sns_client.create_topic(
    Name='My-test'
)

topic_arn = response['TopicArn']
response = sns_client.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint='sxm83320@ucmo.edu'
)


response = sns_client.publish(
    TopicArn=topic_arn,
    Subject='Test message',
    Message='Hello from Python!'
)
