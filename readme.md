### Class S3Service 
functionality: 

* upload file on s3 
* download file from s3
* check if file exists on s3

### How to run project
```shell
git clone https://github.com/Vitalikys/AWS_s3_app.git
cd AWS_s3_app/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
create .env file with your AWS Credentials:
BUCKET_NAME='vitalii-bucket-custom-2'
ACCESS_KEY='AKXXXXXXXXXXXXXXXXXXX'
SECRET_ACCESS_KEY='6xxxxxxxxxxxxxxxxxxxxxxx5WiNGo'


### Packages using in Project
python 3.10
moto[s3]  - for Mock AWS Services
aws 
boto3 
unittest


### run tests with Real  Credentials (connection to AWS):
Only one file should exist in folder (before test) /media/file_3
```shell
python3 testsS3Service.py
```

