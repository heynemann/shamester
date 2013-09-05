#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import abspath, dirname, join

FIXTURE_ROOT_PATH = abspath(dirname(__file__))


def read_fixture(name):
    with open(join(FIXTURE_ROOT_PATH, name), 'r') as fixture:
        return fixture.read()
