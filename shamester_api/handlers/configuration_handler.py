#!/usr/bin/python
# -*- coding: utf-8 -*-

from tornado.web import RequestHandler

CONFIGURATION_KEYS = [
    'ENVIRONMENT',
]


class ConfigurationHandler(RequestHandler):

    def get(self, environment):
        configurations = [
            ".constant('%s', '%s')" % (
                value,
                getattr(self.application.config, value)
            )
            for value in CONFIGURATION_KEYS
        ]

        template = """
            (function() {
              angular.module('configuration')
                  %s;

            }).call(this);
        """ % (
            "\n".join(configurations)
        )
        self.write(template)
