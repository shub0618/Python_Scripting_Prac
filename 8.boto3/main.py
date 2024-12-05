import boto3

client = boto3.client('ec2')
response = client.run_instances(
    ImageId ='ami-0fff1b9a61dec8a5f',
    InstanceType = 't2.micro',
    KeyName ='justforlogin',
    MaxCount = 1,
    MinCount = 1
)