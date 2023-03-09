import logging
import os

import boto3
from botocore.exceptions import ClientError

import constant


# from dotenv import load_dotenv
# load_dotenv()

class S3Service:
    # ACCESS_KEY = os.environ.get("ACCESS_KEY")
    s3_client = boto3.client(
        's3',
        aws_access_key_id=constant.access_key,
        aws_secret_access_key=constant.secret_access_key
    )

    def create_bucket(self, bucket_name, region='eu-west-2'):
        """Create an S3 bucket in a specified region

        If a region is not specified, the bucket is created in the S3 default
        region (us-east-1).

        :param bucket_name: Bucket to create
        :param region: String region to create bucket in, e.g., 'us-west-2'
        :return: True if bucket created, else False
        """
        try:
            location = {'LocationConstraint': region}
            self.s3_client.create_bucket(Bucket=bucket_name,
                                         CreateBucketConfiguration=location)
        except ClientError as e:
            print(str(e))
            logging.error(e)
            return False
        return True

    def upload_file(self, file_name, bucket, object_name=None):
        """Upload a file to an S3 bucket

        :param file_name: File to upload
        :param bucket: Bucket to upload to
        :param object_name: S3 object name. If not specified then file_name is used
        :return: True if file was uploaded, else False
        """

        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = os.path.basename(file_name)

        # Upload the file
        try:
            response = self.s3_client.upload_file(file_name, bucket, object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True

    def download_file(self, bucket_name, object_name):
        """ Upload file from S3 bucket

        :param bucket_name:
        :param object_name: File to download
        :return: True if file was Dowloaded, else False
        """
        try:
            with open(object_name, 'wb') as f:
                self.s3_client.download_fileobj(bucket_name, object_name, f)
        except ClientError as e:
            logging.error(e)
            return False
        except Exception as e:
            logging.error(e)
            return False




