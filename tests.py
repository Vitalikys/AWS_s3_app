import unittest
from aws_app.main import S3Service

class S3servTest(unittest.TestCase):

    def setUp(self) -> None:
        self.my_service = S3Service()

    def test_create_bucket(self):
        result = self.my_service.create_bucket(bucket_name='astest-bucket', region='eu-west-2')
        self.assertEqual(result, True)

    def test_upload_file(self):
        result = self.my_service.upload_file('./file_2', 'vitalii-bucket')
        self.assertEqual(result, True)

    # my_service.download_file(object_name='file_2', bucket_name='vitalii-bucket')


