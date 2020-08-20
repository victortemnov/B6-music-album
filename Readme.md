# Web app

## Download:

- [**album_database.py**](https://github.com/victortemnov/music-album/blob/master/album_database.py) - module_1

- [**album_server.py**](https://github.com/victortemnov/music-album/blob/master/album_server.py) - module_2

- [*albums.sqlite3*](https://drive.google.com/file/d/1KHKrio-StI9jVIVgJH1EKaObpAFzRx25/view)  - database

### Than, run module `album_server.py`

---

***`GET`***

> Use this method to receive artist's albums
if the name of artist is composed by `one` word:

```Python
http -f GET localhost:8080/albums/Beatles
```

```Python
http -f GET localhost:8080/albums/Queen
```

> if `two-three-word` use `quotes`:

```Python
http -f GET localhost:8080/albums/"Pink Floyd"
```

```Python
http -f GET localhost:8080/albums/"Gentle Giant"
```

```Python
http -f GET localhost:8080/albums/"The Rolling Stones"
```

---

***`POST`***

> If the album isn't in the database, then it is added, if such an album already exists, raise -error-message-409-

```Python
http -f POST localhost:8080/albums artist="Disturbed" album="Ten Thousand Fists" genre="Alternative" year="2005"
```
