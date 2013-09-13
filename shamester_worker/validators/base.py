#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import requests
from requests.exceptions import MissingSchema, ConnectionError, Timeout
from requests import Response
from config import Config


class ValidatorBase(object):
    website = None
    config = None

    def __init__(self, website):
        self.website = website
        self.config = Config()

    def _get(self, address):
        response = Response()

        try:
            response = requests.get(address, timeout=self.config.get("TIMEOUT"))
        except MissingSchema:
            self._add_violations("Missing schema")

        except ConnectionError:
            self._add_violations("Address not found")

        except Timeout:
            self._add_violations("Request timeout")

        finally:
            return response

    def validate(self):
        logging.debug("Validating [%s]" % self.website)

        response = self._get(self.website)

        if response.status_code in (404, 500):
            self._add_violations("Unexpected status code, got %d " % response.status_code)

    def _add_violations(self, message):
        logging.warn("VIOLATION [%s] - %s" % (self.website, message))

