#!/usr/bin/python
# -*- coding: utf-8 -*-

from tornado.web import RequestHandler

CONFIGURATION_KEYS = [
    'ENVIRONMENT',
]


class ConfigurationHandler(RequestHandler):

    def get(self):
        configurations = [
            ".constant('%s', '%s')" % (
                value.lower(),
                getattr(self.application.config, value)
            )
            for value in CONFIGURATION_KEYS
        ]

        template = """
          angular.module('configData', [])
              %s;
        """ % (
            "\n".join(configurations)
        )
        self.write(template)
