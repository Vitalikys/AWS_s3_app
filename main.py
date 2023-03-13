from aws_app.s3_service import S3Service


if __name__ == '__main__':
    bucket_name= 'new_bucket_one'
    my_s3 = S3Service()

    my_s3.create_new_bucket(bucket_name=bucket_name)
    my_s3.put_file(file_name='file_3', bucket=bucket_name)
    my_s3.get_file(object_name='file_3', bucket_name=bucket_name)

    