#!/usr/bin/python
# -*- coding: utf-8 -*-

from cow.server import Server
from cow.plugins.motor_plugin import MotorPlugin
from cow.plugins.redis_plugin import RedisPlugin

#from shamester_api.handlers.stream import StreamHandler


def main():
    ShamesterApiServer.run()


class ShamesterApiServer(Server):
    def get_handlers(self):
        handlers = [
            #('/stream?', StreamHandler),
        ]

        return tuple(handlers)

    def get_plugins(self):
        return [
            MotorPlugin,
            RedisPlugin
        ]


if __name__ == '__main__':
    main()
