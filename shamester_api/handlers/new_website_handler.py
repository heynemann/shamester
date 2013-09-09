#!/usr/bin/python
# -*- coding: utf-8 -*-

from tornado.web import RequestHandler, asynchronous
import tornado.gen
import motor
from ujson import loads, dumps

from shamester_api.models import Website


class NewWebsiteHandler(RequestHandler):
    @property
    def websites(self):
        return self.application.mongo.websites

    @asynchronous
    @tornado.gen.coroutine
    def post(self):
        website = loads(self.request.body)
        if website.get('url', None) is None:
            self.write(dumps({
                "success": False,
                "reason": "Url is required!"
            }))

        website = Website(url=website['url'])

        website_data = website.to_dict()

        new_website = yield motor.Op(self.websites.insert, website_data)

        self.application.redis.publish("new-website", website_data)

        self.write(dumps({
            "success": True,
            "websiteId": str(new_website)
        }))

        self.finish()
