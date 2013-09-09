#!/usr/bin/python
# -*- coding: utf-8 -*-

from tornado.web import RequestHandler, asynchronous
import tornado.gen
import motor
from ujson import dumps

from shamester_api.models import Website


class HallOfShameHandler(RequestHandler):
    @property
    def websites(self):
        return self.application.mongo.websites

    @asynchronous
    @tornado.gen.coroutine
    def get(self):
        websites = []
        for website in (yield motor.Op(self.websites.find().to_list)):
            websites.append(Website.from_dict(website).to_dict())

        self.write(dumps(websites))
        self.finish()
