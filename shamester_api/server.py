#!/usr/bin/python
# -*- coding: utf-8 -*-

from os.path import abspath, join, dirname

import tornado.web
from cow.server import Server
from cow.plugins.motor_plugin import MotorPlugin
from cow.plugins.redis_plugin import RedisPlugin

from shamester_api.handlers.new_website_handler import NewWebsiteHandler
from shamester_api.handlers.configuration_handler import ConfigurationHandler


SITE_PATHS = [
    '',
    '/',
    '/ranking'
]


class StaticIndexHandler(tornado.web.StaticFileHandler):
    @classmethod
    def get_absolute_path(cls, root, path):
        if path in SITE_PATHS:
            path = "index.html"

        return super(StaticIndexHandler, cls).get_absolute_path(root, path.lstrip('/'))

    def get(self, path, include_body=True):
        self.path = self.parse_url_path(path)
        absolute_path = self.get_absolute_path(self.root, self.path)
        self.absolute_path = self.validate_absolute_path(self.root, absolute_path)
        if self.absolute_path is None:
            return

        if path in SITE_PATHS:
            self.render(absolute_path, environment=self.application.config.ENVIRONMENT)
            return

        return super(StaticIndexHandler, self).get(path, include_body)


def main():
    ShamesterApiServer.run()


class ShamesterApiServer(Server):
    def get_handlers(self):
        web_path = abspath(join(dirname(__file__), '..', 'shamester-web', 'dist'))

        handlers = [
            ('/scripts/config-([^/]+).js', ConfigurationHandler),
            ('/websites/new/?', NewWebsiteHandler),
            ('/(.*)/?', StaticIndexHandler, {"path": web_path}),
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
