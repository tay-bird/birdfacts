import boto3


def read_from_s3(bucket, key):
    client = boto3.client('s3')

    _object = client.get_object(
        Bucket=bucket,
        Key=key)

    content = _object['Body'].read()
    return content
