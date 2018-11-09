# "Restful User-Service"

## Aufgabenstellung
Die detaillierte [Aufgabenstellung](TASK.md) beschreibt die notwendigen Schritte zur Realisierung.

## Implementierung

Bei der Implementierung habe ich das Flask Restful Full Example, als Basis genommen und für meine Applikation geändert. Die wichtigsten Eigenschaften die ich zum Code hinzugefügt habe, sind die extra Argumente die benötigt werden damit der User mehrere Attribute haben kann.

    parser.add_argument('username')
    parser.add_argument('email')
    parser.add_argument('picture')

### CRUD Funktionen
Zum Aufrufen aller User.
`curl http://localhost:5000/users`

Zum Aufrufen eines bestimmten User.
`curl http://localhost:5000/users/user1`

Zum Löschen eines User.
`curl http://localhost:5000/users/user1 -X DELETE -v`

Zum Anlegen eines User.
`curl http://localhost:5000/users -d "username=gsingh4" -d "email=gsingh4@student.tgm.ac.at" -d "picture=imgur.com/444" -X POST -v`

## Quellen
[Flask ReST](https://flask-restful.readthedocs.io/en/latest/quickstart.html#full-example)
