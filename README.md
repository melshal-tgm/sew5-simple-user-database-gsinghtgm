# "Restful User-Service"

## Aufgabenstellung
Die detaillierte [Aufgabenstellung](TASK.md) beschreibt die notwendigen Schritte zur Realisierung.

## TODO Liste fuer 23.11.2018
Die [Liste](TODO.md) !

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

Zum Updaten eines User.

`curl http://localhost:5000/users/user4 -d"username=gsingh4" -d "email=gsingh3@student.tgm.ac.at" -d "picture=imgur.com/4444" -X PUT -v`

### VueJS initialisieren

* Wenn bis jetzt NodeJS noch nicht installiert ist muss das jetzt gemacht werden
* Im Ordner `/src/main/` ein Kommandofenster öffnen
* Das VueJS-CLI Packet installieren:
`npm install -g @vue/cli`
* VueJS initialisieren:
`vue init webpack`
`? Generate project in current directory? Yes`

    `? Project name <name>`\
`? Project description <description>` \
`? Author <email>` \
`? Vue build standalone` \
`? Install vue-router? Yes` \
`? Use ESLint to lint your code? No` \
`? Set up unit tests No` \
`? Setup e2e tests with Nightwatch? No` \
`? Should we run 'npm install' for you after the project has been created? npm`
* Axios zum verwenden der REST-Schnittstelle installieren
`npm install --save axios`

### 4. Client mit Vue.js auf REST-Server verbinden
Hier werden wir den generierten HelloWorldComponent verändern anstatt einen neuen zu generieren.
Im File `src/components/HelloWorld.vue` alles löschen und durch das ersetzen:
```html
<template>
  <div class="users">
    <h1>Users</h1>
    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">Username</th>
          <th scope="col">Email</th>
          <th scope="col">Picture</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(user, index) in users" :key="index">
          <td>{{ user.username }}</td>
          <td>{{ user.email }}</td>
          <td>{{ user.picture }}</td>
        </tr>
      </tbody>
    </table>

    <h2>User1</h2>
    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">Username</th>
          <th scope="col">Email</th>
          <th scope="col">Picture</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{{ user.username }}</td>
          <td>{{ user.email }}</td>
          <td>{{ user.picture }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      users: [],
      user:[]
    };
  },
  methods: {
    getUsers() {
      const path = "http://localhost:5000/users";
      axios
        .get(path)
        .then(res => {
          this.users = res.data.users;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  getUser() {
      const path = "http://localhost:5000/users/user1";
      axios
        .get(path)
        .then(res => {
          this.user = res.data.user1;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    }
  },
  created() {
    this.getUsers()
    this.getUser()
  }
};
</script>
```
#### Code erklärung:
```html
 <tr v-for="(user, index) in users" :key="index">
          <td>{{ user.username }}</td>
          <td>{{ user.email }}</td>
          <td>{{ user.picture }}</td>
        </tr>
```
Hier wird `tr v-for="(user, index) in users" :key="index` durch jedes Element der Vue-Variable `users` iteriert und der Username, Email Addresse und Bildurl jedes Users angezeigt.
```js
 data() {
    return {
      users: [],
      user:[]
    }
  }
```
Hier wird die Vue-Variable `users und user` deklariert.
```
```js
methods: {
    getUsers() {
      const path = "http://localhost:5000/users";
      axios
        .get(path)
        .then(res => {
          this.users = res.data.users;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  created() {
    this.getUsers()
  }
```
Hier werden 2 Methoden definiert:
**getUsers():**
Es wird mit dem axios Modul ein GET-Request auf die URL `http://localhost:5000/users` geschickt. Das Ergebnis wird in die Vue-Variable `users` gespeichert.
**created()**
Diese Methode wird aufgerufen wenn die Seite geladen wird. Sie ruft hier nur die `getUsers()` Methode auf.

Um den Client zu testen muss der Python Server gestartet werden und der folgende Befehl ausgefühlt werden:
`npm run dev`
Dann kann man im Browser unter `localhost:8080` überprüfen ob alles funktioniert
Wenn keine Daten aufscheinen kann es sein, dass in der Datenbank keine Daten sind.

### Cypress.io Test
* Um cypress zu installieren muss dieser Befehl ausgeführt werden:
`npm install --save cypress  cypress-vue-unit-test`
* Im `package.json` File müssen diese 2 Einträge unter `scripts` hinzugefügt werden:
```json
"scripts":{
	"cy:open": "cypress open",
	"cy:run": "cypress run"
}
```
* Um cypress zu initialisieren muss dieser Befehl ausgeführt werden:
`npm run cy:open`
* Nachdem das Fenster geladen ist und alle Dateien generiert wurden kann man das Fenster wieder schleißen
* Unter `cypress/integration` muss ein neues File namens `testing.spec.js` erstellt werden.
* Der Ordner `cypress/examples` kann gelöscht werden.

Um Vue Datein testen zu wollen, so muss man den Webpack Preprocessor in die `cypress/plugin/index.js` einfügen:
```js
const { onFileDefaultPreprocessor } = require('../../preprocessor/webpack')

module.exports = on => {
  on('file:preprocessor', onFileDefaultPreprocessor)
}
```
Den Preprocessor kann man entweder manuel runterladen oder per `npm i -D @cypress/webpack-preprocessor vue-loader vue-template-compiler css-loader` installieren.
Ein gebundener Vue Test sieht so etwa aus:
```js
import HelloWorld from '../../src/components/HelloWorld.vue'
const mountVue = require('cypress-vue-unit-test')
describe('HelloWorld', () => {
  beforeEach(mountVue(HelloWorld))

  it('Users H1', () => {
    cy.get('h1').should('contain', 'Users')
  })
  it('Read table length', () => {
    cy.get('table tr').should('have.length', 7)
  })
  it('Read Users', () => {
    cy.get('tbody>tr').eq(0).should('contain', 'gsingh@student.tgm.ac.at')
  })
})

```
### Travis CI
Travis CI dient als Testumgebung, weil "It runs on my machine" ist ein Statement das Heute nicht mehr verwendet werden kann.
Für Travis CI muss man sich auf [Travis-CI](www.travis-ci.org) anmelden und seinen GitHub Account verbinden. Dann können Repositories mit einer Travis Konfigurationsdatei gebuildet werden.
Die Travis Konfigurationsdatei muss '.travis.yml' heißen und konfiguriert werden.
Die [Travis-Documentation](https://docs.travis-ci.com/) hilft beim konfigurieren.
Die .travis.yml in diesem Projekt sieht so aus:
```
matrix:
  include:
  - stage: Tox Test
    name: "Unittesting"
    language: python
    python:
    - "3.6"
    install: pip install tox-travis
    script: tox
  - stage: Cypress Test
    name: "Cypress Testing"
    language: node_js
    node_js:
      - 10
    cache:
      npm: true
      directories:
        - ~/.npm
        - ~/.cache
      node_js:
        - '8'
    install:
      - cd src/main/vue
      - npm ci
      - pip install --user -U pip
      - pip install --user flask flask_restful flask_cors
    script:
      - python ../python/server/server.py&
      - sleep 5
      - npm run cy:run
```
Diese Konfiguration enthält 2 Stages für das Backend mit Tox und für das Frontend Cypress.
Der Erfolgreiche Build sieht so aus:

![Build](https://imgur.com/IKJg544.png)

## Quellen
[Flask ReST](https://flask-restful.readthedocs.io/en/latest/quickstart.html#full-example)
