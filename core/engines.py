import os
import dataset
from subprocess import getoutput
from core.errors import InvalidFreezeFileError, InvalidQueryError, InvalidFileExtension, InvalidURLError
from urllib.request import urlopen


class DatabaseEngine:
    """
    Database Interfacing Engine.
    Connects to the database(Mysql) and export the data in a table into a csv file for further reading.
    """

    def __init__(self, **kwargs):
        self.db = dataset.connect('mysql://{0}:{1}@{2}/{3}'.format(kwargs.get('user', 'root'),
                                                                   kwargs.get('password', 'lekan'),
                                                                   kwargs.get('host', 'localhost'),
                                                                   kwargs.get('db_name', 'information_schema')))

    def export_from_terminal(self, freezefile_path):
        """
        This would attempt to export the database content into csv using the
        dataset *datafreeze* command.
        The dataset documentation has more details on using freezefiles.
        :param freezefile: With .yaml extension
        :return:
        """
        if not freezefile_path.endswith('.yaml') and not os.path.isfile(freezefile_path):
            raise InvalidFreezeFileError("Invalid freezefile.")
        print("Exporting database ...")
        return getoutput("datafreeze freezefile.yaml")

    def export_from_script(self, table):
        """
        Exports the table provided.
        :param table:
        :return:
        """
        query = self.db[table]
        print(query)
        if not query:
            print("DB")
            raise InvalidQueryError("The DB Query is Invalid")
        else:
            print("Let")
            try:
                dataset.freeze(query, format='csv', filename='data/data.csv')
                print("Here")
            except Exception as error:
                print("Whe")
                return error


class FileEngine:
    def __init__(self, **kwargs):
        self.file_name = kwargs.get('filename')
        self._decypher_extension()

    def _decypher_extension(self):
        valid_file_extensions = ['xlsx', 'csv']
        valid_image_extensions = ['img', 'png', 'jpeg', 'jpg']
        file, extension = os.path.splitext(self.file_name)
        if extension not in valid_file_extensions and valid_image_extensions:
            raise InvalidFileExtension("The extension {0} is not valid extension".format(extension))
        elif extension in valid_file_extensions:
            self._validate_text_file()
        else:
            self._validate_image_file()

    def _validate_text_file(self):
        pass

    def _validate_image_file(self):
        pass


class UrlEngine:
    def __int__(self, **kwargs):
        self.url = kwargs.get('url', None)
        if self._url_exists():
            self._validate_url()
        else:
            raise InvalidURLError("The url '{0}' is not valid.".format(self.url))

    def _http_add_remove(self, url):
        http = '.http://'
        if url.startswith(http):
            return url
        else:
            url = "{0}{1}".format(http, url)
            return url

    def _url_exists(self):
        url = self._http_add_remove(self.url)
        if (urlopen(url).code / 100) >= 4:
            return False
        else:
            return True

    def _validate_url(self):
        pass
