import boto3

from botocore.exceptions import ClientError, EndpointConnectionError


class Ec2Service:
    def __init__(self, region="eu-west-1"):
        self.region = region
        self._ec2_client = None
        self._account_id = None

    @property
    def ec2(self):
        if not self._ec2_client:
            self._ec2_client = boto3.client("ec2", region_name=self.region)
        return self._ec2_client

    @property
    def account_id(self) -> str:
        if not self._account_id:
            self._account_id = boto3.client('sts').get_caller_identity().get('Account')
        return self._account_id

    def get_one_instance_status(self, instance_id: str) -> str:
        response = self.ec2.describe_instance_status(InstanceIds=[instance_id])
        return response['InstanceStatuses'][0]['InstanceState']['Name']

    # def get_list_all_id_instances(self, ) -> list:
    #     """ function need to fix """
    #     responce = self.ec2.describe_images(
    #         Owners=['self'])
    #     return responce
    #     # return [responce['Images'][i]['ImageId'] for i in range(len(responce['Images']))]

    def all_instances(self) -> list:
        """
        Function to return List[ID's] of all instances.
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeInstances.html
        :return: list of all instances
        """
        response = self.ec2.describe_instances(
            DryRun=False,
            MaxResults=12
        )
        return [response['Reservations'][0]['Instances'][i]['InstanceId'] for i in range(len(response['Reservations']))]

    def start_instance(self, id_instance: str, dry_run: bool = False) -> str:
        """
        Function to Start one instance
        :param id_instance: id_instance
        :param dry_run: Checks whether you have the required permissions for the action
        :return: status
        """
        response = self.ec2.start_instances(
            InstanceIds=[id_instance],
            # AdditionalInfo='string',
            DryRun=dry_run)
        status = response['StartingInstances'][0]['CurrentState']['Name']
        return status

    def stop_instance(self,
                      instance_id: str,
                      hibernates: bool = True,
                      dry_run: bool = False,
                      force: bool = True) -> dict:
        """
        function to stop One instance
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/stop_instances.html

        :param instance_id:  instance id
        :param instanceId: str - instanceId
        :param hibernates: Сплячий режим Hibernates the instance if the instance was enabled for hibernation at launch.
        :param dry_run:
        :param force:
        :return: status
        """
        response = self.ec2.stop_instances(
            InstanceIds=[instance_id],
            Hibernate=hibernates,
            DryRun=dry_run,
            Force=force
        )
        # status = response['StoppingInstances'][0]['Name']
        return response

    def reboot_instance(self, instance_id: str) -> bool:
        try:
            response = self.ec2.reboot_instances(
                InstanceIds=[instance_id, ],
                DryRun=False
            )
            return True
        except ClientError as e:
            return e

    def create_instance(self, availib_zone: str = 'eu-west-1a') -> dict:
        try:
            responce = self.ec2.run_instances(
                ImageId='string',
                InstanceType='a1.medium',
                MaxCount=1,
                ClientToken='string',
                MinCount=1,
                Placement={
                    'AvailabilityZone': availib_zone,
                    'Affinity': 'string',
                    'GroupName': 'string',
                    'PartitionNumber': 123,
                    'HostId': 'string',
                    'Tenancy': 'default',
                    'SpreadDomain': 'string',
                    'HostResourceGroupArn': 'string',
                    'GroupId': 'string'
                })
            return responce
        except Exception as e:
            raise e
