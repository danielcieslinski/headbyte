from uuid import uuid4
from utils import *

"""
Utils regarding importing bookmarks from chromium based browsers
"""

class JSONBookmarksImporter:
    @staticmethod
    def find_bookmarks_files(search_path='~/.config', filename='Bookmarks'):
        """
        :param search_path: Path to start recurrent search at
        :param filename: file to match
        :return: List[Path]
        """
        as_path = Path(search_path)
        if search_path.startswith('~'):
            as_path = as_path.expanduser()

        found = [p.absolute() for p in as_path.rglob(filename)]
        return found

    @staticmethod
    def is_url_bookmark(x: dict):
        """
        :param x: The json elem coming from 'Bookmarks' file
        :return: True if x is valid web url
        """
        try:
            if x['type'] == 'url':
                return True
        except:
            pass
        return False

    def find_and_import(self, search_path='~/.config', filename='Bookmarks'):
        """
        :return: files, bookmarks
        """

        b_files = self.find_bookmarks_files(search_path, filename)
        integr_id = str(uuid4())
        filerecords = [{'path': str(p), 'import_id': integr_id, 'sync': True, 'add_date': get_str_now(),
                        'last_modified': get_modified_time(p)} for p in b_files]

        # 2. List of bookmarks from all browsers
        bookmarks = read_json_files(b_files)

        # 3. Filter urls
        urls = list(filter(self.is_url_bookmark, bookmarks))

        # 4. Remove duplicates
        urls = rm_dup(urls, key='url')

        # 5. Add import id
        [x.update({'import_id': integr_id}) for x in urls]

        # Remove duplicated urls (no point, to keep them)
        urls.sort(key=lambda x: x['date_added'], reverse=False)

        return filerecords, urls
