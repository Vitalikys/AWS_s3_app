import boto3
import moto
import unittest

from aws_app.cloudwatch_service import CloudwatchService


class CloudWatchServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.my_cloud_watch = CloudwatchService()
        self.my_ec2 = boto3.client('ec2', region_name="eu-west-1")

    @moto.mock_ec2
    def test_all(self):
        # create one ec2 instance
        response = self.my_ec2.run_instances(
            ImageId='string',
            InstanceType='a1.medium',
            MaxCount=1,
            ClientToken='string',
            MinCount=1,
            Placement={
                'AvailabilityZone': 'eu-west-1a',
                'Affinity': 'string',
                'GroupName': 'string',
                'PartitionNumber': 123,
                'HostId': 'string',
                'Tenancy': 'default',
                'SpreadDomain': 'string',
                'HostResourceGroupArn': 'string',
                'GroupId': 'string'
            })
        instanceId = response['Instances'][0]['InstanceId']
        self.assertEqual(type(instanceId), str)
        print('instanceId = ', instanceId)

        # time.sleep(5)
        # resp_describe = self.my_ec2.describe_instances(
        #     InstanceIds=[
        #        instanceId,
        #     ],
        #     DryRun=False,
        #     MaxResults=123,
        # )
        # print(resp_describe)


        # test RAM usage
        response = self.my_cloud_watch.get_ram_usage(instance_id=instanceId)
        self.assertEqual(type(response), str)


        # test CPU usage
        # response_cpu = self.my_ec2.get_instance_cpu_usage(instance_id=instanceId)
        # print(response_cpu)
        # self.assertEqual(1,1)

