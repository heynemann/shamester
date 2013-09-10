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


    def run(self):
        try:
            while True:
                
                websites = self.check_new_websites()
                for website in websites:
                    logging.debug("Processing [%s]" % website)

                sleep_for = self.config.get('WORKER_SLEEP_TIME')
                logging.debug("Nothing more to do. Will sleep a little bit... (%ss)" % sleep_for)
                time.sleep(sleep_for)


        except KeyboardInterrupt:
            logging.info("Gently stopped to work.\nBye.")


    def check_new_websites(self):
        logging.debug("Checking for new websites...")
        return ["www.globo.com", "g1.globo.com"]



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
