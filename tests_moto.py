import unittest
import os

from dotenv import load_dotenv
from moto import mock_s3
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

        # check if bucket exists (was created). Using head_bucket
        response = self.my_service.s3_client.head_bucket(Bucket=self.BUCKET_NAME)
        response_code = response['ResponseMetadata']['HTTPStatusCode']
        self.assertEqual(response_code, 200)

        # try to upload NOT EXIST file
        with self.assertRaises(FileNotFoundError):
            self.my_service.put_file(
                file_name='file_4',
                bucket=self.BUCKET_NAME
            )

        # try to upload  file EXIST
        result_bool = self.my_service.put_file(
            file_name='file_3',
            bucket=self.BUCKET_NAME
        )
        self.assertEqual(result_bool, True)

        # check if file exist on S3 server
        result_exist = self.my_service.s3_client.get_object(
            Bucket=self.BUCKET_NAME,
            Key='file_3'
        )
        self.assertTrue(result_exist, msg='Check if file exist on S3 server')


if __name__ == '__main__':
    unittest.main()
