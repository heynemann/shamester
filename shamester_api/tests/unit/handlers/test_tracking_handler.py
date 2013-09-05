#!/usr/bin/env python
# -*- coding: utf-8 -*-

from json import loads

from cow.testing import CowTestCase
from preggy import expect

from tracking.server import TrackingServer
from tracking.config import Config


class TestTrackingHandler(CowTestCase):
    def get_server(self):
        cfg = Config(
            MONGOHOST="localhost",
            MONGOPORT=27017,
            MONGODATABASE="tracking",
            PUSHER_APP_ID="47297",
            PUSHER_KEY="317499100685e39db0c1",
            PUSHER_SECRET="64e29b28a8120e666b2e"
        )

        self.server = TrackingServer(config=cfg)
        return self.server

    def test_store_tracking(self):
        response = self.fetch(
            '/',
            method="POST",
            body='tracking_id=%s&latitude=%s&longitude=%s' % (
                "505978566e77c33341000610",
                30.5,
                40.6
            )
        )

        expect(response.code).to_equal(200)
        expect(response.body).to_be_like('OK')

    def test_get_tracking_info(self):
        response = self.fetch(
            '/',
            method="POST",
            body='tracking_id=%s&latitude=%s&longitude=%s' % (
                "505978566e77c3334100061a",
                30.6,
                40.7
            )
        )

        response = self.fetch('/?id=505978566e77c3334100061a')

        expect(response.code).to_equal(200)

        items = loads(response.body)
        expect(items).to_length(1)
        expect(items[0]['location']['lat']).to_equal(30.6)
        expect(items[0]['location']['lng']).to_equal(40.7)
        expect(items[0]['timestamp']).not_to_be_null()
        expect(items[0]['tracking_id']).to_equal('505978566e77c3334100061a')
