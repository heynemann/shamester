#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cow.testing import CowTestCase
from preggy import expect
from tornado.concurrent import return_future

from tracking.server import TrackingServer
from tracking.config import Config
from tests.fixtures.cab_driver import get_cab_driver


class MockPusher(object):
    def __init__(self):
        self.calls = []

    @return_future
    def publish(self, channel, event_name, event_data, callback):
        self.calls.append((
            channel, event_name, event_data
        ))
        callback(True)


class TestStatusHandler(CowTestCase):
    def setUp(self):
        super(TestStatusHandler, self).setUp()

        self.pusher = MockPusher()
        self.server.application.pusher = self.pusher

    def get_server(self):
        cfg = Config(
            MONGOHOST="localhost",
            MONGOPORT=27017,
            MONGODATABASE="tracking_test",
            PUSHER_APP_ID="47297",
            PUSHER_KEY="317499100685e39db0c1",
            PUSHER_SECRET="64e29b28a8120e666b2e"
        )

        self.server = TrackingServer(config=cfg)
        return self.server

    def stop(self, *args, **kwargs):
        '''Stops the ioloop, causing one pending (or future) call to wait()
        to return.

        Keyword arguments or a single positional argument passed to stop() are
        saved and will be returned by wait().
        '''
        self._AsyncTestCase__stop_args = {
            'args': args,
            'kwargs': kwargs
        }

        # hack to support many arguments in stop
        if self._AsyncTestCase__running:
            self.io_loop.stop()
            self._AsyncTestCase__running = False
        self._AsyncTestCase__stopped = True

    def test_change_status(self):
        driver = get_cab_driver(driver_pk="508fefa76e77c3190500025f")
        coll = self.server.application.mongo.tdespatch_cabdriver

        del driver['_id']

        coll.insert(driver, callback=self.stop)
        response = self.wait()
        driver_pk = response['args'][0]

        response = self.fetch(
            '/change-status/%s' % str(driver_pk),
            method="POST",
            body='new_status=on_way_to_job&device_type=android',
        )['args'][0]

        expect(response.code).to_equal(200)
        expect(response.body).to_be_like('OK')

        coll.find_one({'_id': driver_pk}, callback=self.stop)
        driver_obj = self.wait()['args'][0]

        expect(driver_obj['simple_status']).to_equal('on_way_to_job')
        expect(driver_obj['device_type']).to_equal('android')
        expect(driver_obj['offline']).to_be_false()

    def test_empty_drop_minutes(self):
        driver = get_cab_driver(driver_pk="508fefa76e77c31905000250")
        coll = self.server.application.mongo.tdespatch_cabdriver

        del driver['_id']

        coll.insert(driver, callback=self.stop)
        response = self.wait()
        driver_pk = response['args'][0]

        response = self.fetch(
            '/change-status/%s' % str(driver_pk),
            method="POST",
            body='new_status=drop&drop_minutes=&device_type=android',
        )['args'][0]

        expect(response.code).to_equal(400)
        expect(response.body).to_be_like('INVALID')

    def test_invalid_status(self):
        driver = get_cab_driver(driver_pk="508fefa76e77c31905000251")
        coll = self.server.application.mongo.tdespatch_cabdriver

        del driver['_id']

        coll.insert(driver, callback=self.stop)
        response = self.wait()
        driver_pk = response['args'][0]

        response = self.fetch(
            '/change-status/%s' % str(driver_pk),
            method="POST",
            body='new_status=linus&device_type=android',
        )['args'][0]

        expect(response.code).to_equal(400)
        expect(response.body).to_be_like('INVALID')

    def test_invalid_sms(self):
        driver = get_cab_driver(driver_pk="508fefa76e77c31905000251")
        coll = self.server.application.mongo.tdespatch_cabdriver

        del driver['_id']

        coll.insert(driver, callback=self.stop)
        response = self.wait()
        driver_pk = response['args'][0]

        response = self.fetch(
            '/change-status/%s' % str(driver_pk),
            method="POST",
            body='new_status=sms&device_type=android',
        )['args'][0]

        expect(response.code).to_equal(400)
        expect(response.body).to_be_like('INVALID')

    def _test_invalid_novehicle(self): # TODO
        driver = get_cab_driver(driver_pk="508fefa76e77c31905000251")
        coll = self.server.application.mongo.tdespatch_cabdriver

        del driver['_id']

        coll.insert(driver, callback=self.stop)
        response = self.wait()
        driver_pk = response['args'][0]

        response = self.fetch(
            '/change-status/%s' % str(driver_pk),
            method="POST",
            body='new_status=no_vehicle&device_type=android',
        )['args'][0]

        expect(response.code).to_equal(400)
        expect(response.body).to_be_like('INVALID')

