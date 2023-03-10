## Class S3Service
[![version](https://img.shields.io/badge/python-3.10-green)](https://semver.org)
[![version](https://img.shields.io/badge/boto%5Bs3%5D-1.26.87-green)](https://semver.org)
[![version](https://img.shields.io/badge/unittest-latest-green)](https://semver.org)


Functionality: 
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
#### create .env file with your AWS Credentials:
- BUCKET_NAME='vitalii-bucket-custom-2'
- ACCESS_KEY='AKXXXXXXXXXXXXXXXXXXX'
- SECRET_ACCESS_KEY='6xxxxxxxxxxxxxxxxxxxxxxx5WiNGo'



#### run tests with Real  Credentials (connection to AWS):
Only one file should exist in folder (before test) /media/file_3
```shell
python3 testsS3Service.py
```

#### run tests with Mock Moto (no connection to AWS):
Only one file should exist in folder (before test) /media/file_3
```shell
python3 tests_moto.py
```

