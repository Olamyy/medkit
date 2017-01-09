import csv

import MySQLdb


class DatabaseEngine:
    """
    Database Interfacing Engine.
    Connects to the database(Mysql) and export the data in a table into a csv file for further reading.
    """

    def __init__(self, **kwargs):
        self.db = MySQLdb.connect(host=kwargs.get('server', "localhost"), user=kwargs.get('user', "root"), password=
        kwargs.get('password', 'lekan'), database=kwargs.get('database', 'information_schema'))
        self.db_name = kwargs.get('database', 'information_schema')
        self.cursor = self.db.cursor()

    def export(self, table_name):
        self.cursor.execute("SELECT * FROM {0}.{1}".format(self.db_name, table_name))
        tables = self.cursor.fetchall()
        custom_csv = '{}_table.csv'.format(table_name)
        for table in tables:
            with open(custom_csv, 'w', newline='') as txtfile:
                txtfile.write(str(table))  # ONE RECORD FETCH
                txtfile.close()
                ###@Todo: Finish this.
                ###@
        self.cursor.close()
        self.db.close()


class FileEngine:
    def __init__(self, **kwargs):
        valid_extension = ['csv', 'xlsx', 'pnf', 'jpg']
        self.file_name = kwargs.get('filename')

    def validate_file(self):
        # if not self.file_name.endswith('.{0]'.format(extension for extension in v)):
        pass


class UrlEngine:
    def __int__(self):
        pass
