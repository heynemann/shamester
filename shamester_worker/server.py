#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from optparse import OptionParser
from config import Config

class ShamesterWorkerServer(object):
    config = None

    def __init__(self, opt):
        self.config = Config(opt.conf)


    def run(self):
        try:
            while True:
                self.check_new_websites()
                sleep_for = self.config.getint('sleep_time')
                print "Nothing more to do. Will sleep a little bit... (%ss)" % sleep_for
                time.sleep(sleep_for)


        except KeyboardInterrupt:
            print "\n\nGently stopped to work."


    def check_new_websites(self):
        print "Checking for new websites..."



def main():
    parser = OptionParser()
    
    parser.add_option('-c', '--conf', dest='conf', default='config/local.conf',
                      help='Configuration file to use for the server.')
    
    (opt, args) = parser.parse_args()

    worker = ShamesterWorkerServer(opt)
    worker.run()

if __name__ == '__main__':
    main()
