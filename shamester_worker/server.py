#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

class ShamesterWorkerServer(object):
    def run(self):
        try:
            while True:
                self.check_new_websites()
                print "Nothing more to do. Will sleep a little bit..."
                time.sleep(60)
        except KeyboardInterrupt:
            print "\n\nGently stopped to work."


    def check_new_websites(self):
        print "Checking for new websites..."



def main():
    worker = ShamesterWorkerServer()
    worker.run()

if __name__ == '__main__':
    main()
