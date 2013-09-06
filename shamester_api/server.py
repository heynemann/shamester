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
        handlers = [
            #('/web/?', tornado.web.RedirectHandler, {"url": "/web/index.html"}),
            ('/websites/new/?', NewWebsiteHandler),
        ]

        return tuple(handlers)

    @property
    def static_path(self):
        web_path = abspath(join(dirname(__file__), '..', 'shamester-web', 'dist'))
        print web_path
        return web_path

    def get_settings(self):
        settings = super(ShamesterApiServer, self).get_settings()
        settings['static_url_prefix'] = '/web/'
        return settings

    def get_plugins(self):
        return [
            MotorPlugin,
            RedisPlugin
        ]


if __name__ == '__main__':
    main()
