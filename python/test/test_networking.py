""" Unit tests for the networking module. """

import unittest
from api.networking import CidrMaskConvert, IpValidate

class TestNetworkingMethods(unittest.TestCase):
    """ Tests for networking methods. """
    def setUp(self):
        self.networking = CidrMaskConvert()
        self.validate = IpValidate()

    def test_valid_cidr_to_mask(self):
        """ Test a valid conversion from CIDR to network mask. """
        self.assertEqual("128.0.0.0", self.networking.cidr_to_mask("1"))

    def test_valid_mask_to_cidr(self):
        """ Test a valid conversion from network mask to CIDR. """
        self.assertEqual("1", self.networking.mask_to_cidr("128.0.0.0"))

    def test_invalid_cidr_to_mask(self):
        """ Test an invalid conversion from CIDR to network mask. """
        self.assertEqual("Invalid", self.networking.cidr_to_mask("0"))

    def test_invalid_mask_to_cidr(self):
        """ Test an invalid conversion from network mask to CIDR. """
        self.assertEqual("Invalid", self.networking.mask_to_cidr("0.0.0.0"))

    def test_valid_ipv4(self):
        """ Test a valid IPV4. """
        self.assertTrue(self.validate.ipv4_validation("127.0.0.1"))

    def test_invalid_ipv4(self):
        """ Test an invalid IPV4. """
        self.assertFalse(self.validate.ipv4_validation("192.168.1.2.3"))


if __name__ == "__main__":
    unittest.main()
