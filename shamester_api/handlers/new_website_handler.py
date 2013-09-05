#!/usr/bin/python
# -*- coding: utf-8 -*-

from tornado.web import RequestHandler, asynchronous
import tornado.gen
import motor

from shamester_api.models import Website


class NewWebsiteHandler(RequestHandler):
    @property
    def websites(self):
        return self.application.mongo.websites

    @asynchronous
    @tornado.gen.coroutine
    def post(self):
        url = self.get_param('url')

        website = Website(url=url)

        website_data = website.to_dict()

        yield motor.Op(self.websites.insert, website_data)

        self.application.redis.publish("new-website", website_data)

        self.write("OK")
        self.finish()
