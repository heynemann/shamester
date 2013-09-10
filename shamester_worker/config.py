import os
from derpconf.config import Config, verify_config


Config.define('WORKER_SLEEP_TIME', 60, "Main loop sleep time", 'Worker')


def verify_and_load(config_file):
	verify_config(config_file)
	return Config.load(config_file)