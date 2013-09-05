#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

import motor
from cow.testing import CowTestCase
from preggy import expect
try:
    from tornado.concurrent import return_future
except ImportError:  # This is in case of Tornado's older versions
    return_future = lambda func: func

from tracking.server import TrackingServer
from tracking.config import Config
#from tracking.models import Booking
from tracking.client import TrackingClient


class MockPusher(object):
    def __init__(self):
        self.calls = []

    @return_future
    def publish(self, channel, event_name, event_data, callback):
        self.calls.append((
            channel, event_name, event_data
        ))
        callback(True)


class TestTrackingClientWithMockPusher(CowTestCase):
    def setUp(self):
        super(TestTrackingClientWithMockPusher, self).setUp()

        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        self.pusher = MockPusher()
        self.server.application.pusher = self.pusher

        # Cleaning test database after tests
        motor.Op(self.server.application.mongo.trackings.remove)
        motor.Op(self.server.application.mongo.tdespatch_cabdriver.remove)

    def get_server(self):
        cfg = Config(
            PUSHER_APP_ID="mock-app-id",
            PUSHER_KEY="mock-key",
            PUSHER_SECRET="mock-secret",
            MONGOHOST="localhost",
            MONGOPORT=27017,
            MONGODATABASE="tracking",
        )

        self.server = TrackingServer(config=cfg)
        self.server.debug = False
        return self.server

    def test_change_status_with_client(self):
        client = TrackingClient(base_url=self.get_url('/'), io_loop=self.io_loop)

        client.change_driver_status(
            driver_pk='505978566e77c33341000610',
            data={"new_status": "available", "device_type": "android"},
            callback=self.stop
        )
        result = self.wait()
        expect(result).to_be_true()

        expect(self.pusher.calls).to_length(1)

        call = list(self.pusher.calls[-1])
        call = tuple(call)
        expect(call).to_be_like(
            (
                u'driver_status', 'new_status', {
                    'status': 'driver_online',
                    'driver_pk': u'505978566e77c33341000610',
                    'driver_device': u'android'
                }
            )
        )

        cursor = self.server.application.mongo.trackings.find().sort([('_id', -1)]).limit(1)
        while (yield cursor.fetch_next):
            pass

    def test_update_driver_location_with_client(self):
        client = TrackingClient(base_url=self.get_url('/'), io_loop=self.io_loop)

        client.update_driver_location(
            driver_pk='505978566e77c33341000610',
            data={"latitude": 52.573012, "longitude": 13.6203},
            callback=self.stop
        )
        result = self.wait()
        expect(result.code).to_equal(200)
        expect(result.body).to_equal('OK')

        expect(self.pusher.calls).to_length(1)

        call = list(self.pusher.calls[-1])
        call = tuple(call)
        expect(call).to_be_like(
            (u'driver_location', 'new_location', {'lat': 52.573012, 'lng': 13.6203})
        )

    def test_get_driver_location_with_client(self):
        client = TrackingClient(base_url=self.get_url('/'), io_loop=self.io_loop)
        driver_pk = '505978566e77c33341000611'

        client.update_driver_location(
            driver_pk=driver_pk,
            data={"latitude": 52.573012, "longitude": 13.6203},
            callback=self.stop
        )
        result = self.wait()
        expect(result.code).to_equal(200)
        expect(result.body).to_equal('OK')

        client.get_driver_location(
            driver_pk=driver_pk,
            callback=self.stop
        )
        result = self.wait()
        expect(result).not_to_be_null()

        expect(result[0]["tracking_id"]).to_equal(driver_pk)
        expect(result[0]["location"]).to_be_like({'lat': 52.573012, 'lng': 13.6203})
        expect(result[0]["timestamp"]).to_be_true()
