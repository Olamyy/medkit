import random
from core.engines import DatabaseEngine, FileEngine, UrlEngine


class Parser(object, DatabaseEngine, FileEngine, UrlEngine):
    """
    Jabb parser class.
    Would handle parsing object into the analyze.
    Carries out a number of actions on the object before analyzing them.
    """

    def __init__(self, **data):
        super(Parser, self).__init__()
        self.data = data
        self.engine = self.data.get('engine', None)

    def __repr__(self):
        return self.__class__

    def get_engine(self):
        if self.engine == "database":
            pass
        elif self.engine == "url":
            pass
        else:
            pass

