from datetime import datetime, timedelta, timezone

import boto3


class CloudwatchService:
    def __init__(self, region="eu-west-1"):
        self.region = region
        self._cloud_watch_client = None

    @property
    def cloud_watch_client(self):
        if not self._cloud_watch_client:
            self._cloud_watch_client = boto3.client("cloudwatch", region_name=self.region)
        return self._cloud_watch_client

    def get_ram_usage(self, instance_id: str):
        """ # https: // boto3.amazonaws.com / v1 / documentation / api / latest / reference / services / cloudwatch / client / get_metric_data.html
            Function to get RAM usage
        :param instance_id:
        :return:
        """
        response = self.cloud_watch_client.get_metric_data(
            MetricDataQueries=[
                {
                    'Id': instance_id,
                    'MetricStat': {
                        'Metric': {
                            'Namespace': 'AWS/EC2',
                            'MetricName': 'MemoryUtilization',
                            'Dimensions': [
                                {
                                    'Name': 'InstanceId',
                                    'Value': instance_id
                                },
                            ]
                        },
                        'Period': 60,
                        'Stat': 'Average',
                        'Unit': 'Percent'
                    },
                    'ReturnData': True,
                    'Period': 60,
                    'AccountId': 'string'
                },
            ],
            StartTime=datetime.now() - timedelta(seconds=60),
            EndTime=datetime.now(),
            # NextToken='string',
            ScanBy='TimestampDescending',
            MaxDatapoints=13,
            # LabelOptions={'Timezone': 'timezone'}
        )
        return response['MetricDataResults']['Values'][0]


