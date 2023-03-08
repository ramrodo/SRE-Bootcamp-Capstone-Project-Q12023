""" Classes for networking module. """
from socket import inet_ntoa
from struct import pack
from ipaddress import ip_address

class CidrMaskConvert:
    """ Convertion between CIDR and mask. """
    def cidr_to_mask(self, cidr):
        """" Convert CIDR to mask. """
        host_bits = 32 - int(cidr)
        mask = inet_ntoa(pack("!I", (1 << 32) - (1 << host_bits)))

        if mask == "0.0.0.0":
            return "Invalid"

        return mask

    def mask_to_cidr(self, mask):
        """" Convert mask to CIDR. """
        cidr = str(sum(bin(int(x)).count("1") for x in mask.split(".")))

        if cidr == "0":
            return "Invalid"

        return cidr

class IpValidate:
    """ IP Validation. """
    def ipv4_validation(self, address):
        """ Validate IPV4 address. """
        try:
            ip_address(address)
            return True
        except ValueError:
            return False
