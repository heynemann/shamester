#!/usr/bin/python
# -*- coding: utf-8 -*-

from os.path import abspath, join, dirname

import tornado.web
from cow.server import Server
from cow.plugins.motor_plugin import MotorPlugin
from cow.plugins.redis_plugin import RedisPlugin

from shamester_api.handlers.new_website_handler import NewWebsiteHandler


def main():
    ShamesterApiServer.run()


class ShamesterApiServer(Server):
    def get_handlers(self):
        web_path = abspath(join(dirname(__file__), '..', 'shamester-web', 'dist'))

        handlers = [
            ('/web/(.*)', tornado.web.StaticFileHandler, {'path': web_path}),
            ('/websites/new/?', NewWebsiteHandler),
        ]

        return tuple(handlers)

    def get_plugins(self):
        return [
            MotorPlugin,
            RedisPlugin
        ]


if __name__ == '__main__':
    main()
