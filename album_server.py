from bottle import HTTPError
from bottle import request
from bottle import route
from bottle import run


from album_database import DataBaseSession, Album, DuplicateAlbumError


DB_PATH = "sqlite:///albums.sqlite3"
db = DataBaseSession(DB_PATH)


class YearValueError(Exception):
    pass


class EmptyValueError(Exception):
    pass


@route("/albums/<artist>")
@route("/albums/<artist>/")
def albums(artist):
    """
    Returns a list of all artist's albums in database.
    """
    albums = db.find(artist)
    if not albums:
        error_message = f"***No albums for {artist}***"
        return HTTPError(404, error_message)
    html_message = into_html(artist, albums)
    return html_message


def into_html(artist, albums):
    """
    Make HTML from artist's albums.
    """
    albums_count = len(albums)
    albums_list = [f"<li>{album}</li>" for album in albums]
    albums_list = "".join(albums_list)
    html_message = f"<strong>{artist}</strong> has {albums_count} album(s):<br><ul>{albums_list}</ul>"
    return html_message


@route("/albums", method="POST")
@route("/albums/", method="POST")
def add():
    """
    Adds new album to the database.
    Returns 400 error if received values are not valid.
    Returns 409 error if the album is already in the database.
    """
    try:
        album_data = request_data()
        db.add(album_data)
    except EmptyValueError:
        return HTTPError(400, "Album or artist cannot be empty")
    except YearValueError:
        return HTTPError(400, "Invalid year value")
    except DuplicateAlbumError:
        error_message = f"Album '{album_data.album}' has been already added"
        return HTTPError(409, error_message)
    else:
        return f"Album '{album_data.album}' by {album_data.artist} has been successfully added."


def request_data():
    """
    Parses data from POST-request.
    """
    album = request.forms.get("album")
    artist = request.forms.get("artist")
    genre = request.forms.get("genre")
    year = request.forms.get("year")
    album = Album(
        album=album,
        artist=artist,
        genre=genre,
        year=year
    )
    valid(album)
    return album


def valid(album):
    """
    Checks if received values are valid.
    """
    if not album.artist or not album.album:
        raise EmptyValueError()
    try:
        if album.year is not None and int(album.year) < 1900:
            raise YearValueError()
    except ValueError:
        raise YearValueError()


if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)
    