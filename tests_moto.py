import unittest
import os

from dotenv import load_dotenv
from moto import mock_s3
import boto3
from aws_app.main import S3Service

load_dotenv()


class TestS3service(unittest.TestCase):

    def setUp(self) -> None:
        self.BUCKET_NAME = os.environ.get("BUCKET_NAME")
        ACCESS_KEY = os.environ.get("ACCESS_KEY")
        SECRET_ACCESS_KEY = os.environ.get("SECRET_ACCESS_KEY")
        if SECRET_ACCESS_KEY and ACCESS_KEY:
            self.my_service = S3Service(
                access_key=ACCESS_KEY,
                secret_access_key=SECRET_ACCESS_KEY
            )

    @mock_s3
    def test_put_file(self):
        # create bucket
        test_bucket_bool = self.my_service.create_new_bucket(
            bucket_name=self.BUCKET_NAME,
            region='eu-west-2')
        self.assertEqual(test_bucket_bool, True)

        # try to upload NOT EXIST file
        result = self.my_service.put_file(
            file_name='file_4',
            bucket=self.BUCKET_NAME
        )
        self.assertRaises(FileNotFoundError, result)


if __name__ == '__main__':
    unittest.main()
