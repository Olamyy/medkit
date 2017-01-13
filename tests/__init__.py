from unittest import TestCase
import sqlalchemy

from core.engines import DatabaseEngine

try:
    from mock import patch, MagicMock
except ImportError:
    from unittest.mock import patch, MagicMock


class TestDatabaseEngine(TestCase):
    def testConnectionWithInvalidDetails(self):
        with self.assertRaises(sqlalchemy.exc.OperationalError):
            DatabaseEngine(user="root", host="lekan", password="tests", db_name="blablabla")
