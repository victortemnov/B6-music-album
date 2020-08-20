import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Album(Base):
    __tablename__ = "album"
    id = sa.Column(sa.Integer, primary_key=True)
    year = sa.Column(sa.Integer)
    artist = sa.Column(sa.Text)
    genre = sa.Column(sa.Text)
    album = sa.Column(sa.Text)


class DataBaseSession:
    """
    Adds or finds or checks for albums.
    """
    def __init__(self, db):
        self.session = connect(db)

    def find(self, artist):
        albums = self.session.query(Album).filter(Album.artist == artist).all()
        album_names = [album.album for album in albums]
        return album_names

    def add(self, album_data):
        self.exist(album_data)
        self.session.add(album_data)
        self.session.commit()

    def exist(self, album_data):
        if self.session.query(Album).filter(Album.album == album_data.album).first():
            raise DuplicateAlbumError()


def connect(DB_PATH):
    Engine = sa.create_engine(DB_PATH)
    Session = sessionmaker(Engine)
    return Session()


class DuplicateAlbumError(Exception):
    pass
