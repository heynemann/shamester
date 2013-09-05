#!/usr/bin/python
# -*- coding: utf-8 -*-

from derpconf.config import Config

Config.define('MONGOHOST', 'localhost', "Database configuration", "Database")
Config.define('MONGOPORT', 6680, "Database configuration", "Database")
Config.define('MONGODATABASE', 'shamester', "Database configuration", "Database")

Config.define('REDISHOST', 'localhost', "Database configuration", "Database")
Config.define('REDISPORT', 7777, "Database configuration", "Database")
