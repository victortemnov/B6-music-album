# Temnov hw-b6-web-app

## 1. Download:

- [**album_database.py**](https://link)

- [**album_server.py**](https://link)

- [*albums.sqlite3*](https://drive.google.com/file/d/1KHKrio-StI9jVIVgJH1EKaObpAFzRx25/view)  - `database from google`

## 2. After download run module **album_server.py**

`GET`

if the `artist` name is from `one` word:

```python
http -f GET localhost:8080/albums/Beatles
```

if `two-three-word` use `quotes`:

```python
http -f GET localhost:8080/albums/"Pink Floyd"
```

```python
http -f GET localhost:8080/albums/"The Rolling Stones"
```

`POST`

```python
http -f POST localhost:8080/albums artist="Disturbed" album="Ten Thousand Fists" genre="Alternative" year="2005"
```
