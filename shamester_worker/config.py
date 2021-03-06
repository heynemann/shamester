import os
from derpconf.config import Config, verify_config


Config.define("WORKER_SLEEP_TIME", 60, "Main loop sleep time", "Worker")

Config.define("LOG_LEVEL", "ERROR", "Default log level", "Logging")
Config.define("LOG_FORMAT", "%(asctime)s:%(levelname)s %(module)s - %(message)s", 
	"Log Format to be used when writing log messages", "Logging")
Config.define("LOG_DATE_FORMAT", "%Y-%m-%d %H:%M:%S",
    "Date Format to be used when writing log messages.", "Logging")

Config.define("VALIDATORS", set(), "List of classes to validate a website", "Validators")
Config.define("TIMEOUT", 1, "Http Timeout (in seconds)", "Validators")

Config.define("MAX_PAGE_SIZE", 100, "Validates the html file size (in KB)", "Validators")

def verify_and_load(config_file):
	verify_config(config_file)
	return Config.load(config_file)