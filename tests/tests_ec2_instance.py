import time

import moto
import unittest

from aws_app.ec2_service import Ec2Service


class Ec2Test(unittest.TestCase):
    def setUp(self) -> None:
        self.my_ec2 = Ec2Service()

    @moto.mock_ec2
    def test_ec2_all(self):
        # create one ec2 instance
        response = self.my_ec2.create_instance()
        instanceId = response['Instances'][0]['InstanceId']
        self.assertEqual(type(instanceId), str)

        # Checking status of instance. should be pending. {'Code': 0, 'Name': 'pending'}
        state_ac2_after_create = response['Instances'][0]['State']
        self.assertEqual(state_ac2_after_create['Name'], 'pending')

        # Needed to wait 5 sec for starting system -> 'State':running
        time.sleep(5)
        state_ = self.my_ec2.get_one_instance_status(instanceId)
        self.assertEqual(state_, 'running')

        # Try to stop instanse
        self.my_ec2.stop_instance(instanceId)
        response_stop = self.my_ec2.get_one_instance_status(instanceId)
        self.assertEqual(response_stop, 'stopped')

        # Try to start instance
        self.my_ec2.start_instance(instanceId)
        time.sleep(5)
        status = self.my_ec2.get_one_instance_status(instanceId)
        self.assertEqual(status, 'running')

        # list of all instances
        result_all_inst = self.my_ec2.all_instances()
        self.assertEqual(len(result_all_inst), 1)


if __name__ == '__main__':
    unittest.main()
