import logging
import requests

class ValidatorBase(object):
    address = None

    def __init__(self, address):
        self.address = address

    def _get(self, address):
        requests.get(address)

    def validate(self):
    	logging.debug("Validating [%s]" % self.address)

    def _add_violations(self, message):
        pass