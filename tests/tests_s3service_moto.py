import unittest
import os

from dotenv import load_dotenv
from moto import mock_s3
from aws_app.s3_service import S3Service

load_dotenv()


class TestS3service(unittest.TestCase):

    def setUp(self) -> None:
        self.BUCKET_NAME = os.environ.get("AWS_BUCKET_NAME")
        self.my_service = S3Service()

    @mock_s3
    def test_s3_service(self):
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

        # try to upload to S3.  file EXIST
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

        result = self.my_service.get_file(
            bucket_name=self.BUCKET_NAME,
            object_name='file_3')
        self.assertTrue(result)

        result = self.my_service.check_exist(
            bucket=self.BUCKET_NAME,
            file_name='file_3_not_exist')
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
