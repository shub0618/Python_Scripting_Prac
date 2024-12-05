import boto3

client = boto3.client('ec2')
response = client.terminate_instances(
    InstanceIds= [
        'i-005c5d0fd63080a40',
   ]
)
