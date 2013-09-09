import ConfigParser


class Config(object):
    config = None
    defaults = {
                "sleep_time": "60"
            }

    def __init__(self, filename):
        self.config = ConfigParser.SafeConfigParser(defaults=self.defaults)
        self.config.read(filename)


    def getint(self, option):
        try:
            return self.config.getint('MAIN', option)
        except:
            return self.config.getint('DEFAULT', option)