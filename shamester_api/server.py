#!/usr/bin/python
# -*- coding: utf-8 -*-

from os.path import abspath, join, dirname

import tornado.web
from cow.server import Server
from cow.plugins.motor_plugin import MotorPlugin
from cow.plugins.redis_plugin import RedisPlugin

from shamester_api.handlers.new_website_handler import NewWebsiteHandler


class StaticIndexHandler(tornado.web.StaticFileHandler):
    @classmethod
    def get_absolute_path(cls, root, path):
        if path == '/' or path == '':
            path = "index.html"

        return super(StaticIndexHandler, cls).get_absolute_path(root, path.lstrip('/'))


def main():
    ShamesterApiServer.run()


class ShamesterApiServer(Server):
    def get_handlers(self):
        web_path = abspath(join(dirname(__file__), '..', 'shamester-web', 'dist'))

        handlers = [
            ('/websites/new/?', NewWebsiteHandler),
            ('(.*)/?', StaticIndexHandler, {"path": web_path}),
        ]

        return tuple(handlers)

    def get_settings(self):
        settings = super(ShamesterApiServer, self).get_settings()
        del settings['static_path']
        return settings

    def get_plugins(self):
        return [
            MotorPlugin,
            RedisPlugin
        ]


if __name__ == '__main__':
    main()
