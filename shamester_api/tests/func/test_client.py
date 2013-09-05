#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cow.server import Server
from tornado.web import RequestHandler, asynchronous

from tracking.client import TrackingClient


class TestHandler(RequestHandler):
    @asynchronous
    def get(self):
        client = TrackingClient(base_url="http://local.tdispatch.com:4444/", io_loop=self.application.io_loop)

        data = {
            "new_status": "drop",
            "drop_minutes": 10,
            "device_type": "android"
        }
        client.change_driver_status("505978566e77c33341000610", data, callback=self.handle_change_driver_status)

    def handle_change_driver_status(self, response):
        self.write("OK")
        self.finish()


class TestServer(Server):
    def get_handlers(self):
        return (
            ('/', TestHandler),
        )


if __name__ == '__main__':
    TestServer.run()
