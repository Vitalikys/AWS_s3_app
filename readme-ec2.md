## Class Ec2service
[![version](https://img.shields.io/badge/python-3.10-green)](https://semver.org)
[![version](https://img.shields.io/badge/boto%5Bec2%5D-1.26.87-green)](https://semver.org)
[![version](https://img.shields.io/badge/unittest-latest-green)](https://semver.org)

[ec2 boto Doc](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html)

Available statuses of instances:
'pending'|'running'|'shutting-down'|'terminated'|'stopping'|'stopped'

Functionality:

* start ec2 instance
* stop instance
* reboot instance
* get one instance status
* list all my ID's instances
* create_instance

### How to Run Tests: 
```shell
python -m unittest tests/tests_ec2_instance.py
```
## class CloudwatchService
вытянуть данные по инстансу: использование цпу диск и тд

    pending...


