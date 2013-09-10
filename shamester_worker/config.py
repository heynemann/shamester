import os
from derpconf.config import Config, verify_config


Config.define("WORKER_SLEEP_TIME", 60, "Main loop sleep time", "Worker")

Config.define("LOG_LEVEL", "ERROR", "Default log level", "Logging")
Config.define("LOG_FORMAT", "%(asctime)s %(name)s:%(levelname)s %(message)s", 
	"Log Format to be used when writing log messages", "Logging")
Config.define("LOG_DATE_FORMAT", "%Y-%m-%d %H:%M:%S",
    'Date Format to be used when writing log messages.', 'Logging')

def verify_and_load(config_file):
	verify_config(config_file)
	return Config.load(config_file)