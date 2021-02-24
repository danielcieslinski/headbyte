import fire
from src.bookmarks_import import JSONBookmarksImporter

class Headbyte(object):
    bookmarks = JSONBookmarksImporter

if __name__ == '__main__':
    fire.Fire(Headbyte)
