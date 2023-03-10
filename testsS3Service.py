import os
import unittest
from dotenv import load_dotenv
from aws_app.main import S3Service

load_dotenv()


class S3serviceTest(unittest.TestCase):

    def setUp(self) -> None:
        self.BUCKET_NAME = os.environ.get("BUCKET_NAME")
        ACCESS_KEY = os.environ.get("ACCESS_KEY")
        SECRET_ACCESS_KEY = os.environ.get("SECRET_ACCESS_KEY")
        if SECRET_ACCESS_KEY and ACCESS_KEY:
            self.my_service = S3Service(
                access_key=ACCESS_KEY,
                secret_access_key=SECRET_ACCESS_KEY
            )

    def test_create_bucket(self):
        result = self.my_service.create_new_bucket(
            bucket_name=self.BUCKET_NAME,
            region='eu-west-2')
        self.assertEqual(result, True)

    def test_put_file(self):
        file_name = 'file_3'
        bucket = self.BUCKET_NAME
        #  file_3 should exist.  Located  in /media folder
        result = self.my_service.put_file(
            file_name=file_name,
            bucket=bucket
        )
        self.assertEqual(result, True)
        # get list of all objects from bucket
        objs = self.my_service.s3_client.list_objects(Bucket=bucket)
        list_keys_in_bucket = [obj['Key'] for obj in objs['Contents']]

        # checking if file was uploaded to service
        result_upload = file_name in list_keys_in_bucket
        self.assertEqual(result_upload, True)

    def test_get_file(self):
        result_get = self.my_service.get_file(
            bucket_name=self.BUCKET_NAME,
            object_name='file_3')
        self.assertEqual(result_get, True)

        # check if file exist (was downloaded Succcessfully)
        file_path = './media/' + 'file_3'
        self.assertEqual(os.path.exists(file_path), True)


if __name__ == '__main__':
    unittest.main()
