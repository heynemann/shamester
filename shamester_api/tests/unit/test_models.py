#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from unittest import TestCase

from preggy import expect

from tracking.models import Tracking


class TestTracking(TestCase):
    def test_can_create_tracking(self):
        tracking = Tracking(tracking_id="tracking_id", location={'lat':20.5, 'lng':30.6})
        expect(tracking).not_to_be_null()
        expect(tracking.tracking_id).to_equal("tracking_id")
        expect(tracking.location['lat']).to_equal(20.5)
        expect(tracking.location['lng']).to_equal(30.6)
        expect(tracking.timestamp).not_to_be_null()

        dt = datetime(2012, 10, 10, 10, 10, 10)
        tracking = Tracking(tracking_id="tracking_id", location={'lat':20.5, 'lng':30.6}, timestamp=dt)
        expect(tracking.timestamp).to_equal(dt)

    def test_to_timestamp_method(self):
        dt = datetime(2012, 10, 10, 10, 10, 10)
        expect(Tracking.to_timestamp(dt)).to_equal("2012-10-10 10:10:10.000000")

    def test_from_timestamp_method(self):
        dt_str = "2012-10-10 10:10:10.000000"
        dt = datetime(2012, 10, 10, 10, 10, 10)
        expect(Tracking.from_timestamp(dt_str)).to_equal(dt)

    def test_to_dict(self):
        dt_str = "2012-10-10 10:10:10.000000"
        dt = datetime(2012, 10, 10, 10, 10, 10)
        tracking = Tracking(tracking_id="tracking_id", location={'lat':20.5, 'lng':30.6}, timestamp=dt)

        expected = {
            'tracking_id': "tracking_id",
            'location': {
                'lat': 20.5,
                'lng': 30.6,
                },
            'timestamp': dt_str
        }

        expect(tracking.to_dict()).to_be_like(expected)

    def test_from_dict(self):
        dt_str = "2012-10-10 10:10:10.000000"
        expected = {
            'tracking_id': "tracking_id",
            'location': {
                'lat': 20.5,
                'lng': 30.6,
                },
            'timestamp': dt_str
        }

        tracking = Tracking.from_dict(expected)

        expect(tracking.tracking_id).to_equal("tracking_id")
        expect(tracking.location['lat']).to_equal(20.5)
        expect(tracking.location['lng']).to_equal(30.6)

        dt = datetime(2012, 10, 10, 10, 10, 10)
        expect(tracking.timestamp).to_equal(dt)
