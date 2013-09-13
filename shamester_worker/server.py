#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
import logging

from optparse import OptionParser
from config import Config, verify_and_load

LOGS = {
    0: 'error',
    1: 'warning',
    2: 'info',
    3: 'debug'
}

class ShamesterWorkerServer(object):
    config = None
    validators = set()


    def __init__(self, opt):
        self.config = verify_and_load(opt.conf)

        if opt.verbose:
            log_level = LOGS[opt.verbose].upper() 
        else: 
            log_level = self.config.get("LOG_LEVEL")

        logging.basicConfig(
            level=log_level,
            format=self.config.get("LOG_FORMAT"),
            datefmt=self.config.get("LOG_DATE_FORMAT")
        )

        self.validators.add("validators.base.ValidatorBase")
        for validator in self.config.get("VALIDATORS"):
            self.validators.add(validator)

        logging.debug("Will validate using %s" % self.validators)


    def run(self):
        try:
            while True:
                websites = self.check_new_websites()
                for website in websites:
                    logging.debug("Processing [%s]" % website)
                    self.validate_website(website)


                sleep_for = self.config.get("WORKER_SLEEP_TIME")
                logging.debug("Nothing more to do. Will sleep a little bit... (%ss)" % sleep_for)
                time.sleep(sleep_for)


        except KeyboardInterrupt:
            logging.info("Gently stopped to work.\nBye.")


    def check_new_websites(self):
        logging.debug("Checking for new websites...")
        return ["http://www.globo.com", "g1.globo.com", "http://timeout.com", "http://globo.com/404"]


    def validate_website(self, website):
        for validator_full_name in self.validators:

            validator = self.new_validator(validator_full_name, website)
            if validator:
                validator.validate()

    def new_validator(self, validator_full_name, website):
        try:
            module_name, class_name = validator_full_name.rsplit('.', 1)
            
            module = __import__(module_name, globals(), locals(), class_name)
            return getattr(module, class_name)(website)

        except AttributeError, e:
            logging.warning("Could not instantiate [%s]. Ignoring. (%s)" % (validator_full_name, e))
            
            return None


def main():
    parser = OptionParser()
    
    parser.add_option('-c', '--conf', dest='conf', default='../shamester_config/local.conf',
                      help='Configuration file to use for the server.')
    parser.add_option('--verbose', '-v', action='count', help='Log level: v=warning, vv=info, vvv=debug.')
    
    (opt, args) = parser.parse_args()

    worker = ShamesterWorkerServer(opt)
    worker.run()

if __name__ == '__main__':
    main()
