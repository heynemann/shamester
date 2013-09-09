#!/usr/bin/python
# -*- coding: utf-8 -*-

from os.path import abspath, dirname, join

web_root_path = abspath(join(dirname(__file__), '..', '..', 'shamester-web', 'dist'))

from derpconf.config import Config

Config.define('MONGOHOST', 'localhost', "Database configuration", "Database")
Config.define('MONGOPORT', 6680, "Database configuration", "Database")
Config.define('MONGODATABASE', 'shamester', "Database configuration", "Database")

Config.define('REDISHOST', 'localhost', "Database configuration", "Database")
Config.define('REDISPORT', 7777, "Database configuration", "Database")

Config.define('WEB_ROOT_PATH', web_root_path, "Root path for the web app.", "Web")
Config.define('ENVIRONMENT', 'local', "Defines the javascript include to be used.", "Web")
