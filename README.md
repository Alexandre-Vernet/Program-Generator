# Program-Generator

## Technologies
Generate fast project for :
- Angular
- React
- Express
- NX
- Laravel
- Ionic

## Locations
- All the web projects are created in the `[USER]/Documents/Dev/Web/` folder.
- All the mobile projects are created in the `[USER]/Documents/Dev/Mobile/` folder.


## Template

### Angular

Generate Angular project with :

- SCSS for styles
- Routing
- Disable strict mode

``
ng new *projectName* --style=scss --routing --strict
``

### React

Generate React project

``
npx create-react-app *projectName*
``

### Express

Generate Express project with a ```server.js``` file with dependencies :
- Express
- Axios
- Nodemon

Finally, it's add a template code with default route and server listening

```
npm init -y
```

```js
const express = require('express');
const app = express();
require('dotenv').config();
const port = process.env.PORT || 3333;

app.use(express.static('public'));
app.use(express.json());

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(port, () => {
  console.log(`App listening on port ${ port }`);
});
```

### NX

Generate NX project with :

- Angular + Nest
- ```front``` for app name
- SCSS for styles
- No nx-cloud

``
npx create-nx-workspace --preset=angular-nest --appName=front --style=scss --nx-cloud=N *projectName*
``

### Laravel

Generate Laravel project

``
composer create-project laravel/laravel *projectName* --prefer-dist"
``

### Ionic

Generate Ionic project

``
ionic start "*projectName* blank --type=angular
``
