import boto3

# Specify the bucket name and region
bucket_name = 'amit-bucket-020103'
region = 'us-west-2'  # Replace with your desired region

# Create an S3 client with the specified region
s3_client = boto3.client('s3', region_name=region)

# Create the bucket
try:
    s3_client.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': region
        }
    )
    print(f"Bucket '{bucket_name}' created successfully in region '{region}'!")
except Exception as e:
    print(f"Error creating bucket: {e}")